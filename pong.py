import pygame

#make a window 800*600
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong")

left_score = 0
right_score = 0

init = False

bg_color = (0,0,0)

running = True

clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(bg_color)
 
    if not running:
        pygame.time.wait(3000)
        break
   
    #ball movement
    if not init:
        ball_x = 400
        ball_y = 300
        ball_x_change = 9
        ball_y_change = 0
        
        left_paddle_y = 275
        right_paddle_y = 275

        init = True

    ball_x += ball_x_change
    ball_y += ball_y_change

    #draw the ball
    pygame.draw.circle(screen, (255,255,255), (ball_x, ball_y), 10)

    #draw the left paddle
    pygame.draw.rect(screen, (255,255,255), (0,left_paddle_y,10,50))

    #draw the right paddle
    pygame.draw.rect(screen, (255,255,255), (790,right_paddle_y,10,50))

    #draw the left score
    font = pygame.font.SysFont(None, 72)
    text_left_score = font.render(str(left_score), True, (255,255,255))
    screen.blit(text_left_score, (187,50))

    #draw the right score
    text_right_score = font.render(str(right_score), True, (255,255,255))
    screen.blit(text_right_score, (587,50))

    keys = pygame.key.get_pressed()

    #right paddle movement
    if keys[pygame.K_UP]:
        if right_paddle_y > 0:
            right_paddle_y -= 12
    if keys[pygame.K_DOWN]:
        if right_paddle_y < 550:
            right_paddle_y += 12

    #left paddle movement
    if keys[pygame.K_w]:
        if left_paddle_y > 0:
            left_paddle_y -= 9
    if keys[pygame.K_s]:
        if left_paddle_y < 550:
            left_paddle_y += 9

    #ball collision with left paddle
    if ball_x <= 10 and ball_x >= 0:
        if ball_y >= left_paddle_y - 5 and ball_y <= left_paddle_y + 55:
            ball_x_change = -ball_x_change
            ball_x = 11
            delta_y = ball_y - left_paddle_y - 25
            ball_y_change = int(delta_y / 5)

    #ball collision with right paddle
    if ball_x >= 790 and ball_x <= 800:
        if ball_y >= right_paddle_y - 5 and ball_y <= right_paddle_y + 55:
            ball_x_change = -ball_x_change
            ball_x = 789
            delta_y = ball_y - right_paddle_y - 25
            ball_y_change = int(delta_y / 5)

    #ball collision with top and bottom
    if ball_y <= 0:
        ball_y_change = -ball_y_change
        ball_y = 1
    if ball_y >= 600:
        ball_y_change = -ball_y_change
        ball_y = 599

    #score
    if ball_x <= -50:
        right_score += 1
        ball_x = 400
        ball_y = 300
        ball_x_change = 9
        ball_y_change = 0
    if ball_x >= 850:
        left_score += 1
        ball_x = 400
        ball_y = 300
        ball_x_change = -9
        ball_y_change = 0

    #loop
    if left_score == 10:
        textWin = font.render("Left wins", True, (255,255,255))
        screen.blit(textWin, (270,275))
        text_left_score = font.render(str(10), True, (255,255,255))
        running = False
    if right_score == 10:
        textWin = font.render("Right wins", True, (255,255,255))
        screen.blit(textWin, (270,275))
        text_right_score = font.render(str(10), True, (255,255,255))
        running = False
        
    #set 60 fps
    clock.tick(60)

    #display fps
    fontFps = pygame.font.SysFont(None, 36)
    textFps = fontFps.render("FPS:" + str(format(clock.get_fps(),'.2f')), True, (255,255,255))
    screen.blit(textFps, (0,0))
    
    #Update the screen
    pygame.display.update()


