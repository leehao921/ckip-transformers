import sys
from collections import Counter
from pandas import ExcelWriter
import pandas as pd

tmp_data=[]
for fileName in ["中信金控", "兆豐金控", "台新金控", "台灣金融控股", "國泰金控", "第一金控", "玉山金控", "土地銀行", "富邦金控", "開發金", "新光金控"]:
    fileloc = "./_target/"+fileName+"reslut.xls"
    file = pd.read_excel(fileloc)
    tmp_data.append(file)
    print(fileName + str(len(file)))
result=pd.concat(tmp_data)
print(len(result))
print(result.head())
result.to_csv("./_target/reslut.xls")
