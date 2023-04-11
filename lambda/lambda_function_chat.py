import os
import json
import openai
import boto3


def lambda_handler(event, context):
    prompt = json.loads(event.get('body')).get('prompt')
    model = "gpt-3.5-turbo"

    # Retrieve the secret ARN from the environment variable
    secret_arn = os.environ["OPENAPI_SECRET_ARN"]

    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId=secret_arn)
    openapi_key = response["SecretString"]

    openai.api_key = openapi_key

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
    except openai.error.RateLimitError:
        return {
            "statusCode": 429,
            "headers": {},
            "body": 'RateLimitError from Open API'
        }

    response_text = response['choices'][0]['message']['content']

    if response_text is None:
        return {
            "statusCode": 500,
            "headers": {},
            "body": 'None'
        }

    return {
        "statusCode": 200,
        "headers": {},
        "body": response_text.strip()
    }
