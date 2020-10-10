import sys
import os
print(sys.version)
import pandas as pd

df = pd.read_pickle("Z:/mycm_crypto/CryptEval/dummy_LengthVStime_raspi.pkl")

print(df)
