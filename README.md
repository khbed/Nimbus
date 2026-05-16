# Nimbus
Nimbus lets you manage AWS in plain English. No docs, no console, just tell it what you want.

## Prerequisites

### 1. Install the AWS CLI

Follow the official guide for your platform:
[https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions)

### 2. Configure your credentials

You'll need an AWS Access Key ID and Secret Access Key. If you don't have one:

1. Log in to the [AWS Console](https://console.aws.amazon.com)
2. Go to **IAM → Users → Your user → Security credentials**
3. Click **Create access key**
4. Copy both the key ID and secret

Then run:

```bash
aws configure
```

You'll be prompted for:

AWS Access Key ID: YOUR_ACCESS_KEY
AWS Secret Access Key: YOUR_SECRET_KEY
Default region name: us-east-1
Default output format: json

### 3. Verify it works

```bash
aws sts get-caller-identity
```

If you see your account ID and user ARN, you're good to go.