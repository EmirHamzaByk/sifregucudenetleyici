import re

def check_password_strength(password):
    if len(password) < 8:
        return "Zayıf. Lütfen en az 8 karakter içeren bir şifre kullanın."
    elif not re.search("[a-z]", password):
        return "Zayıf. Lütfen küçük harfleri içeren bir şifre kullanın."
    elif not re.search("[A-Z]", password):
        return "Zayıf. Lütfen büyük harfleri içeren bir şifre kullanın."
    elif not re.search("[0-9]", password):
        return "Orta. Lütfen rakamları içeren bir şifre kullanın veya özel karakterler ekleyin."
    elif not re.search("[!@#%&! @ # $ % ^ & * ( ) _ - + = { } [ ] \ | ; : '  , . < > / ?]", password):
        return "Orta. Lütfen özel karakterleri içeren bir şifre kullanın veya rakamlar ekleyin."
    else:
        return "Güçlü"
banner = """       
**************************************
*************EmirhamzaByk*************
************************************** 
"""
print(banner)

while True:
    password = input("Lütfen şifrenizi giriniz (kapatmak için 'kapat'): ")
    if password == 'kapat':
        break
    print("Şifreniz , ", check_password_strength(password))
