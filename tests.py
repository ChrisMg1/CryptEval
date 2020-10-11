from Crypto.Cipher import AES
import onetimepad
from random import choice
from string import ascii_uppercase

AESkey = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".encode('utf8')
AESmsg = "hello, there".encode('utf8')

print(AESmsg)
# print(AESmsg.encode('utf8'))

cipher = AES.new(AESkey, AES.MODE_EAX)

cipher = AES.new(AESkey, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext = cipher.encrypt(AESmsg)

print(ciphertext)

d_cipher = AES.new(AESkey, AES.MODE_EAX, cipher.nonce)

# cipher.update()

cleartext = d_cipher.decrypt(ciphertext)


print(cleartext.decode('utf8'))



otp_cipher = onetimepad.encrypt('some text', 'andom_key')
print(otp_cipher)

otp_msg = onetimepad.decrypt(otp_cipher, 'andom_key')
print(otp_msg)

def createMSGorKEY(in_length):
    ret = ''.join(choice(ascii_uppercase) for i in range(in_length)).encode('utf8')
    return ret

print(createMSGorKEY(8))

a = [1,2,3]

print(a)

b = a.copy()

print(b)

a.append(4)

print(b)
