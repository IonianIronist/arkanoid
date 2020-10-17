import sys, pygame

def check_events(player, ball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player.rect.left > 0:
                player.move_left = True
            if event.key == pygame.K_RIGHT and player.rect.right < player.screen_rect.right:
                player.move_right = True
            if event.key == pygame.K_SPACE:
                ball.paused = not ball.paused
                player.paused = not player.paused
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.move_left = False
            if event.key == pygame.K_RIGHT:
                player.move_right = False
