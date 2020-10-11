# from SHANNONvsAES import AESenc, createMSGorKEY
import pandas as pd
import datetime
from random import choice
from string import ascii_uppercase
from matplotlib import pyplot as plt
from Crypto.Cipher import AES
# from Cryptodome.Cipher import AES
from Crypto.Random import get_random_bytes

def AESenc(AESmessage, AESkey, AnzahlVorgaenge):

    begin_aes = datetime.datetime.now()

    for i in range(0, AnzahlVorgaenge):
        cipher = AES.new(AESkey, AES.MODE_EAX)
        nonce = cipher.nonce
        #ciphertext, tag = cipher.encrypt_and_digest(AESmessage)
        ciphertext = cipher.encrypt(AESmessage)
        #print(min(AESmessage))

    time_diff_aes = datetime.datetime.now() - begin_aes
    begin_aes = None

    return time_diff_aes


def createMSGorKEY(in_length):
    # ret = ''.join(choice(ascii_uppercase) for i in range(in_length)).encode('utf8')
    return get_random_bytes(in_length)

ZeitAES = []
Nachrichtenlaenge = []

# Anzahl Verschlüsselungen:
ik = 5

# Länge:
length = 5000
print(get_random_bytes(32))



total_begin = datetime.datetime.now()

# for j in range(1, length):
for j in range(1, length*100, length):
    print('länge: ', j, '/', length)
    iter_msg = createMSGorKEY(j)
    iter_AES_key = createMSGorKEY(16)


    ZeitAES.append(AESenc(iter_msg, iter_AES_key, ik))
    Nachrichtenlaenge.append(j)

    #iter_msg = iter_AES_key = None

    print('länge: ', j, '/', length)

df = pd.DataFrame(list(zip(Nachrichtenlaenge,
                           [(i.days * 86400000) + (i.seconds * 1000) + (i.microseconds / 1000) for i in ZeitAES]
                           )),
               columns =['Nachrichtenlaenge', 'ZeitAES'])



df.to_pickle("ergebnisse/dummy_LengthVStime_aes.pkl")
# df.to_pickle("ergebnisse/dummy_AnzahlVStime.pkl")

print(datetime.datetime.now() - total_begin)

#print(df)

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
ax1.plot(df['Nachrichtenlaenge'], df['ZeitAES'], color='k', marker='o', markersize=1,
         linewidth=0.1, label=str('AES-256'))



ax1.set_xlabel('Message Length [byte]')
ax1.set_ylabel('Encryption Time [ms]')
# ax1.set_title(str('Constant Message Length: ' + str(my_parameters.Nachrichtenlaenge_iter) + ' Bytes'))
# ax1.set_ylim(ymin=0, ymax=cr_ylim)
ax1.set_xlim(xmin=0)
plt.legend()
plt.grid(color='0.7', linestyle='dotted', linewidth=0.5)
# fig1.savefig('C:/Users/blue/Documents/Forschungsprojekt-FUH/Ausarbeitung/Abbildungen/plots/AnzahlVStime_english.svg',
# fig1.savefig('ergebnisse/AnzahlVStime_english.svg', format='svg', orientation='landscape', pad_inches=0, dpi=1200)

fig1.show()
plt.show()