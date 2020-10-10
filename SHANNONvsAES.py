import datetime
import onetimepad
from Crypto.Cipher import AES
from random import choice
from string import ascii_uppercase
import pandas as pd
import my_parameters


def OTPenc(OTPmessage, OTPkey, AESkey, AnzahlVorgaenge):

    # print('imputs OTP')
    # print(OTPmessage, OTPkey, AESkey, AnzahlVorgaenge)
    begin_otp = datetime.datetime.now()

    for i in range(1, AnzahlVorgaenge):
        # onetimepad.encrypt(str(OTPmessage), str(OTPkey))
        for m, k in zip(OTPmessage, OTPkey):
            my_otp = m ^ k

    end_otp = datetime.datetime.now()
    time_diff_otp = end_otp - begin_otp

    return time_diff_otp


def AESenc(AESmessage, OTPkey, AESkey, AnzahlVorgaenge):

    begin_aes = datetime.datetime.now()

    for i in range(1, AnzahlVorgaenge):
        cipher = AES.new(AESkey, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(AESmessage)

    end_aes = datetime.datetime.now()
    time_diff_aes = end_aes - begin_aes

    return time_diff_aes


def createMSGorKEY(in_length):
    ret = ''.join(choice(ascii_uppercase) for i in range(in_length)).encode('utf8')
    return ret


Nachrichtenlaenge = []
AnzahlVerschluesselungen = []
ZeitOTP = []
ZeitAES = []


total_begin = datetime.datetime.now()

# start @ 1
for ik in range(my_parameters.AnzahlVerschluesselungen_iter, my_parameters.AnzahlVerschluesselungen_iter + 1):
    for j in range(1, my_parameters.Nachrichtenlaenge_iter + 1):
        iter_msg = createMSGorKEY(j)
        iter_AES_key = createMSGorKEY(32)
        iter_OTP_key = createMSGorKEY(j)

        # print(iter_msg, iter_AES_key, iter_OTP_key)

        Nachrichtenlaenge.append(j)
        AnzahlVerschluesselungen.append(ik)
        ZeitOTP.append(OTPenc(iter_msg, iter_OTP_key, iter_AES_key, ik))
        ZeitAES.append(AESenc(iter_msg, iter_OTP_key, iter_AES_key, ik))

        iter_msg = iter_AES_key = iter_OTP_key = None

        print('länge: ', j, '/', my_parameters.Nachrichtenlaenge_iter)

    print('anzahl: ', ik, '/', my_parameters.AnzahlVerschluesselungen_iter)

print('Nachrichtenlaenge: ', Nachrichtenlaenge)
print('AnzahlVerschluesselungen: ', AnzahlVerschluesselungen)
print('ZeitAES: ', ZeitAES)
print('ZeitOTP: ', ZeitOTP)

df = pd.DataFrame(list(zip(Nachrichtenlaenge, AnzahlVerschluesselungen,
                           [(i.days * 86400000) + (i.seconds * 1000) + (i.microseconds / 1000) for i in ZeitAES],
                           [(i.days * 86400000) + (i.seconds * 1000) + (i.microseconds / 1000) for i in ZeitOTP]
                           )),
               columns =['Nachrichtenlaenge', 'AnzahlVerschluesselungen', 'ZeitAES', 'ZeitOTP'])

print('Nachrichtenlaenge: ', Nachrichtenlaenge)
print('AnzahlVerschluesselungen: ', AnzahlVerschluesselungen)
print('ZeitAES: ', ZeitAES)
print('ZeitOTP: ', ZeitOTP)

df.to_pickle("ergebnisse/dummy_LengthVStime.pkl")
# df.to_pickle("ergebnisse/dummy_AnzahlVStime.pkl")

print(datetime.datetime.now() - total_begin)
