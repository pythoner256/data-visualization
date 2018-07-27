import json
import pygal
import requests


response = requests.get('https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json')  # 发送请求

with open("交易收盘数据.json", 'w') as f:  # 将返回的数据写入到本地
     f.write(response.text)


"""绘制折线图；准备数据"""
dates = []
months = []
weeks = []
weekdays = []
closes = []

filename = "交易收盘数据.json"
with open(filename) as f:
    datas = json.load(f)

for data_dict in datas:
    dates.append(data_dict["date"])
    months.append(int(data_dict["month"]))
    weeks.append(int(data_dict["week"]))
    weekdays.append(data_dict["weekday"])
    closes.append(int(float(data_dict["close"])))

"""开始绘制"""

l_chart = pygal.Line(x_label_rotation=45, show_minor_x_labels=False)  # X轴顺时针旋转20度；设置不用显示所有的X标签
l_chart.title = "收盘价(￥)"  # 图表标题
l_chart.x_labels = dates
N = 20
l_chart.x_labels_major = dates[::N]  # 每隔20天显示一次
l_chart.add("收盘价", closes)
l_chart.render_to_file("收盘价折线图(￥).svg")  # 存到本地文件中

