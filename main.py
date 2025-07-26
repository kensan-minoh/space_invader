import pygame
import random

# classes
class Game():
    def __init__(self, invader_group, spaceship_group, invader_laser_group, spaceship_laser_group):
        self.invader_group = invader_group
        self.spaceship_group = spaceship_group
        self.invader_laser_group = invader_laser_group
        self.spaceship_laser_group = spaceship_laser_group
        
        self.score = 0
        self.round = 1
        self.lives = 5

        self.spaceship_image = pygame.image.load('spaceship64.png').convert_alpha()
        self.invader_image = pygame.image.load('invader64.png').convert_alpha() 
        self.spaceship_laser_image = pygame.image.load('green_laser.png')
        self.my_font = pygame.font.Font('game_font.ttf', 32)

        self.laser_beam_sound = pygame.mixer.Sound('laser_beam_sound.mp3')
        self.laser_beam_sound.set_volume(0.1)
        self.destroy_sound = pygame.mixer.Sound('destroy_sound.wav')
        self.destroy_sound.set_volume(0.2)


        self.making_invaders()
        self.spaceship = Spaceship(self.spaceship_group)
        
        self.pausing_game("SPACE INVADER GAME", "PRESS ENTER TO BEGIN!")

    def update(self):
        self.make_hud()
        self.check_collisions()

    def pausing_game(self, main_text, sub_text):
        main_messege_text = self.my_font.render(main_text, True, 'white')
        main_message_rect = main_messege_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2-50))
        sub_messege_text = self.my_font.render(sub_text, True, 'white')
        sub_message_rect = sub_messege_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))

        display_surface.blit(main_messege_text, main_message_rect)
        display_surface.blit(sub_messege_text, sub_message_rect)

        pygame.display.update()
        is_waiting = True
        while is_waiting:

            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                is_waiting = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                is_waiting = False


    def check_collisions(self):
        for sprite in self.spaceship_laser_group.sprites():
            invader = pygame.sprite.spritecollideany(sprite, self.invader_group)
            if invader:
                self.destroy_sound.play()
                self.score += 10 * self.round
                invader.kill()
                sprite.kill()


    def making_invaders(self):
        for j in range(5):

            for i in range(11):
                Invader(self.invader_image, i*60, j*60+GAME_WINDOW_UP+10, self.invader_group)
    def making_spaceship_laser(self):
        if len(self.spaceship_laser_group) < 3:
            self.laser_beam_sound.play()
            Spaceship_laser(self.spaceship_laser_image, self.spaceship.rect.centerx, self.spaceship.rect.top,self.spaceship_laser_group)

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


class Invader(pygame.sprite.Sprite):
    def __init__(self, image, x, y, invader_group):
        super().__init__(invader_group)
        self.image = image

        self.rect = self.image.get_rect(topleft=(x,y))
        self.invader_group = invader_group
        self.velocity_x = 1
        self.direction_x = 1
        self.velocity_y = 20

    def update(self):
        self.rect.x += self.direction_x * self.velocity_x
        if self.rect.right >= WINDOW_WIDTH+10 or self.rect.left <= -10:
            for sprite in self.invader_group.sprites():

                sprite.direction_x *= -1
                sprite.rect.y += self.velocity_y

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, spaceship_group):
        super().__init__(spaceship_group)
        self.spaceship_group = spaceship_group
        self.image = pygame.image.load('spaceship64.png')
        self.rect = self.image.get_rect(midbottom=(WINDOW_WIDTH//2, WINDOW_HEIGHT-20))
        

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.rect.right <= WINDOW_WIDTH:
            self.rect.x += 3
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x += -3

class Spaceship_laser(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spaceship_laser_group):
        super().__init__(spaceship_laser_group)
        self.image = image
        self.rect = self.image.get_rect(midbottom=(x, y))


    def update(self):
        self.move()


    def move(self):
        self.rect.y += -5
        if self.rect.top <= GAME_WINDOW_UP:
            self.kill()










# initialize pygame
pygame.init()

# set a display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 650
GAME_WINDOW_UP = 40
GAME_WINDOW_DOWN = WINDOW_HEIGHT - 100

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Invaders')


# set FPS and the clock
FPS = 60
clock = pygame.time.Clock()


my_invader_group = pygame.sprite.Group()
my_spaceship_group = pygame.sprite.GroupSingle()
my_invader_laser_group = pygame.sprite.Group()
my_spaceship_laser_group = pygame.sprite.Group()

my_game = Game(my_invader_group, my_spaceship_group, my_invader_laser_group, my_spaceship_laser_group)


# main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            my_game.making_spaceship_laser()


    # fill the background
    display_surface.fill('black')


    # update hud
    my_game.update()
    my_invader_group.update()
    my_invader_group.draw(display_surface)
    my_spaceship_group.update()
    my_spaceship_group.draw(display_surface)
    my_spaceship_laser_group.update()
    my_spaceship_laser_group.draw(display_surface)


    # update the display
    pygame.display.update()





    # tick the clock
    clock.tick(FPS)

# end the game
pygame.quit()


