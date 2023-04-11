#!/usr/bin/env python3
import aws_cdk as cdk

from lambda_openai_bootstrap.lambda_openai_bootstrap_stack import LambdaOpenaiBootstrapStack

app = cdk.App()
LambdaOpenaiBootstrapStack(app, "LambdaOpenaiBootstrapStack")

app.synth()
