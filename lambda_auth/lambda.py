import json

def lambda_handler(event, context):
    
    token = event.get('queryStringParameters').get("token", "")
    # 如有需要可实现更高级别的校验，比如正则匹配、参数+时间 哈希
    if token == '123456':
      return {
        "isAuthorized": True,
        "context": {
          "exampleKey": "exampleValue"
        }
      }
    else : 
      return {
        "isAuthorized": False,
        "context": {
          "exampleKey": "exampleValue"
        }
      }