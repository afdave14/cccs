import pygame, sys, random, math
pygame.init()
random.seed()

#CONSTANTS
SCORE_HEIGHT = 60
WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)
SIZE = (WIDTH, HEIGHT)

surface = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Simple Breakout Game")
sys.stdout = file("stdout.txt", "w")
sys.stderr = file("stderr.txt", "w")

violet = pygame.Color("violet")
red = pygame.Color("red")
blue = (0, 128, 255)
yellow = pygame.Color("yellow")
green = pygame.Color("green")
white = pygame.Color("white")
paddle_border = (0,100,100)

#change number of lives
lives = 3
score = 0
level = 1

highscore = []

try:
    highscore_strings = file("highscore.txt","r").readlines()
    for s in highscore_strings:
        highscore.append(int(s))
except:
    highscore = [0,0,0]
    
#sound
click = pygame.mixer.Sound("blip.wav")

#display score and lives
Top_bar = pygame.Rect(0, 30, WIDTH, 2)

#paddle
paddle = {}
paddle["rect"]= pygame.Rect((WIDTH-100)/2, HEIGHT-20, 100, 20)
paddle["speed"] = [0, 0]

#ball
ball = {}
radius = 10
ball["rect"] = pygame.Rect(WIDTH/2 - radius, HEIGHT - 30, radius*2, radius*2) 
ball["alive"] = False
xpos = WIDTH/2
ypos = HEIGHT - 30

#change ball speed
ball["speed"] = 3.0
ball["rect"].bottom = paddle["rect"].top
ball["angle"] = 0
ball["true_x"] = ball["rect"].x + float(ball["rect"].w)/2
ball["true_y"] = ball["rect"].y + float(ball["rect"].h)/2

#list for bricks
wall = []
brick_w = 63
brick_h = 20
line = 2

for i in range(10):
    for j in range(3):
        wall.append(pygame.Rect((brick_w + line)*i, SCORE_HEIGHT +( brick_h + line)*j, brick_w, brick_h))
 
collides = False
running = True

fnt = pygame.font.Font(None, 36)
def titleScreen(gameover=False):

    pressSpace = fnt.render("Press Space key to start", False, green)
    g_over = fnt.render("Game Over", False, red)

    welcome = fnt.render("Welcome to Breakout Game", False, green)
    welcomeRect = welcome.get_rect()
    welcomeRect.left = (WIDTH - welcomeRect.w)/2
    welcomeRect.top = HEIGHT * 0.3
    
    g_overRect= g_over.get_rect()
    g_overRect.left = (WIDTH - g_overRect.w)/2
    g_overRect.top = HEIGHT * 0.3
    
    pressRect = pressSpace.get_rect()
    pressRect.left= (WIDTH - pressRect.w) / 2 
    pressRect.top = HEIGHT * 0.75

    topscore1 = fnt.render("High Score 1:   "+ str(highscore[0]), False, white)
    topscore2 = fnt.render("High Score 2:   "+ str(highscore[1]), False, white)
    topscore3 = fnt.render("High Score 3:   "+ str(highscore[2]), False, white)

    topscore1Rect = topscore1.get_rect()
    topscore1Rect.centerx = WIDTH / 2
    topscore1Rect.centery = HEIGHT/2 - topscore1Rect.h*1.5

    topscore2Rect = topscore2.get_rect()
    topscore2Rect.centerx = WIDTH / 2
    topscore2Rect.centery = HEIGHT/2
    
    topscore3Rect = topscore3.get_rect()
    topscore3Rect.centerx = WIDTH / 2
    topscore3Rect.centery = HEIGHT/2 + topscore1Rect.h*1.5
    
    waiting = 0    

    while waiting == 0:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = 1
                
            elif event.type == pygame.KEYDOWN:
                keypress = pygame.key.get_pressed()
                if keypress[pygame.K_SPACE]:
                    waiting = 2
                    
        surface.fill(BLACK)
        if level % 4 == 1:
            brick_color = blue
            paddle_color = blue
        if level % 4 == 2:
            brick_color = yellow
            paddle_color = yellow
        if level % 4 == 3:
            brick_color = green
            paddle_color = green
        if level % 4 == 0:
            brick_color = violet
            paddle_color = violet
        for i in wall:
            pygame.draw.rect(surface, brick_color, i)
        surface.blit(pressSpace, pressRect)
       
        if gameover:
            surface.blit(g_over, g_overRect)
            score_line= fnt.render("Score: " + str(score), False, white)
            score_rect = score_line.get_rect()
            score_rect.top = (30 - score_rect.h )/ 2
            score_rect.left = 10

            level_line= fnt.render("Level: " + str(level), False, white)
            level_rect = level_line.get_rect()
            level_rect.top = (30 - level_rect.h )/ 2
            level_rect.centerx = WIDTH/2    


            lives_line= fnt.render("Lives: " + str(lives), False, white)
            lives_rect = lives_line.get_rect()
            lives_rect.top = (30 - lives_rect.h )/ 2
            lives_rect.right = WIDTH - 10

            surface.blit(score_line, score_rect)
            surface.blit(lives_line, lives_rect)
            surface.blit(level_line, level_rect)
        else:
            surface.blit(welcome, welcomeRect)

        #Draw the topbar            
        pygame.draw.rect(surface, red, Top_bar)
        
        surface.blit(topscore1, topscore1Rect)
        surface.blit(topscore2, topscore2Rect)
        surface.blit(topscore3, topscore3Rect)

        pygame.display.flip()
        
        clock.tick(60)    
          
    if waiting == 1:
        return False
    if waiting == 2:
        return True
    
clock = pygame.time.Clock()

if titleScreen():
    
    while running:
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.event.pump()
           
        keypress = pygame.key.get_pressed()
        mousepos = pygame.mouse.get_pos()
        paddle["rect"].centerx = mousepos[0]
        if paddle["rect"].left < 0:
            paddle["rect"].left = 0
        if paddle["rect"].right > WIDTH:
            paddle["rect"].right = WIDTH        
        
        if keypress[pygame.K_SPACE]:
            if ball["angle"] == 0:
                ball["angle"] = math.pi/4
                    
        surface.fill(BLACK)        
       
        # move ball with paddle 
        if ball["angle"] == 0:
            ball["true_x"] = paddle["rect"].centerx
            ball["rect"].centerx = paddle["rect"].centerx
           
        block_hit_this_frame = False
        
        # change y
        delta_y = math.sin(ball["angle"])*ball["speed"]
        ball["true_y"] -= delta_y
        ball["rect"].centery = ball["true_y"]
        
        #check for bricks 
        brick_hit = ball["rect"].collidelist(wall)
        if brick_hit != -1:
            block_hit_this_frame = True
            ball["true_y"] += delta_y
            ball["rect"].centery = ball["true_y"]
            ball["angle"]-= 2*(ball["angle"] - math.pi)
            
            wall.pop(brick_hit)
            click.play()
            score = score + level*3
                    
        if ball["rect"].top < Top_bar.bottom:
            ball["true_y"] += delta_y
            ball["rect"].centery = ball["true_y"]
            ball["angle"]-= 2*(ball["angle"] - math.pi)

        if wall == []:
            for i in range(10):
                for j in range(3):
                    wall.append(pygame.Rect((brick_w + line)*i, SCORE_HEIGHT +( brick_h + line)*j, brick_w, brick_h))
            ball["rect"] = pygame.Rect(WIDTH/2 - radius, HEIGHT - 30, radius*2, radius*2)        
            paddle["rect"] = pygame.Rect((WIDTH-100)/2, HEIGHT-20, 100, 20)
            ball["rect"].bottom = paddle["rect"].top
            ball["true_y"] = ball["rect"].centery
            ball["speed"] *= 1.5
            level += 1
            ball["angle"] = 0.0

        #check for paddle
        paddle_hits_this_frame = False
        if ball["rect"].colliderect(paddle["rect"]):
            paddle_hits_this_frame = True
            if ball["angle"]> math.pi:
                ball["angle"]-= 2*(ball["angle"] - math.pi)

                #fix angle if needed
                while ball["angle"] < 0:
                    ball["angle"] += math.pi*2
                while ball["angle"] >= math.pi*2:
                    ball["angle"] -= math.pi*2
            
                paddlepos = ball["rect"].centerx - paddle["rect"].centerx

                if paddlepos < -20:
                    if ball["angle"] < math.pi*5/6:
                        ball["angle"]+=math.pi/12
                        if ( math.pi/2 - 0.1) < ball["angle"] < ( math.pi/2 + 0.1):
                            ball["angle"]+=math.pi/12
                        
                elif paddlepos > 20:
                    if ball["angle"] > math.pi/6:
                        ball["angle"] -= math.pi/12
                        if ( math.pi/2 - 0.1) < ball["angle"] < ( math.pi/2 + 0.1):
                            ball["angle"]-=math.pi/12
          
                click.play()
               
        # change x
        delta_x = math.cos(ball["angle"])*ball["speed"]
        ball["true_x"] += delta_x
        ball["rect"].centerx = ball["true_x"]

        # check for the wall
        if ball["rect"].left < 0:
            ball["true_x"] -= delta_x
            ball["rect"].centerx = ball["true_x"]
            ball["angle"] -= 2*(ball["angle"]-math.pi/2)
                   
        if ball["rect"].right > WIDTH:
            ball["true_x"] -= delta_x
            ball["rect"].centerx = ball["true_x"]
            ball["angle"] -= 2*(ball["angle"]-math.pi/2)
            
        #check for the side of paddle
        if ball["rect"].colliderect(paddle["rect"]) \
           and not paddle_hits_this_frame:            
            if ball["rect"].left < paddle["rect"].right:
                ball["true_x"] -= delta_x
                ball["rect"].centerx = ball["true_x"]
                if math.pi/2 < ball["angle"] < 3*math.pi/2:
                    ball["angle"] -= 2*(ball["angle"]-math.pi/2)
                           
            elif ball["rect"].right > paddle["rect"].left:
                ball["true_x"] -= delta_x
                ball["rect"].centerx = ball["true_x"]
                if not math.pi/2 < ball["angle"] < 3*math.pi/2:
                    ball["angle"] -= 2*(ball["angle"]-math.pi/2)

        brick_hit = ball["rect"].collidelist(wall)

        #check for bricks
        if brick_hit != -1:
            if not block_hit_this_frame:
                ball["true_x"] -= delta_x
                ball["rect"].centerx = ball["true_x"]
                ball["angle"] -= 2*(ball["angle"]-math.pi/2)            
                wall.pop(brick_hit)
                click.play()
                score = score + level*3

        #fix angle if needed
        while ball["angle"] < 0:
            ball["angle"] += math.pi*2
        while ball["angle"] >= math.pi*2:
            ball["angle"] -= math.pi*2            
                                  
        if ball["rect"].bottom > HEIGHT + radius*2:
            lives = lives - 1
            if lives == 0:
                if score > highscore[2]:
                    highscore.append(score)
                    highscore.sort(reverse=True)
                    highscore_str = ""
                    for x in range(3):
                        highscore_str += str(highscore[x]) + "\n"
                    file("highscore.txt", 'w').write(highscore_str)  
                if titleScreen(True):
                    ball["speed"] = 3.0
                    lives = 3
                    score = 0
                    level = 1
                    wall = []
                    for i in range(10):
                        for j in range(3):
                            wall.append(pygame.Rect((brick_w + line)*i, SCORE_HEIGHT +( brick_h + line)*j, brick_w, brick_h))
                else:
                    running = False
            ball["rect"] = pygame.Rect(WIDTH/2 - radius, HEIGHT - 30, radius*2, radius*2)        
            paddle["rect"] = pygame.Rect((WIDTH-100)/2, HEIGHT-20, 100, 20)
            ball["rect"].bottom = paddle["rect"].top 
            ball["angle"] = 0.0
            ball["true_x"] = ball["rect"].centerx
            ball["true_y"] = ball["rect"].centery
            
        if level % 4 == 1:
            brick_color = blue
            paddle_color = blue
        if level % 4 == 2:
            brick_color = yellow
            paddle_color = yellow
        if level % 4 == 3:
            brick_color = green
            paddle_color = green
        if level % 4 == 0:
            brick_color = violet
            paddle_color = violet

        for i in wall:
            pygame.draw.rect(surface, brick_color, i)

        score_line= fnt.render("Score: " + str(score), False, white)
        score_rect = score_line.get_rect()
        score_rect.top = (30 - score_rect.h )/ 2
        score_rect.left = 10    

        level_line= fnt.render("Level: " + str(level), False, white)
        level_rect = level_line.get_rect()
        level_rect.top = (30 - level_rect.h )/ 2
        level_rect.centerx = WIDTH/2    

        lives_line= fnt.render("Lives: " + str(lives), False, white)
        lives_rect = lives_line.get_rect()
        lives_rect.top = (30 - lives_rect.h )/ 2
        lives_rect.right = WIDTH - 10
        
        surface.blit(score_line, score_rect)
        surface.blit(lives_line, lives_rect)
        surface.blit(level_line, level_rect)
        
        pygame.draw.circle(surface, red, ball["rect"].center, 10)
        pygame.draw.rect(surface, paddle_color, paddle["rect"])
        pygame.draw.rect(surface, paddle_border, paddle["rect"], 4)
        pygame.draw.rect(surface, red, Top_bar)

        pygame.display.flip()
        clock.tick(60)    

pygame.quit()
