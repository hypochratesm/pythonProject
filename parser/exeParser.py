import pandas as pd

df_sheet_index = pd.read_excel('C:/Users/qraft/Documents/메타 코드(값) 리스트_20170927.xlsx' , sheet_name='BANK LIST')


#print(df_sheet_index)

for idx in range(len(df_sheet_index)):
    print(tuple(df_sheet_index.values[idx]))

