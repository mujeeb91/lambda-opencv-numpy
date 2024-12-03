#### Setup Steps
##### Step 1: Deploy dependencies and code
Install the Python requirements into the package directory
`python3.13 -m pip install --target ./packages/ --requirement requirements.txt`

Create the deployment package including both the dependencies and the lambda_function.py file
`(cd packages && zip -r ../lambda.zip .) && zip -g lambda.zip lambda_function.py`


`aws s3 cp lambda.zip s3://xray-image-processing/image-processing-lambda-code/`
`aws s3 cp lambda.zip s3://mujeeb91/v/`

```
aws lambda update-function-code \
    --function-name vImageProcessing \
    --s3-bucket mujeeb91 \
    --s3-key v/lambda.zip
```

Lambda Object URL:
https://mujeeb91.s3.us-east-2.amazonaws.com/v/lambda.zip