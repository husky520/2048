# coding:utf8
import random
from draw import draw, padding
from getch import Getch
class Game():
    def __init__(self):
        self.level = int(raw_input('Game Level: '))

        self.init()

        # 监听输入
        getch = Getch()
        while(True):
            operate = getch().upper()
            # print(operate + '\r')
            if operate == 'E':
                break
            elif operate == 'R':
                print('\n' * 100)
                self.level = int(raw_input('Game Level: '))
                self.init()
            elif operate == 'w' or operate == 'D' or operate == 'S' or operate == 'A':
                self.step(operate)
            else:
                pass
    
    # 初始化
    def init(self):
        self.size = 5        # 格子大小 (5)
        self.score = 0       # 分数

        # 初始化空棋盘
        self.layout = [[0 for i in range(self.level)] for j in range(self.level)]
        # 放置数字
        self._set_number()

        self.canvas = {
            # 预设元素
            'title': '\n' * 100 + padding(' 2048 ', self.level * self.size + self.level + 1, '*'),
            'score': 'score: ' + str(self.score),
            'tips': '\nTips: (W)Up (D)Right (S)Down (A)Left (R)Restart (E)Exit',
            'splitor': '+-----' * self.level + '+'
        }

        # 渲染图像
        draw(self)

    # 操作
    def step(self, direction):
        if   direction == 'W':
            pass
        elif direction == 'D':
            pass
        elif direction == 'S':
            pass
        elif direction == 'A':
            pass

    
    # 退出
    def exit(self):
        pass
    
    def _set_number(self):
        new_num = random.choice([2, 2, 4])
        # 这里需要优化：抽出所有为0的格子坐标，从该数组中选择
        while(True):
            x = random.randint(0, self.level - 1)
            y = random.randint(0, self.level - 1)
            if self.layout[y][x] == 0:
                self.layout[y][x] = new_num
                break
