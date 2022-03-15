test = " union select 0x61646d696e#"
for character in test:
    print(str(hex(ord(character)))[2:],end='')