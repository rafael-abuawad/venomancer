import pygame

pygame.init()
size = width, height = (720, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

speed = [5, 5]
ball = pygame.image.load("images/intro_ball.gif")
ballrect = ball.get_rect()
alpha = 0
alpha_ticker = 1

screen.fill("black")
ball.set_alpha(0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.blit(ball, ballrect)
    ball.set_alpha(alpha)
    alpha += alpha_ticker
    print(alpha)
    if alpha >= 150 or alpha <= 0:
        alpha_ticker *= -1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
