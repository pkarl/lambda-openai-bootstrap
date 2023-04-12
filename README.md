# lambda-openai-bootstrap

> ### 🚨 **CAUTION** 🚨
> This is beta software that generates un-auth'd API gateway endpoints which use OpenAI APIs. Do not share those
> endpoints with anyone.
> For now, I encourage you to destroy the infra after use. Command below.

> TODO: add auth

> TODO: add github action(s)

> TODO: add message queue + trigger

## Prerequisites

1. [AWS Account](https://aws.amazon.com/)
2. [AWS CLI](https://aws.amazon.com/cli/) - [Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
3. [Node.js](https://nodejs.org/en/) (version 14 or higher) - [Installation Guide](https://nodejs.org/en/download/)
4. [Python](https://www.python.org/) (version 3.9 or higher) - [Installation Guide](https://www.python.org/downloads/)
5. [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) - Install the AWS CDK by
   running `npm install -g aws-cdk`
6. [OpenAI API Key](https://www.openai.com/) - detailed instructions at the bottom of README

## Setup

### 1. Clone this repo

```bash
$ git clone https://github.com/pkarl/lambda-openai-bootstrap.git`
$ cd lambda-openai-bootstrap
```

### 2. Create & activate the virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
```

> Windows: `.venv\Scripts\activate`

### 3. Install python packages for CDK App _and_ for Lambda Layer

```bash
pip install -r requirements.txt
cd layer
pip install -r requirements.txt -t python
cd ..
```

### 4. Configure the AWS CLI

```bash
aws configure 

# Follow the prompts to input your ...
# AWS Access Key ID, 
# AWS Secret Access Key, 
# Default region name, 
# and Default output format
```

## Usage (Local)

### 0. [optional] Customize the lambda function(s)

In the `/lambda` directory, modify the `lambda_function_chat.py` or add
additional `lambda_function_[custom name here].py` files to use the
desired OpenAI APIs. Update the `lambda_openai_bootstrap/lambda_openai_bootstrap_stack.py` file accordingly (search
for `PUT ADDITIONAL LAMBDA FUNCTIONS HERE`...).

### 1. Add OpenAI API key to env

```bash
export OPENAPI_KEY=AA-0000000000000000000000000000000000000000000
````

### 2. Smoke Test your AWS infra locally

This will run cdk commands to simulate a build and generate cloudformation templates (and will reveal nasty bugs along
the way).

```bash
python app.py
```

### 3. Deploy the AWS infrastructure using CDK

```bash
cdk bootstrap
cdk deploy
```

### 4. Test the deployed Lambda function(s)

After the deployment is complete, you will see the API Gateway URL(s) in the terminal output. Use these URLs to make
HTTP requests and test the Lambda functions.

ex:

```bash
$ http post https://000000000A.execute-api.us-east-1.amazonaws.com/prod/ prompt="what's a good compliment for an ugly person?" -v
```

> 👆 uses httpie (https://httpie.io/)

### 5. Clean up / Destroy resources

When you no longer need the resources, run the following command to delete them:

```bash
cdk destroy
```

## Usage (GitHub Actions)

## FAQ

idk, file an issue or leave a comment to get this party started.

## Retrieving OpenAI API Keys

Follow these steps to obtain your OpenAI API keys:

1. **Sign up for an OpenAI account**:

   If you don't already have an account, sign up for an OpenAI account by visiting
   the [OpenAI website](https://www.openai.com/) and clicking on the "Sign up" button.

2. **Log in to your OpenAI account**:

   Log in to your OpenAI account by visiting the [OpenAI website](https://www.openai.com/) and clicking on the "Log in"
   button.

3. **Navigate to the API keys page**:

   Once logged in, click on your profile icon in the top right corner and select "API keys" from the dropdown menu.

4. **Generate a new API key**:

   On the API keys page, click on the "Create" button to generate a new API key. A unique key will be generated, and you
   can provide a description (optional) to help you remember its purpose.

   > **Note**: Keep your API key secret and never share it publicly. It's essential to treat your API keys like
   passwords, as they grant access to
