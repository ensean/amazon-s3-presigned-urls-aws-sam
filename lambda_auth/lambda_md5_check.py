import json
import hashlib

# SALT+key 计算 md5，来校验请求是否合法，必要的话 SALT 可以通过后端下发
SALT = 'HelloWorld'

def lambda_handler(event, context):
    
    token = event.get('queryStringParameters').get("token", "")
    key = event.get('queryStringParameters').get("key", "")
    
    hash = hashlib.md5((SALT+key).encode('utf-8')).hexdigest()
    
    if token == hash:
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