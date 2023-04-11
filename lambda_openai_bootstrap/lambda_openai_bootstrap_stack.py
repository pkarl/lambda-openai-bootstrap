import os

from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_apigateway as apigw,
    aws_secretsmanager as secretsmanager,
    SecretValue
)

from constructs import Construct


class LambdaOpenaiBootstrapStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        openapi_key = os.environ.get("OPENAPI_KEY")

        # Lambda Layer with Python dependencies
        layer = _lambda.LayerVersion(
            self, "OaiLayer",
            code=_lambda.Code.from_asset("layer"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_9],
            description="Lambda layer with Python dependencies"
        )

        # IAM role with relevant permissions
        role = iam.Role(
            self, "OaiLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        openapi_secret = secretsmanager.Secret(self, "OPENAPI_KEY",
                                               description="OpenAPI key from local environment variable",
                                               secret_string_value=SecretValue.unsafe_plain_text(openapi_key)
                                               )

        openapi_secret.grant_read(role)

        # Lambda function with outgoing HTTP request
        chat_function = _lambda.Function(
            self, "OaiChatCompletionLambda",
            code=_lambda.Code.from_asset("lambda"),
            handler="lambda_function_chat.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            role=role,
            layers=[layer],
            timeout=Duration.seconds(30),
            environment={
                "OPENAPI_SECRET_ARN": openapi_secret.secret_arn
            }
        )

        # API Gateway without IAM authentication
        api = apigw.LambdaRestApi(
            self, "OpenApiChatApi",
            handler=chat_function,
            proxy=True
        )

        # Define the root resource
        root_resource = api.root

        # Add a GET method to the root resource
        root_resource.add_method("POST", api_key_required=False)
