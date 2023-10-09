from GO import GoGame

game = GoGame()  # 注意这里我们创建了GoGame的一个实例

while True:
    state = game.step((8, 8), 'black')
    print(state)

   
