import sys, pygame

def check_events(player, ball, go=False, game=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player.rect.left > 0:
                player.move_left = True
            if event.key == pygame.K_RIGHT and player.rect.right < player.screen_rect.right:
                player.move_right = True
            if event.key == pygame.K_SPACE and player.lives > 0:
                ball.paused = not ball.paused
                player.paused = not player.paused
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.move_left = False
            if event.key == pygame.K_RIGHT:
                player.move_right = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if game.go_button.rect.collidepoint(x,y) and game.go:
                    game.restart()

def update_level(blox):
    dead = []    
    for i in range(len(blox)):
        blox[i].blitme()
        if blox[i].life == 0 :
            dead.append(i)
    for d in dead:
        blox.pop(d)


    
    
