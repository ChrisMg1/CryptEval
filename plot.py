from matplotlib import pyplot as plt
import pandas as pd
import my_parameters
import math
import sys
import tikzplotlib
from mpl_toolkits.mplot3d import Axes3D

def roundup(in_time):
    return int(math.ceil(in_time / 50.0)) * 50

lang_plot = 'ger'
platform = 'pi'


if platform == 'pc':
    # df = pd.read_pickle("dummy_AnzahlVStime.pkl")
    df = pd.read_pickle("dummy_LengthVStime.pkl")
    LaengeKonst = df[df["Nachrichtenlaenge"] == my_parameters.Nachrichtenlaenge_iter]
    AnzahlKonst = df[df["AnzahlVerschluesselungen"] == my_parameters.AnzahlVerschluesselungen_iter]

elif platform == 'pi':
    #
    df = pd.read_pickle("Z:/mycm_crypto/CryptEval/dummy_LengthVStime_raspi.pkl")
    LaengeKonst = df[df["Nachrichtenlaenge"] == my_parameters.Nachrichtenlaenge_raspi]
    AnzahlKonst = df[df["AnzahlVerschluesselungen"] == my_parameters.AnzahlVerschluesselungen_raspi]

else:
    sys.exit("invalid platform")


cr_ylim = roundup(max(max(AnzahlKonst['ZeitAES']), max(AnzahlKonst['ZeitOTP']), max(LaengeKonst['ZeitAES']), max(LaengeKonst['ZeitOTP'])))

print(cr_ylim)

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
ax1.plot(LaengeKonst['AnzahlVerschluesselungen'], LaengeKonst['ZeitAES'], color='k', marker='o', markersize=1.5,
         linewidth=0.1, label=str('AES-256'))
ax1.plot(LaengeKonst['AnzahlVerschluesselungen'], LaengeKonst['ZeitOTP'], color='0.7', marker='s', markersize=1.5,
         linewidth=0.1, label=str('SIKAF (OTP)'))

if lang_plot == 'eng':
    ax1.set_xlabel('number of encryptions [n]')
    ax1.set_ylabel('time [ms]')
    ax1.set_title(str('Constant Message Length: ' + str(my_parameters.Nachrichtenlaenge_iter) + ' Bytes'))
    ax1.set_ylim(ymin=0, ymax=cr_ylim)
    ax1.set_xlim(xmin=0)
    plt.legend()
    plt.grid(color='0.7', linestyle='dotted', linewidth=0.5)
    # fig1.savefig('C:/Users/blue/Documents/Forschungsprojekt-FUH/Ausarbeitung/Abbildungen/plots/AnzahlVStime_english.svg',
    fig1.savefig('AnzahlVStime_english.svg',
                 format='svg', orientation='landscape', pad_inches=0, dpi=1200)

elif lang_plot == 'ger':
    ax1.set_xlabel('Anzahl Maskierungen [n]')
    ax1.set_ylabel('Zeit [ms]')
    ax1.set_title(str('Nachrichtenlänge konstant bei ' + str(my_parameters.Nachrichtenlaenge_iter) + ' Bytes'))
    ax1.set_ylim(ymin=0, ymax=cr_ylim)
    ax1.set_xlim(xmin=0)
    plt.legend()
    plt.grid(color='0.7', linestyle='dotted', linewidth=0.5)
    # fig1.savefig('C:/Users/blue/Documents/Forschungsprojekt-FUH/Ausarbeitung/Abbildungen/plots/AnzahlVStime.pdf',
    fig1.savefig('AnzahlVStime.pdf',
                 format='pdf', orientation='landscape', pad_inches=0)
else:
    sys.exit("invalid language")
#fig1.show()



fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
ax2.plot(AnzahlKonst['Nachrichtenlaenge'], AnzahlKonst['ZeitAES'], color='k', marker='o', markersize=0.5,
         linewidth = 0.1, label=str('AES-256'))
ax2.plot(AnzahlKonst['Nachrichtenlaenge'], AnzahlKonst['ZeitOTP'], color='0.7', marker='s', markersize=0.5,
         linewidth = 0.1, label=str('SIKAF (OTP)'))



if lang_plot == 'eng':
    ax2.set_xlabel('message length [byte]')
    ax2.set_ylabel('time [ms]')
    ax2.set_title(str('Constant Number of Encryptions n=' + str(my_parameters.AnzahlVerschluesselungen_iter)))
    ax2.set_ylim(ymin=0, ymax=cr_ylim)
    ax2.set_xlim(xmin=0)
    plt.legend()
    plt.grid(color='0.7', linestyle='dotted', linewidth=0.5)
    # fig2.savefig('C:/Users/blue/Documents/Forschungsprojekt-FUH/Ausarbeitung/Abbildungen/plots/LengthVStime_english.svg',
    fig2.savefig('LengthVStime_english.svg',
                 format='svg', orientation='landscape', pad_inches=0, dpi=1200)

elif lang_plot == 'ger':
    ax2.set_xlabel('Nachrichtenlänge [Byte]')
    ax2.set_ylabel('Zeit [ms]')
    ax2.set_title(str('Anzahl Maskierungen konstant bei n=' + str(my_parameters.AnzahlVerschluesselungen_iter)))
    ax2.set_ylim(ymin=0, ymax=cr_ylim)
    ax2.set_xlim(xmin=0)
    plt.legend()
    plt.grid(color='0.7', linestyle='dotted', linewidth=0.5)
    # fig2.savefig('C:/Users/blue/Documents/Forschungsprojekt-FUH/Ausarbeitung/Abbildungen/plots/LengthVStime.pdf',
    fig2.savefig('LengthVStime.pdf',
                 format='pdf', orientation='landscape', pad_inches=0)
else:
    sys.exit("invalid language")

#fig2.show()

fig3 = plt.figure(3)

ax3 = fig3.add_subplot(121, projection='3d')

X = df['Nachrichtenlaenge'].to_numpy()
Y = df['AnzahlVerschluesselungen'].to_numpy()
Z = df['ZeitOTP'].to_numpy()

ax3.scatter(X, Y, Z, c='b', marker='o')

ax3.set_xlabel('Nachrichtenlänge')
ax3.set_ylabel('Anzahl Verschlüsselungen')
ax3.set_zlabel('Benötigte Zeit')
plt.legend(title='One Time Pad')

ax4 = fig3.add_subplot(122, projection='3d')

X = df['Nachrichtenlaenge'].to_numpy()
Y = df['AnzahlVerschluesselungen'].to_numpy()
Z = df['ZeitAES'].to_numpy()

ax4.scatter(X, Y, Z, c='b', marker='o')

ax4.set_xlabel('Nachrichtenlänge')
ax4.set_ylabel('Anzahl Verschlüsselungen')
ax4.set_zlabel('Benötigte Zeit')
plt.legend(title='AES-256')
plt.tight_layout()

# fig3.savefig('C:/Users/blue/Documents/Forschungsprojekt-FUH/Ausarbeitung/Abbildungen/plots/threedee')
fig3.savefig('threedee')
#fig3.show()


# plt.show()
