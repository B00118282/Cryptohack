from Crypto.PublicKey import RSA

with open('privacy_enhanced_mail.pem','r') as key_file:
    key = RSA.importKey(key_file.read())
    print(key)



#from Crypto.PublicKey import RSA
#pemkey = open(pemkey).read()
#RSA.importKey(f.read(pemkey, passphrase=None))