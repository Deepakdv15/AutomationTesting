import json
import requests
import jsonpath
# odict='{"key1":"value1","key2":"value2"}'
# json_result=json.loads(odict)
# print(json_result)
url="https://reqres.in/api/users?page=2"
response=requests.get(url)
print(response.text)
assert response.status_code==200

json_response=json.loads(response.text)
print(json_response)
data=jsonpath.jsonpath(json_response,"total")
print(data[0])
data=jsonpath.jsonpath(json_response,"data[0].first_name")
print(data[0])

for val in json_response["data"]:
    print(val["email"])