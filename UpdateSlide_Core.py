import json,boto3
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def lambda_handler(event, context):
    
    s3 = boto3.client("s3")
    bucket = 'credsholder123'
    key = 'authfile.json'
    fileObj = s3.get_object(Bucket=bucket, Key=key)
    fileData = json.loads(fileObj["Body"].read().decode('utf-8'))
    
    creds = Credentials(token=fileData['access_token'],
                        refresh_token=fileData['refresh_token'],
                        client_id=fileData['client_id'],
                        token_uri=fileData['token_uri'],
                        client_secret=fileData['client_secret'])
    service = build('slides', 'v1', credentials=creds, cache_discovery=False)
    data = {
         "requests" : event['body'] 
     }
    response = service.presentations().batchUpdate(presentationId=event['presid'], body=data).execute()
    return {
         'statusCode': 200,
         'body': json.dumps('Success!'),
         'Slide Object ID': response.get('objectId')
    }