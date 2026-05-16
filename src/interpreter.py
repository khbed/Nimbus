ACTIONS = {
    "list lambdas": {
        "service": "lambda",
        "action": "list_functions",
        "params": {}
    },
    "list ec2": {
        "service": "ec2",
        "action": "describe_instances",
        "params": {}
    },
    "list s3": {
        "service": "s3",
        "action": "list_buckets",
        "params": {}
    },
    "list s3 buckets": {
        "service": "s3",
        "action": "list_buckets",
        "params": {}
    },
    "list iam users": {
        "service": "iam",
        "action": "list_users",
        "params": {}
    },
    "list users": {
        "service": "iam",
        "action": "list_users",
        "params": {}
    },
}

def parse(user_input: str) -> dict | None:
    normalized = user_input.strip().lower()

    if normalized in ACTIONS:
        return ACTIONS[normalized]

    for key, action in ACTIONS.items():
        if key in normalized:
            return action

    return None