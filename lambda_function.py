import json

def lambda_handler(event, context):
    # TODO implement
    print("This is Version 3")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda Version 3!')
