import boto3
from botocore.exceptions import BotoCoreError, ClientError

def execute(action: dict) -> dict:
    service = action["service"]
    method_name = action["action"]
    params = action.get("params", {})

    try:
        client = boto3.client(service)
        method = getattr(client, method_name)
        response = method(**params)
        return { "ok": True, "data": response }

    except ClientError as e:
        code = e.response["Error"]["Code"]
        message = e.response["Error"]["Message"]
        return { "ok": False, "error": f"{code}: {message}" }

    except BotoCoreError as e:
        return { "ok": False, "error": str(e) }

    except Exception as e:
        return { "ok": False, "error": f"Unexpected error: {str(e)}" }