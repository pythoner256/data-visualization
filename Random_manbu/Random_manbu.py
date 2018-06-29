# 创建类，首先初始化x,y的坐标，并且漫步次数默认设置为5000次
# 创建一个循环，这个循环控制着漫步的长度和方向，当x走的次数等于5000的时候就停下来
# 规定一个反向，这个方向使用choice随机取，要么正，要么反方向
# 规定一个长度，同样用choice随机取值
# x,y的走向都遵循上面的规律
# 当他两取得0的时候跳过继续执行循环
# 计算下一个x,y的值
# 把下一个x,y的值添加到他们对应的列表中

import matplotlib.pyplot as plt

from random import choice


class Walk:
    def __init__(self, initial_count=5000):  # 设置掷骰子次数为5000次
        self.initial_count = initial_count
        self.xcoor = [0]  # 初始化x,y的坐标在原点
        self.ycoor = [0]

    def all_point(self):  # 获取所有的点
        while len(self.xcoor) < self.initial_count:
            x_dir = choice([-1, 1])  # 让x随机选择一个方向，要么正方形要么反方向
            x_stp = choice([0, 1, 2, 3, 4])  # 让x随机走多少步
            x_len = x_stp * x_dir  # 计算x走的长度

            y_dir = choice([-1, 1])
            y_stp = choice([0, 1, 2, 3, 4])
            y_len = y_stp * y_dir

            if x_len == 0 and y_len == 0:
                continue

            next_x = self.xcoor[-1] + x_len
            next_y = self.ycoor[-1] + y_len

            self.xcoor.append(next_x)
            self.ycoor.append(next_y)


point = Walk()
point.all_point()

"""给点设置不同的颜色"""
point_number = list(range(point.initial_count))
plt.scatter(point.xcoor, point.ycoor, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=15)

"""重新绘制起点和终点,让他们显示不同颜色"""
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(point.xcoor[-1], point.ycoor[-1], c='red', edgecolors='none', s=100)

"""调整尺寸适应屏幕"""
plt.figure(figsize=(10, 6))  # figure()用于指定图表的宽度，高度、分辨率和背景色；同时可指定分辨率dpi
plt.show()

