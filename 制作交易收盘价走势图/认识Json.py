import requests

response = requests.get('https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json')  # 发送请求

with open("交易收盘数据.json", 'w') as f:  # 将返回的数据写入到本地
    f.write(response.text)

file = response.json()  # 转换成Python列表格式

"""
[{
    "date": "2017-01-01",
    "month": "01",
    "week": "52",
    "weekday": "Sunday",
    "close": "6928.6492"
},
{
    "date": "2017-01-02",
    "month": "01",
    "week": "1",
    "weekday": "Monday",
    "close": "7070.2554"
},........
"""