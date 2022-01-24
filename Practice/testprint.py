import csv
from pathlib import Path
from csv import writer
import pandas as pd

#*****************************************#

print("######################## HELLO!!############################")
f = open('final_fantasy2.csv', 'w') #gjhjkjnbjhvnbmn
writer = csv.writer(f)

df = pd.read_csv(r'./daily_rate_sheet.csv')
print (df)
file=open('qualifying_loans2.csv',"w")
file.write('mic check, 1, 2, 1, 2')
file.close()


