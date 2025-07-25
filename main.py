import pygame
import random

# classes
class Game():
    def __init__(self):
        self.score = 0
        self.round = 1
        self.lives = 5

        self.my_font = pygame.font.Font('game_font.ttf', 32)

    def update(self):
        self.make_hud()

    def make_hud(self):
        round_text = self.my_font.render(f"ROUND: {self.round}", True, 'white')
        round_rect = round_text.get_rect(topleft=(20, 10))
        score_text = self.my_font.render(f"SCORE: {self.score}", True, 'white')
        score_rect = score_text.get_rect(midtop=(WINDOW_WIDTH//2, 10))       
        lives_text = self.my_font.render(f"SCORE: {self.lives}", True, 'white')
        lives_rect = lives_text.get_rect(topright=(WINDOW_WIDTH-20, 10))       
        display_surface.blit(round_text, round_rect)
        display_surface.blit(score_text, score_rect)        
        display_surface.blit(lives_text, lives_rect)

        pygame.draw.line(display_surface, 'white', (0, GAME_WINDOW_UP), (WINDOW_WIDTH, GAME_WINDOW_UP),width=2)
        pygame.draw.line(display_surface, 'white', (0, GAME_WINDOW_DOWN), (WINDOW_WIDTH, GAME_WINDOW_DOWN), width=2)












# initialize pygame
pygame.init()

# set a display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
GAME_WINDOW_UP = 40
GAME_WINDOW_DOWN = WINDOW_HEIGHT - 100

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Invaders')


# set FPS and the clock
FPS = 60
clock = pygame.time.Clock()

my_game = Game()

# main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # fill the background
    display_surface.fill('black')


    # update hud
    my_game.update()


    # update the display
    pygame.display.update()





    # tick the clock
    clock.tick(FPS)

# end the game
pygame.quit()


