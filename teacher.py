import pygame
import random

# classes
class Game():
    ''' a class to help control and update display'''

    def __init__(self, alien_group):
        ''' initialize the game'''
        self.alien_group = alien_group

    def update(self):
        ''' update the game'''

        pass

    def draw(self):
        ''' draw the hud and other information to display'''
        pass

    def shift_aliens(self):
        ''' shift a wave of aliens down the screen and reverse direction'''
        pass

    def check_collisions(self):
        ''' check for collisions'''
        pass

    def check_round_completion(self):
        ''' check to see if a player has completed a single round'''
        pass

    def start_new_round(self):
        ''' start a new round'''
        pass

    def check_game_status(self):
        ''' check to see the status of the game and how the player dies'''
        pass

    def pause_game(self):
        ''' pauses the game'''
        pass

    def reset_game(self):
        ''' reset the game'''
        pass

class Player(pygame.sprite.Sprite):
    ''' a class to model a spaceship the user can control '''
    def __init__(self, bullet_group, group):
        ''' initialize the player'''

        super().__init__(group)
        self.bullet_group = bullet_group
        self.image = pygame.image.load('spaceship64.png')
        self.rect = self.image.get_rect(midbottom=(WINDOW_WIDTH//2, WINDOW_HEIGHT))

        self.lives = 5
        self.velocity = 8

        self.shoot_sound = pygame.mixer.Sound('laser_beam_sound.mp3')


    def update(self):
        ''' update the player'''
        keys = pygame.key.get_pressed()

        # move the player within the bounds of the screen
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x += -self.velocity

    def fire(self):
        ''' fire a bullet'''
        PlayerBullet(self.rect.center, self.rect.top, self.bullet_group)

    def reset(self):
        '''reset the players position'''
        self.rect.centerx = WINDOW_WIDTH // 2


class Alien(pygame.sprite.Sprite):
    ''' a class to model an enemy alien '''
    def __init__(self, group):
        ''' initialize the alien'''

        super().__init__(group)
        pass

    def update(self):
        ''' update the alien'''
        pass

    def fire(self):
        ''' fire a bullet'''
        pass

    def reset(self):
        '''reset the aliens position'''
        pass

class PlayerBullet(pygame.sprite.Sprite):
    ''' a class to model a bullet fired by the player'''

    def __init__(self, x, y, group):
        ''' initialize the bullet'''
        super().__init__(group)
        self.bullet_group = group
        self.image = pygame.image.load('green_laser.png')
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.velocity = 5

    def update(self):
        ''' update the bullet'''
        self.rect.y -= self.velocity
        if self.rect.top < 0:
            self.kill()


class AlienBullet(pygame.sprite.Sprite):
    ''' a class to model a bullet fired by the alien'''

    def __init__(self, group):
        ''' initialize the bullet'''
        pass

    def update(self):
        ''' update the bullet'''
        pass  






# initialize pygame
pygame.init()

# set a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Invaders')


# set FPS and the clock
FPS = 60
clock = pygame.time.Clock()

# create bullet groups
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()

# create a player group and a player object
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group, my_player_group)

# create an alien group. will add alien objects via the game's start new round method
my_alien_group = pygame.sprite.Group()

# create a game object
my_game = Game(my_alien_group)


# main game loop
running = True
while running:
    # check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # fill the background
    display_surface.fill('black')

    # update and display all sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_alien_group.update()
    my_alien_group.draw(display_surface)

    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)

    # update and draw Game object
    my_game.update()
    my_game.draw()




    # update the display
    pygame.display.update()

    # tick the clock
    clock.tick(FPS)

# end the game
pygame.quit()


