import json


filename = "交易收盘数据.json"
with open(filename) as f:
    datas = json.load(f)

for data_dict in datas:
    """json值都是字符串，对应的转成整型"""
    date = data_dict["date"]  # 日期
    month = int(data_dict["month"])  # 月份
    week = int(data_dict["week"])  # 第几周
    weekday = data_dict["weekday"]  # 星期几
    close = int(float(data_dict["close"]))  # 收盘价

