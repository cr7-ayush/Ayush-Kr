import json,boto3

def lambda_handler(event, context):
    InvokeLam = boto3.client("lambda", region_name="us-east-2")
    payload = { "presid" : "1Xhv_wk_QDuNPLsdYPbAJe_BO9xVkdCr3XMe65cc4g_s" }
    requests = []
    requests.append({
        'deleteText': {
            'objectId': "gc6f80d1ff_0_1",
            'textRange': {
                'type':  "ALL"
                }
            }
        })
    requests.append({
        'insertText': {
            'objectId': "gc6f80d1ff_0_1",
            'insertionIndex': "0",
            'text': "test"
            }
        })
    payload.update({"body" : requests})
    response = InvokeLam.invoke(FunctionName = "UpdateSlide-Core", InvocationType = "RequestResponse", Payload = json.dumps(payload))
    print(payload)
    return {'Result': json.loads(response["Payload"].read())}
