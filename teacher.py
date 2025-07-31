import pygame
import random

# classes
class Game():
    ''' a class to help control and update display'''

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        ''' initialize the game'''
        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_image = pygame.image.load('invader64.png')
        self.alien_bullet_group = alien_bullet_group

        # set game values
        self.round_number = 1
        self.score = 0

        #self.velocity = 5

        # set sounds and music
        self.new_round_sound = pygame.mixer.Sound('new_round_sound.mp3')
        self.breach_sound = pygame.mixer.Sound('reach_ground.wav')
        self.alien_hit_sound = pygame.mixer.Sound('destroy_sound.wav')
        self.player_hit_sound = pygame.mixer.Sound('loose_life_sound.mp3')

        # set font
        self.font = pygame.font.Font('game_font.ttf', 32)


        #self.start_new_round()

    def update(self):
        ''' update the game'''
        self.shift_aliens()
        self.check_collisions()
        self.check_round_completion()
        # self.check_game_status()
        # self.draw()
    

    def draw(self):
        ''' draw the hud and other information to display'''
        # set text
        round_text = self.font.render(f"ROUND: {self.round_number}", True, 'white')
        round_rect = round_text.get_rect(topleft=(20, 10))
        score_text = self.font.render(f"SCORE: {self.score}", True, 'white')
        score_rect = score_text.get_rect(midtop=(WINDOW_WIDTH//2, 10))       
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, 'white')
        lives_rect = lives_text.get_rect(topright=(WINDOW_WIDTH-20, 10))       
        display_surface.blit(round_text, round_rect)
        display_surface.blit(score_text, score_rect)        
        display_surface.blit(lives_text, lives_rect)

        pygame.draw.line(display_surface, 'white', (0, 50), (WINDOW_WIDTH, 50),width=4)
        pygame.draw.line(display_surface, 'white', (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), width=4)
 
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
        # create a grid of Aliens 11 columns and 5 rows
        for j in range(5):
            for i in range(11):
                x_cor = 64 * i + 64
                y_cor = 64 * j + 64
                Alien(self.alien_image, x_cor, y_cor, self.round_number, self.alien_bullet_group, self.alien_group)

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
        # restric the number of the bullets on the screen at a time
        if len(self.bullet_group) < 2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)

    def reset(self):
        '''reset the players position'''
        self.rect.centerx = WINDOW_WIDTH // 2


class Alien(pygame.sprite.Sprite):
    ''' a class to model an enemy alien '''
    def __init__(self, image, x, y, velocity, bullet_group, group):
        ''' initialize the alien'''

        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = velocity
        self.bullet_group = bullet_group
        self.alien_group = group
        self.starting_x = x
        self.starting_y = y
        self.direction = 1

        self.shoot_sound = pygame.mixer.Sound('invader_laser_sound.mp3')

    def update(self):
        ''' update the alien'''
        self.rect.x += self.velocity * self.direction

        # randomly fire a bullet
        if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()

    def fire(self):
        ''' fire a bullet'''
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)
        

    def reset(self):
        '''reset the aliens position'''
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1

class PlayerBullet(pygame.sprite.Sprite):
    ''' a class to model a bullet fired by the player'''

    def __init__(self, x, y, group):
        ''' initialize the bullet'''
        super().__init__(group)
        self.bullet_group = group
        self.image = pygame.image.load('green_laser.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 10

    def update(self):
        ''' update the bullet'''
        self.rect.y -= self.velocity

        # if the bullet is off the screen, kill it
        if self.rect.bottom < 0:
            self.kill()


class AlienBullet(pygame.sprite.Sprite):
    ''' a class to model a bullet fired by the alien'''

    def __init__(self, x, y, group):
        ''' initialize the bullet'''
        super().__init__(group)
        self.bullet_group = group
        self.image = pygame.image.load('red_laser.png')
        self.rect = self.image.get_rect(center=(x,y))

        self.velocity = 10

    def update(self):
        ''' update the bullet'''
        self.rect.y += self.velocity
        
        # if the bullet is off the screen, kill it
        if self.rect.y > WINDOW_HEIGHT:
            self.kill()







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
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
my_game.start_new_round()

# main game loop
running = True
while running:
    
    for event in pygame.event.get():
        # check to see if the user wants to quit
        if event.type == pygame.QUIT:
            running = False
        # player wants to fire
        if event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
            my_player.fire()

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


