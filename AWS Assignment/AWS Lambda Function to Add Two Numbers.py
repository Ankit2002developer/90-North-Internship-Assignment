def lambda_handler(event, context):
    """
    Lambda function to add two numbers.
    :param event: dict with 'num1' and 'num2' as keys
    :param context: AWS Lambda runtime information (not used here)
    :return: Sum of the two numbers
    """
    try:
        # Extract numbers from the event object
        num1 = event['num1']
        num2 = event['num2']
        
        # Calculate the sum
        result = num1 + num2
        
        return {
            "statusCode": 200,
            "body": {
                "message": "Addition successful",
                "num1": num1,
                "num2": num2,
                "result": result
            }
        }
    except KeyError:
        return {
            "statusCode": 400,
            "body": "Invalid input: 'num1' and 'num2' are required in the event."
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
