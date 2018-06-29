import pygal

from random import randint


class Tou:
    def __init__(self, side_num=6):
        self.side_num = side_num

    def roll(self):
        return randint(1, self.side_num)  # 随机返回骰子掷出的点数


die = Tou()
die2 = Tou(10)  # 创建一个10面的骰子

fre = []  # 保存骰子的点数之和

for i in range(500):
    result = die.roll()+die2.roll()  # 掷两次骰子，计算他们的和
    fre.append(result)

count_num = []  # 保存点数之和出现的次数

for num in range(2, die.side_num+die2.side_num+1):
    number = fre.count(num)
    count_num.append(number)


"""图表展示"""
hist = pygal.Bar()
hist.title = 'Result of rolling D10 and D6 500 times'
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

hist.add('D6+D10', count_num)
hist.render_to_file('D6+D10_analysis.svg')  # 保存文件

