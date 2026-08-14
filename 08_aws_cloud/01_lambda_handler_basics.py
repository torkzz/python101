"""
AWS Lambda Function Handler Structure in Python

Concepts:
- Lambda Handler entrypoint (`def lambda_handler(event, context)`).
- Standard AWS imports (`boto3`, `botocore.config.Config`).
- Event payload & Context metadata object.
- Logger initialization (`logging.getLogger()`, `logger.setLevel("INFO")`).
- Returning API Gateway compatible JSON response (`statusCode`, `headers`, `body`).
"""

import json
import logging
import datetime as dt
from typing import Any, Dict
import boto3
from botocore.config import Config


class DummyContext:
    """Mock AWS Lambda context object for local testing."""
    def __init__(self) -> None:
        self.function_name = "demo-lambda-function"
        self.memory_limit_in_mb = 128
        self.aws_request_id = "abc-123-xyz-789"


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Standard AWS Lambda Python function handler entrypoint."""

    # 1. Initialize logger
    logger = logging.getLogger()
    logger.setLevel("INFO")

    logger.info("Lambda execution started.")
    logger.info(f"Function Name: {getattr(context, 'function_name', 'N/A')}")
    logger.info(f"Request ID   : {getattr(context, 'aws_request_id', 'N/A')}")

    # 2. Configure AWS SDK Boto3 Client (e.g. S3 or DynamoDB)
    my_config = Config(region_name="us-east-1", retries={"max_attempts": 3})
    # s3_client = boto3.client("s3", config=my_config)

    # 3. Extract parameters from incoming event payload
    query_params = event.get("queryStringParameters") or {}
    user_name = query_params.get("name", "Developer")

    # 4. Construct JSON response body
    response_body = {
        "message": f"Hello {user_name}, welcome to AWS Lambda!",
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
        "event_keys": list(event.keys()),
    }

    # 5. Return API Gateway compatible HTTP response dictionary
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(response_body),
    }


def main() -> None:
    print("=== AWS Lambda Function Handler Local Test ===")

    # Mock API Gateway HTTP GET Event Payload
    mock_event = {
        "resource": "/hello",
        "path": "/hello",
        "httpMethod": "GET",
        "queryStringParameters": {"name": "Alex"},
        "body": None,
    }

    mock_context = DummyContext()

    # Execute lambda_handler locally
    result = lambda_handler(mock_event, mock_context)

    print(f"\nResponse Status Code: {result['statusCode']}")
    print("Response Headers    :", result["headers"])
    print("Parsed Response Body:")
    print(json.dumps(json.loads(result["body"]), indent=2))


if __name__ == "__main__":
    main()
