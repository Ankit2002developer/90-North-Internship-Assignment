import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Lambda function to upload a document to S3.
    :param event: dict containing 'file_name', 'file_content', and 'bucket_name'
    :param context: AWS Lambda runtime information (not used here)
    :return: Upload status
    """
    try:
        # Extract file details from the event
        bucket_name = event['bucket_name']  # Target S3 bucket
        file_name = event['file_name']      # Name of the file to store
        file_content = event['file_content']  # Base64 encoded content
        
        # Decode the base64 file content
        decoded_content = base64.b64decode(file_content)
        
        # Upload the file to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=decoded_content
        )
        
        return {
            "statusCode": 200,
            "body": f"File '{file_name}' successfully uploaded to '{bucket_name}'"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
