import pygame

WHITE = (255, 255, 255)
ORANGE = (255, 153, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# ------------------------------
heroSprite = pygame.Surface((100, 70))
pygame.draw.rect(heroSprite, RED, (0, 0, 100, 60))
pygame.draw.circle(heroSprite, WHITE, (15, 60), 10)
pygame.draw.circle(heroSprite, WHITE, (85, 60), 10)
heroSprite.set_colorkey(BLACK)
# set_colorkey(<COLOR>) configure <COLOR> to be transparent

# ------------------------------
ballSpriteOrange = pygame.Surface((20,20))
pygame.draw.circle(ballSpriteOrange, ORANGE, (10, 10), 10)
heroSprite.set_colorkey(BLACK)

# ------------------------------
ballSpriteBLUE = pygame.Surface((20,20))
pygame.draw.circle(ballSpriteBLUE, BLUE, (10, 10), 10)
heroSprite.set_colorkey(BLACK)

# ------------------------------
# animation = []
# animation.add(heroSprite)
# animation.add(ballSpriteBLUE)



# This loads an image as a surface. It takes name of the image file
someLoadedImage = pygame.image.load("ActionGameProject/Fred animation demo/ball.png")
# <<ADVANCED>> This can some how make screen.blit(someLoadedImage, (x, y)) much faster
# ============ because it convert someLoadedImage into a format based on the current resolution
someLoadedImage = pygame.transform.scale(someLoadedImage, (20, 20))
someLoadedImage = someLoadedImage.convert()
someLoadedImage.set_colorkey(WHITE)

