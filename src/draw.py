# coding:utf8
from utils import padding

def draw(game):
    # 渲染函数
    def _render(game, maps):
        print(game.canvas['title'])
        print(game.canvas['score'])
        for i in range(len(maps)):
            print maps[i]
        print(game.canvas['tips'])
    

    # 生成图像
    maps = []
    maps.append(game.canvas['splitor'])
    for i in range(game.level):
        row = '|'
        for j in range (game.level):
            if game.layout[i][j] == 0:
                row += padding(' ', game.size) + '|'
            else:
                row += padding(str(game.layout[i][j]), game.size) + '|'
        maps.append(row)
        maps.append(game.canvas['splitor'])
    
    # 渲染图像
    _render(game, maps)