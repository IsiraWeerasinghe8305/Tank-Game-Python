import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Battle")



PLAYER_SIZE = 30
BULLET_SIZE = 10
PLAYER_SPEED = 5
BULLET_SPEED = 7
Flag_SIZE=50

player_xf = 150
player_yf = SCREEN_HEIGHT // 2 + 50
player2_xf = SCREEN_WIDTH - 180
player2_yf = SCREEN_HEIGHT // 2 + 50

GREEN = (100, 255, 100)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
WHITE = (255, 255, 255)
RED = (255, 0, 0)





# Define the player starting position
player_x = 50 
player_y = SCREEN_HEIGHT // 2
player2_x = SCREEN_WIDTH - 50
player2_y = SCREEN_HEIGHT // 2

bullets = []
walls = [
    pygame.Rect(200, 200, 20, 200),
    pygame.Rect(400, 100, 20, 200),
    pygame.Rect(600, 300, 20, 200),
    pygame.Rect(100, 400, 200, 20),
    pygame.Rect(500, 400, 200, 20),
    pygame.Rect(100, 00, 20,100 ),
    pygame.Rect(600, 00, 20,100 ),
    pygame.Rect(350, 500, 20,100 ),
]


# text in end of the game
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
def game_over_screen(winner):
    screen.fill(WHITE)
    game_over_text = font.render("Game Over", True, RED)
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2 - game_over_text.get_height()//2))
    winner_text = small_font.render(f"{winner} wins!", True, RED)
    screen.blit(winner_text, (SCREEN_WIDTH//2 - winner_text.get_width()//2, SCREEN_HEIGHT//2 + game_over_text.get_height()//2 + 20))
    replay_text = small_font.render("Press Enter to Replay", True, RED)
    screen.blit(replay_text, (SCREEN_WIDTH//2 - replay_text.get_width()//2, SCREEN_HEIGHT//2 + game_over_text.get_height()//2 + 60))
    pygame.display.flip()

    replaying = False
    while not replaying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                replaying = True
                return True
    return False


running = True
clock = pygame.time.Clock()
last_direction = 'd' 
last2_direction = '4'  

def check_bullet_collision(player_rect, bullets):
    for bullet in bullets:
        if player_rect.colliderect(bullet):
            return True
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if last_direction == 'a':
                    bullet = pygame.Rect(player_x, player_y + PLAYER_SIZE // 2 - BULLET_SIZE // 2, BULLET_SIZE, BULLET_SIZE)
                    bullets.append((bullet, 'a', 'player1'))
                elif last_direction == 'd':
                    bullet = pygame.Rect(player_x + PLAYER_SIZE, player_y + PLAYER_SIZE // 2 - BULLET_SIZE // 2, BULLET_SIZE, BULLET_SIZE)
                    bullets.append((bullet, 'd', 'player1'))
                elif last_direction == 'w':
                    bullet = pygame.Rect(player_x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, player_y, BULLET_SIZE, BULLET_SIZE)
                    bullets.append((bullet, 'w', 'player1'))
                elif last_direction == 's':
                    bullet = pygame.Rect(player_x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, player_y + PLAYER_SIZE, BULLET_SIZE, BULLET_SIZE)
                    bullets.append((bullet, 's', 'player1'))
                    
            if event.key == pygame.K_KP_0:
                if last2_direction == '4':
                    bullet2 = pygame.Rect(player2_x, player2_y + PLAYER_SIZE // 2 - BULLET_SIZE // 2, BULLET_SIZE, BULLET_SIZE)
                    bullets.append((bullet2, '4', 'player2'))
                elif last2_direction == '6':
                    bullet2 = pygame.Rect(player2_x + PLAYER_SIZE, player2_y + PLAYER_SIZE // 2 - BULLET_SIZE // 2, BULLET_SIZE, BULLET_SIZE)
                    bullets.append((bullet2, '6', 'player2'))
                elif last2_direction == '8':
                    bullet2 = pygame.Rect(player2_x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, player2_y, BULLET_SIZE, BULLET_SIZE)
                    bullets.append((bullet2, '8', 'player2'))
                elif last2_direction == '5':
                    bullet2 = pygame.Rect(player2_x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, player2_y + PLAYER_SIZE, BULLET_SIZE, BULLET_SIZE)
                    bullets.append((bullet2, '5', 'player2'))

    # Player_movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        if not any(wall.collidepoint(player_x - PLAYER_SPEED, player_y + PLAYER_SIZE // 2) for wall in walls):
            player_x -= PLAYER_SPEED
        last_direction = 'a'
    elif keys[pygame.K_d] and player_x < SCREEN_WIDTH - PLAYER_SIZE:
        if not any(wall.collidepoint(player_x + PLAYER_SIZE + PLAYER_SPEED, player_y + PLAYER_SIZE // 2) for wall in walls):
            player_x += PLAYER_SPEED
        last_direction = 'd'
    elif keys[pygame.K_w] and player_y > 0:
        if not any(wall.collidepoint(player_x + PLAYER_SIZE // 2, player_y - PLAYER_SPEED) for wall in walls):
            player_y -= PLAYER_SPEED
        last_direction = 'w'
    elif keys[pygame.K_s] and player_y < SCREEN_HEIGHT - PLAYER_SIZE:
        if not any(wall.collidepoint(player_x + PLAYER_SIZE // 2, player_y + PLAYER_SIZE + PLAYER_SPEED) for wall in walls):
            player_y += PLAYER_SPEED
        last_direction = 's'

    if keys[pygame.K_LEFT] and player2_x > 0:
        if not any(wall.collidepoint(player2_x - PLAYER_SPEED, player2_y + PLAYER_SIZE // 2) for wall in walls):
            
            player2_x -= PLAYER_SPEED
        last2_direction = '4'
    elif keys[pygame.K_RIGHT] and player2_x < SCREEN_WIDTH - PLAYER_SIZE:
        if not any(wall.collidepoint(player2_x + PLAYER_SIZE + PLAYER_SPEED, player2_y + PLAYER_SIZE // 2) for wall in walls):
            player2_x += PLAYER_SPEED
        last2_direction = '6'
    elif keys[pygame.K_UP] and player2_y > 0:
        if not any(wall.collidepoint(player2_x + PLAYER_SIZE // 2, player2_y - PLAYER_SPEED) for wall in walls):
            player2_y -= PLAYER_SPEED
        last2_direction = '8'
    elif keys[pygame.K_DOWN] and player2_y < SCREEN_HEIGHT - PLAYER_SIZE:
        if not any(wall.collidepoint(player2_x + PLAYER_SIZE // 2, player2_y + PLAYER_SIZE + PLAYER_SPEED) for wall in walls):
            player2_y += PLAYER_SPEED
        last2_direction = '5'

    # Move bullets
    for bullet, direction, owner in bullets[:]:
        if direction == 'a':
            bullet.x -= BULLET_SPEED
        elif direction == 'd':
            bullet.x += BULLET_SPEED
        elif direction == 'w':
            bullet.y -= BULLET_SPEED
        elif direction == 's':
            bullet.y += BULLET_SPEED
        elif direction == '4':
            bullet.x -= BULLET_SPEED
        elif direction == '6':
            bullet.x += BULLET_SPEED
        elif direction == '8':
            bullet.y -= BULLET_SPEED
        elif direction == '5':
            bullet.y += BULLET_SPEED

        # Remove bullets that are out of screen
        if bullet.x < 0 or bullet.x > SCREEN_WIDTH or bullet.y < 0 or bullet.y > SCREEN_HEIGHT:
            bullets.remove((bullet, direction, owner))

        player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
        player2_rect = pygame.Rect(player2_x, player2_y, PLAYER_SIZE, PLAYER_SIZE)
        
        player_rectf = pygame.Rect(player_xf, player_yf, Flag_SIZE, Flag_SIZE)
        player2_rectf = pygame.Rect(player2_xf, player2_yf, Flag_SIZE, Flag_SIZE)

        if owner == 'player1' and bullet.colliderect(player2_rect):
            if game_over_screen("Player 1"):
                player_x, player_y = 50, SCREEN_HEIGHT // 2
                player2_x, player2_y = SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2
                bullets.clear()
        elif owner == 'player1' and bullet.colliderect(player2_rectf):
            if game_over_screen("Player 1"):
                player_x, player_y = 50, SCREEN_HEIGHT // 2
                player2_x, player2_y = SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2
                bullets.clear()
                    
        elif owner == 'player2' and bullet.colliderect(player_rect):
            if game_over_screen("Player 2"):
                player_x, player_y = 50, SCREEN_HEIGHT // 2
                player2_x, player2_y = SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2
                bullets.clear()
        elif owner == 'player2' and bullet.colliderect(player_rectf):
            if game_over_screen("Player 2"):
                player_x, player_y = 50, SCREEN_HEIGHT // 2
                player2_x, player2_y = SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2
                bullets.clear()
                
    # Collision detection with walls
    for wall in walls:
        for bullet, direction, owner in bullets[:]:
            if wall.colliderect(bullet):
                bullets.remove((bullet, direction, owner))

    # Draw everything
    screen.fill(GREEN)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, RED, (player2_x, player2_y, PLAYER_SIZE, PLAYER_SIZE))
    
 
    for bullet, _, _ in bullets:
        pygame.draw.rect(screen, BLACK, bullet)
    for wall in walls:
        pygame.draw.rect(screen, GRAY, wall)

    pygame.draw.rect(screen, BLUE, (player_xf, player_yf, Flag_SIZE, Flag_SIZE))
    pygame.draw.rect(screen, RED, (player2_xf, player2_yf, Flag_SIZE, Flag_SIZE))
    
    
    
    # Update display
    pygame.display.flip()

    clock.tick(60)
pygame.quit()
