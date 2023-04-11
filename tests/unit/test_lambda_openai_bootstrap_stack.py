import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_openai_bootstrap.lambda_openai_bootstrap_stack import LambdaOpenaiBootstrapStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_openai_bootstrap/lambda_openai_bootstrap_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaOpenaiBootstrapStack(app, "lambda-openai-bootstrap")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
