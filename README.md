### Setup Steps
#### Set up the dependencies and awscli(one time activity)
1. Install awscli and configure it
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

2. Install the Python requirements into the packages directory (for opencv, numpy etc.)
`python3.13 -m pip install -t ./packages/ -r requirements.txt`

#### Do the following to make changes to the Lambda code
1. Create the deployment package including both, dependencies and the lambda code
`(cd packages && zip -r ../lambda.zip .) && zip -g lambda.zip lambda_function.py`
2. Upload the Lambda code to S3
`aws s3 cp lambda.zip s3://xray-image-processing/image-processing-lambda-code/`
3. Update the Lambda function to use the uploaded code
```
aws lambda update-function-code \
    --function-name xray-image-processing \
    --s3-bucket xray-image-processing \
    --s3-key lambda.zip
```

#### Other Lambda function configurations
1. Since I don't have access to create IAM roles (for Lambda execution), I used an existing role (Role name: sironaPanProcessing-role-kmm8sby4) in the Lambda function.
2. Increased the timeout to 10 seconds.
3. Generated a non-authenticated function url and added custom authentication through bearer token.
4. Generated an auth_token and set it in the environment variables (the same token needs to be passed when sending requests to the Lambda function)