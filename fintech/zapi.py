import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':'J37FJD9FLS9Q6LB8A6B2JKWK67SEATS4',
  'secret':'U5LAWCSG52EVMT4K',
  'usetype':'stage',
  'phone': +918360581227,
  'message':'hello user',
  'senderid':'hackpro'
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
# print response.text
