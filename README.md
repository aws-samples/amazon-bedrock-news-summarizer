# Amazon Bedrock News Summarizer

This Python project demonstrates how to fetch news from multiple APIs and utilize AWS Bedrock to process and generate text based on the fetched news data. It integrates news data from GNews and NewsAPI, formats it, and sends it to an AWS Bedrock machine learning model for natural language processing.

## Features

- **News Data Retrieval**: Fetch news from the GNews and NewsAPI services. You can additional APis based on your requirememnts.
- **AWS Bedrock Integration**: Use AWS Bedrock to invoke a machine learning model that processes news data.
- **Modular Design**: Easily extendable for additional news sources by implementing a base news fetcher class.

## Overview
The news-summarizer code provided establishes a scalable framework designed to seamlessly integrate additional news APIs as needed. It uses modular programming principles centered around a base class, NewsFetcher, which specifies a method fetch_news that must be implemented by any subclass. This method sets the contract for fetching news, which is individually implemented by GNewsFetcher and NewsAPIFetcher to interact with their respective APIs. This architecture not only facilitates the current functionality of fetching and formatting news data from GNews and NewsAPI but also simplifies the process of integrating more news sources. By creating new subclasses of NewsFetcher, developers can easily extend the application to include more APIs. Each subclass manages its own API interactions and formats the fetched data, which is then aggregated and processed by AWS Bedrock's machine learning model via boto3 for advanced natural language processing. This approach ensures that the system remains adaptable and maintainable, supporting ongoing expansion and customization without significant restructuring.


## Setup

### Prerequisites

- Python 3.6 or higher
- Boto3
- urllib
- NewsAPI Python Client
- AWS CLI configured with appropriate AWS credentials

### Python Libraries
To run the news-summarizer script, you will need to install several Python libraries. These include:

boto3: AWS SDK for Python, used for interacting with AWS services including AWS Bedrock.
urllib.request: A module for opening URLs, used to fetch news data from the GNews API.
NewsAPI Python Client: A client library to fetch news from NewsAPI.
You can install these libraries using pip:

```
pip install boto3 newsapi-python
```
### AWS Configuration and Credentials
Before you can interact with AWS services through boto3, you need to configure your AWS credentials:

AWS CLI Installation: First, ensure that AWS CLI is installed on your system.

```
pip install awscli
```
 Install the libraries for news-api
```
pip install newsapi-python
```
### Configure AWS CLI: Set up your AWS credentials (AWS Access Key ID and AWS Secret Access Key) and default region using the AWS CLI. These credentials should be associated with an AWS account that has permissions to access the required AWS services.

```
aws configure
```

### AWS IAM Roles and Permissions
Create a user with administrative access and secure your AWS account root user by enabling multi-factor authentication. Finally, request access to the desired Amazon Bedrock models through the AWS Management Console, ensuring all API and user permissions are properly configured for compliance and operational needs.

#### Sample IAM Role for Amazon Bedrock Usage:
Here's an example of an IAM role JSON policy document that grants necessary permissions to use Amazon Bedrock, specifically tailored for allowing the invocation of models and managing API interactions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "BedrockModelInvoke",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": [
                "arn:aws:bedrock:*:123456789012:model/*"
            ]
        },
        {
            "Sid": "ManageAPIInteractions",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetModel",
                "bedrock:ListModelVersions",
                "bedrock:ListModels"
            ],
            "Resource": "*"
        }
    ]
}

```

### Environment Variables
Set environment variables for the API keys needed for GNews and NewsAPI, ensuring they are securely stored  in the enviroment or in AWS Secrets Manager and accessible in your development environment:

```
export GNEWS_API_KEY='your_gnews_api_key_here'
export NEWS_API_KEY='your_news_api_key_here'
```

6. Security Considerations
Make sure that your script and environment adhere to best security practices, such as not hardcoding sensitive information (like API keys and AWS credentials) directly in the script. Use environment variables or secure vaults like AWS Secrets Manager for handling sensitive data.


## Note
You will have to subscribe news-api and gnews api to use this code. 















