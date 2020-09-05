from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd


df = pd.read_pickle("dummy_AnzahlVStime.pkl")

print(df)

LaengeKonst = df[df["Nachrichtenlaenge"] == 1499]
AnzahlKonst = df[df["AnzahlVerschluesselungen"] == 499]

print(AnzahlKonst)


fig = plt.figure()

ax2 = fig.add_subplot(111)

ax2.plot(AnzahlKonst['Nachrichtenlaenge'], LaengeKonst['ZeitAES'], color='g', marker='o', markersize=2, label=str('AES'))
ax2.plot(AnzahlKonst['Nachrichtenlaenge'], LaengeKonst['ZeitOTP'], color='r', marker='o', markersize=2, label=str('OTP'))

ax2.set_xlabel('Nachrichtenlänge [byte]')
ax2.set_ylabel('Zeit [ms]')
ax2.set_title('Anzahl Verschluesselungen const = 9992')
#ax1.set_ylim([0, 8])
plt.legend(title='Verfahren')

plt.show()
