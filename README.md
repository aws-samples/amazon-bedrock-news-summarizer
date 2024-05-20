# Amazon Bedrock News Summarizer

Amazon bedrock project demonstrates how to add Bedrock Agent calling news data source from the web and integrating with Amazon Bedrock. The code fetch news from multiple RSS feeds, APIs and utilize Amazon Bedrock to process and generate list of news and summary based on the fetched news data. It integrates news data from RSS feeds from Cointelegraph, GNews and NewsAPI, formats it, and sends it to an Amazon Bedrock Anthropic Claude models(interchangeable) for summary of list of latest  news.

## Features

- **News Data Retrieval**: Fetch news from the RSS feeds, GNews and NewsAPI services. You can add or remove RSS feeds and APIs based on your requirememnts.
- **Amazon Bedrock Integration**: Use Amazon Bedrock to invoke a machine learning model that processes news data.
- **Modular Design**: Easily extendable for additional news sources like RSS feeds, news Apis by implementing a base news fetcher class.

## Overview

This news summarizer tool leverages Amazon Bedrock's powerful language models to fetch and condense news articles. It utilizes a flexible framework that can integrate multiple news sources, including GNews, NewsAPI, and RSS feeds. This system is designed to be easily expandable, allowing for the seamless addition of new sources.
The tool's core is a base class called NewsFetcher, which defines a standard way for subclasses to retrieve and format news data from various APIs and RSS feeds.  This modular approach ensures the code is maintainable and adaptable as new sources are added.
By combining this fetched news data, the tool harnesses the capabilities of Amazon Bedrock's language models, effectively summarizing the most relevant information into concise summaries. This streamlined process is facilitated by libraries like boto3, langchain, and langchain-aws, resulting in a powerful and efficient news summarization solution.


## Setup

### Prerequisites

- Python 3.6 or higher
- Boto3
- urllib
- NewsAPI Python Client
- AWS CLI configured with appropriate AWS credentials
- langchain
- langchain-aws

### Python Libraries
To run the news-summarizer script, you will need to install several Python libraries. These include:

boto3: AWS SDK for Python, used for interacting with AWS services including AWS Bedrock.
urllib.request: A module for opening URLs, used to fetch news data from the GNews API.
NewsAPI Python Client: A client library to fetch news from NewsAPI.
You can install these libraries using pip:

```
pip install requirements.txt
```
### AWS Configuration and Credentials
Before you can interact with AWS services through boto3, you need to configure your AWS credentials:

AWS CLI Installation: First, ensure that AWS CLI is installed on your system.

```
pip install awscli
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


6. Security Considerations
   
* Secure Network Isolation: Deploy the news summarizer within a Virtual Private Cloud (VPC) to restrict network access. Configure security groups to allow outbound connections only to the necessary APIs (GNews, NewsAPI) and RSS feed endpoints.

* Least Privilege IAM Roles:  Create IAM roles with the minimum permissions required for the summarizer to interact with Bedrock and other AWS services. Avoid using overly permissive roles to reduce the potential impact of any security breaches.

* Content Filtering with Bedrock Guardrails: Utilize Amazon Bedrock's built-in content filtering mechanisms or custom guardrails to filter out inappropriate or harmful content from the generated summaries.

* Human-in-the-Loop Review: Implement a human review process for the final summaries before they are published or used for decision-making. This ensures accuracy and prevents the spread of misinformation or biased content.
* API Rate Limiting: Monitor and enforce rate limits for API calls to GNews and NewsAPI. This prevents abuse and ensures fair usage of these external services.

* Error Handling and Logging: Implement comprehensive error handling to catch and log exceptions that occur during news fetching or summarization. This helps with debugging and identifying potential security issues.

* Secrets Management: Store API keys and other sensitive information securely. Consider using a secrets management service like AWS Secrets Manager to store and retrieve credentials in a secure manner.

* Data Encryption: Encrypt sensitive data at rest and in transit to protect it from unauthorized access.

* Vulnerability Scanning: Regularly scan your code and dependencies for known vulnerabilities. Keep libraries and packages up-to-date to address any security patches.

* Least Privilege Access to RSS Feeds: When accessing RSS feeds, use a non-privileged user or service account to limit the potential impact of any compromised feed.


## Note
You may have to subscribe news-api and gnews for API access or use the RSS feeds. When using RSS feeds in this code, be mindful of the structure and consistency of different feeds, as it can vary. Implement robust error handling to gracefully manage cases where feeds are unavailable or contain unexpected formats.















