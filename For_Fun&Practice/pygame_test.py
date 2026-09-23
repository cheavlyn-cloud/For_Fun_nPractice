import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

square_pos = pygame.Rect(375, 275, 50, 50)

circle_pos = pygame.Vector2(200, 200)
circle_spd = pygame.Vector2()
circle_rad = 20
circle_acc = 0.01
circle_spd_mul = 0.99
bounce_str = 1.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square_pos.y -= 5
    if keys[pygame.K_DOWN]:
        square_pos.y += 5
    if keys[pygame.K_LEFT]:
        square_pos.x -= 5
    if keys[pygame.K_RIGHT]:
        square_pos.x += 5

    # Apply friction
    circle_spd *= circle_spd_mul
    # Accelerate toward the square
    circle_spd += (pygame.Vector2(square_pos.center) - circle_pos) * circle_acc

    # Bounce off walls
    if circle_pos.x < circle_rad:
        circle_pos.x = circle_rad
        circle_spd.x = -circle_spd.x * bounce_str
    elif circle_pos.x > screen.get_width() - circle_rad:
        circle_pos.x = screen.get_width() - circle_rad
        circle_spd.x = -circle_spd.x * bounce_str

    if circle_pos.y < circle_rad:
        circle_pos.y = circle_rad
        circle_spd.y = -circle_spd.y * bounce_str
    elif circle_pos.y > screen.get_height() - circle_rad:
        circle_pos.y = screen.get_height() - circle_rad
        circle_spd.y = -circle_spd.y * bounce_str

    circle_pos += circle_spd

    screen.fill('black')
    pygame.draw.circle(screen, 'blue', circle_pos, circle_rad)
    pygame.draw.rect(screen, 'red', square_pos)
    pygame.display.flip()
    clock.tick(60)