import pygame
import sys

# 初始化pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 设置棋盘的大小和格子的数量
BOARD_SIZE = (256, 256)
GRID_COUNT = 19

# 计算每个格子的大小
GRID_SIZE = BOARD_SIZE[0] // (GRID_COUNT + 1)

# 定义星位的位置
star_points = [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15), (15, 3), (15, 9), (15, 15)]

class GoGame:
    def __init__(self):
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        pygame.display.set_caption("围棋")
        self.board = [[None for _ in range(GRID_COUNT)] for _ in range(GRID_COUNT)]
        self.turn = 'black'  # 让黑子先行

    def draw_board(self):
        """绘制棋盘"""
        font = pygame.font.Font(None, 12)
        for i in range(GRID_COUNT):
            label = font.render(chr(ord('a') + i), True, BLACK)
            self.screen.blit(label, (i * GRID_SIZE + GRID_SIZE, 0))
            self.screen.blit(label, (0, i * GRID_SIZE + GRID_SIZE))

        for x in range(GRID_COUNT):
            for y in range(GRID_COUNT):
                pos = (x * GRID_SIZE + GRID_SIZE, y * GRID_SIZE + GRID_SIZE)
                pygame.draw.line(self.screen, BLACK, (GRID_SIZE, y * GRID_SIZE + GRID_SIZE), (BOARD_SIZE[0] - GRID_SIZE, y * GRID_SIZE + GRID_SIZE), 1)
                pygame.draw.line(self.screen, BLACK, (x * GRID_SIZE + GRID_SIZE, GRID_SIZE), (x * GRID_SIZE + GRID_SIZE, BOARD_SIZE[1] - GRID_SIZE), 1)
                
                if (x, y) in star_points:
                    pygame.draw.circle(self.screen, BLACK, pos, 2)
                
                if self.board[x][y] == 'black':
                    pygame.draw.circle(self.screen, BLACK, pos, GRID_SIZE // 2 - 2)
                elif self.board[x][y] == 'white':
                    pygame.draw.circle(self.screen, BLACK, pos, GRID_SIZE // 2)
                    pygame.draw.circle(self.screen, WHITE, pos, GRID_SIZE // 2 - 2)

    def step(self, action, color):
        x, y = action
        if 0 <= x < GRID_COUNT and 0 <= y < GRID_COUNT and self.board[x][y] is None:
            self.board[x][y] = color
            self.turn = 'white' if self.turn == 'black' else 'black'  # 切换回合

        # 渲染
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill(WHITE)
        self.draw_board()
        pygame.display.flip()

        # 获取游戏画面的数组表示
        game_state = pygame.surfarray.array3d(pygame.display.get_surface())
        
        return game_state
# if __name__ == "__main__":
#     game = GoGame()
#     while True:
#         game.step((8, 8), 'black')
#         game.step((9, 9), 'white')
