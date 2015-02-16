# Todo:
# - fix flicker
# - make turtle class - Rain
# - fix bounce animation - Dad
# - Have launcher only move when you click on it - Dad
# - Add rubber bands to launcher - Dad
# - Show text if you hit target - Rain
# - Show score - Rain
# - Add x axis collision point code to Ball update - Dad
# - Add sound
# - Animate turtle - Rain

# DONE
# - reset game function - Dad
# - Create launcher - Dad


import pygame
import math


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

VELOCITY = 5
FORCE_MULTIPLIER = 60

pygame.init()

# Set the width and height of the screen [width, height]
size = (333, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Paperball")
background_image = pygame.image.load("room.jpg").convert()

targetx = 169
targety = 100

change_pos = False
mouse_down = False
launch1 = [0,0]
launch2 = [0,0]

score = 0



class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()

        # Initialize some variables
        self.change = [0,0]
        self.force = [0,0]
        self.distance = [10,20]
        self.collision1 = [0,0]
        self.hit_target = False
        self.start = [168,520]


        self.bounce = False
        self.bounce2 = False
        self.bounce_pause = 0
        self.bounce_pause2 = 0
        self.bounce_length = 0
        self.bounce_length2 = 0
        self.bounce_done = False

        self.image = pygame.image.load("paper20.png").convert()
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect(center=(self.start))
        print self.rect.x
        print self.rect.y
        print self.rect.width

    def calculate_collision(self):
        # Calculate distance to 1st collision point
        self.distance[0] = FORCE_MULTIPLIER * self.force[0]
        self.distance[1] = FORCE_MULTIPLIER * self.force[1]

        # Calculate collision point
        self.collision1[0] = self.rect.x + self.distance[0]
        self.collision1[1] = self.rect.y - self.distance[1]


    def update(self):
        if change_pos == True:

            # Test if hit 1st collision point

            # print "collision1 x = ", self.collision1[0]
            # if self.rect.x >= self.collision1[0]:
            #     self.gravity[0] += GRAVITY*3

            #print "collision1 y = ", self.collision1[1]
            if self.rect.y <= self.collision1[1]:
                self.bounce = True

            # Bounce 1
            if self.bounce == True and self.bounce_done == False:
                if self.bounce_pause < 10:
                    self.bounce_pause += 1
                else:
                    self.rect.x += 2
                    self.rect.y -= 3
                    self.bounce_length += 1
                
                if self.bounce_length >= 30:
                    self.bounce = False
                    self.bounce2 = True

            # Bounce 2
            if self.bounce2 == True and self.bounce_done == False:
                if self.bounce_pause2 < 20:
                    self.bounce_pause2 += 1
                else:
                    self.rect.x += 2
                    self.rect.y -= .5
                    self.bounce_length2 += 1

                if self.bounce_length2 >= 20:
                    self.bounce_done = True

            # Change position
            if self.bounce == False and self.bounce2 == False and self.bounce_done == False:
                self.rect.x += VELOCITY * self.force[0]
                self.rect.y -= VELOCITY * self.force[1]

    def target_collision(self):
        self.center = (self.rect[0] + 28, self.rect[1] + 24)
        global score, add1
        if targetx + 17 <= (self.collision1[0] + 7) and (self.collision1[0] + 7) <= targetx + 67 and targety + 15 <= (self.collision1[1] + 4) and (self.collision1[1] + 4) <= targety + 65:
            self.hit_target = True
        elif targetx + 17 <= (self.collision1[0] + 52) and (self.collision1[0] + 52) <= targetx + 67 and targety + 15<= (self.collision1[1] + 4) and (self.collision1[1] + 4) <= targety + 65:
            self.hit_target = True
        elif targetx + 17 <= (self.collision1[0] + 7) and (self.collision1[0] + 7) <= targetx + 67 and targety + 15<= (self.collision1[1] + 48) and (self.collision1[1] + 48) <= targety + 65:
            self.hit_target = True
        elif targetx + 17 <= (self.collision1[0] + 52) and (self.collision1[0] + 52) <= targetx + 67 and targety + 15<= (self.collision1[1] + 48) and (self.collision1[1] + 48) <= targety + 65:
            self.hit_target = True

        if self.hit_target == True and add1 == True:
            score += 1
            add1 = False
            






    
    



class Launcher(pygame.sprite.Sprite):
    def __init__(self):
        super(Launcher, self).__init__()
        self.width = 60
        self.height = 15
        self.return_start = False
        self.start = [168,550]
        self.diff = [0,0]

        # Create an image of the block, and fill it with a color.
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(self.start))

    def update(self):
        if self.return_start == True:
            # Calculate distance to starting point
            self.diff[0] = (self.rect.x + self.width/2) - self.start[0]
            self.diff[1] = (self.rect.y + self.height/2) - self.start[1]

            if self.diff[0] > 6:
                self.rect.x -= 6
            elif self.diff[0] > 0:
                self.rect.x -= self.diff[0]
            elif self.diff[0] < -6:
                self.rect.x += 6
            elif self.diff[0] < 0:
                self.rect.x -= self.diff[0]

            if self.diff[1] > 6:
                self.rect.y -= 6
            elif self.diff[1] > 0:
                self.rect.y -= self.diff[1]
            



class Turtle(pygame.sprite.Sprite):

    def __init__(self):
        super(Turtle, self).__init__()
        self.start = [targetx, targety]
        self.image = pygame.image.load("turtle100.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=(self.start))
        self.changetargetx = 0
        self.changetargety = 0
        self.targetx = 0
        self.targety = 0

    def update(self):
        self.targetx += self.changetargetx
        self.targety += self.changetargety

  

paper_ball = Ball()
ball_launcher = Launcher()
turtle = Turtle()

all_sprites = pygame.sprite.Group()
all_sprites.add(turtle)
all_sprites.add(paper_ball)
all_sprites.add(ball_launcher)

font = pygame.font.SysFont('Calibri', 25, True, False)



# Loop until the user clicks the close button.
done = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def setup():
    # Initialize ball's variables
    global change_pos
    change_pos = False
    paper_ball.kill()
    paper_ball.rect.x = paper_ball.start[0]-paper_ball.rect.width/2
    paper_ball.rect.y = paper_ball.start[1]-paper_ball.rect.height/2
    paper_ball.change = [0,0]
    paper_ball.gravity = [0,0]
    paper_ball.force = [0,0]
    paper_ball.distance = [10,20]
    paper_ball.collision1 = [0,0]
    paper_ball.hit_target = False

    paper_ball.bounce = False
    paper_ball.bounce2 = False
    paper_ball.bounce_pause = 0
    paper_ball.bounce_pause2 = 0
    paper_ball.bounce_length = 0
    paper_ball.bounce_length2 = 0
    paper_ball.bounce_done = False
    ball_launcher.return_start = False

    all_sprites.add(paper_ball)



# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and change_pos == False:
                paper_ball.force[0] += 1
                print "x = " + str(paper_ball.force[0])
            if event.key == pygame.K_LEFT and change_pos == False:
                paper_ball.force[0] -= 1
                print "x = " + str(paper_ball.force[0])
            if event.key == pygame.K_UP and change_pos == False:
                paper_ball.force[1] += 1
                print "y = " + str(paper_ball.force[1])
            if event.key == pygame.K_DOWN and change_pos == False:
                paper_ball.force[1] -= 1
                print "y = " + str(paper_ball.force[1])
            if event.key == pygame.K_SPACE and change_pos == False:
                paper_ball.calculate_collision()
                change_pos = True

            # Reset game button
            if event.key == pygame.K_TAB:
                setup()
        elif event.type == pygame.MOUSEBUTTONDOWN and \
            (event.pos[0] > ball_launcher.rect.x and  \
            event.pos[0] < (ball_launcher.rect.x + ball_launcher.width)) and \
            (event.pos[1] > ball_launcher.rect.y and  \
            event.pos[1] < (ball_launcher.rect.y + ball_launcher.height)):
            print "mouse button down at (%d, %d)" % event.pos
            mouse_down = True
            if ball_launcher.return_start == True:
                setup()
            launch1[0] = event.pos[0]
            launch1[1] = event.pos[1]

        elif event.type == pygame.MOUSEBUTTONUP and mouse_down == True:
            print "mouse button up at (%d, %d)" % event.pos
            mouse_down = False
            paper_ball.force[1] += (launch2[1] - launch1[1])/14
            print "force y = ", paper_ball.force[1] 
            paper_ball.calculate_collision()
            change_pos = True
            ball_launcher.return_start = True

            add1 = True


        if event.type == pygame.MOUSEMOTION and \
            mouse_down == True and \
            event.pos[1] > 550:
            ball_launcher.rect.x = event.pos[0] - ball_launcher.width/2
            ball_launcher.rect.y = event.pos[1] - ball_launcher.height/2
            paper_ball.rect.x = event.pos[0] - ball_launcher.width/2
            paper_ball.rect.y = event.pos[1] - 55
            launch2[0] = event.pos[0]
            launch2[1] = event.pos[1]

    # --- Game logic should go here


    # --- Drawing code should go here


    screen.blit(background_image, [0, 0])


    # Call the update() method for all blocks in the block_list
    all_sprites.update()


    # Update & display ball sprite
    all_sprites.draw(screen)

    paper_ball.target_collision()

    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [0, 0])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


# Close the window and quit.
pygame.quit()
    