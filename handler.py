import json
import boto3

def operations(event, context):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000");
    if(event["operation"]="get"):
        response=get(event,dynamodb)
    elif(event["operation"]="create"):
        response=create(event,dynamodb)
    elif(event["operation"]="update"):
        response=update(event,dynamodb)
    else:
        response=delete(event,dynamodb)
    
    body = {
        "message": "Operation executed successfully!",
        "response": response
    }

    final_response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return final_response
def get(event,dynamodb):
    username=event['username']
    table = dynamodb.Table('UserTable')
    response = table.get_item(Key={'username': username})
    return response
def create(event,dynamodb):
    table = dynamodb.create_table(
    TableName='UserTable',
    KeySchema=
    {
        'AttributeName': 'username',
        'KeyType': 'HASH'
    },
    AttributeDefinitions=
    {
        'AttributeName': 'password',
        'AttributeType': 'RANGE'
    },
    ProvisionedThroughput={
    'ReadCapacityUnits': 1,
    'WriteCapacityUnits': 1
    }
    )
    return table.table_status
def update(event,dynamodb):
    username=event["username"]
    password=event["password"]
    table = dynamodb.Table('UserTable')
    response = table.update_item(
        Key={
            'username': username,
        },
        UpdateExpression = 'SET password = :val1',
        ExpressionAttributeValues={':val1': password }
    )
    return response
def delete(event,dynamodb):
    username=event["username"]
    table = dynamodb.Table('UserTable')
    response = table.delete_item(
        Key={
            'username': username
        }
    )
    return response
    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
