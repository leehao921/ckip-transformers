import json

f = open('/Users/felix/Documents/Coding/python/dictionary.json')
data = json.load(f)
f.close()

target = "分析"
print(data)
data[target] = {}
# data[target]['技術'] = []
# data[target]['優化'] = []
tmp = []
element = input('優化特徵：\n')

tmp = element.split(',')
data[target]['技術'] = tmp
print(data)
element = input('優化特徵：\n')

tmp = element.split(',')
data[target]['優化'] = tmp


arange = json.dumps(data, indent=4, ensure_ascii=False)
w = open('/Users/felix/Documents/Coding/python/dictionary.json',
         'w', encoding='utf-8')
w.write(arange)

# {
#     "服務":{
#         "技術":[],
#         "優化":[]
#     }
# }

# 商業方法,瀏覽,介面,網路,服務,客服,交易,支付,登入,自然人,行動,線上,個人化,實體,虛擬,感應,藍芽,網頁,應用程式}
#         {方便,簡易,快速,通知,建議,直覺化,}
# “管理”:{資料庫,系統,數據,安全,自動化,管理,控管,區塊鏈,整合,平台,排程,維護,資料,交換,架設,設計,設備,電子}
#         {結果,優化,效能,安全性,效率,隱密性,整合}
# “分析”:{處理,演算法,行銷,評估,風險,分析,機器,學習,智慧,調變,保險,處理,運用,辨識,計算}
#         {精準,效益,個人化}
