import random, pygame, sys
from pygame.locals import *
from bird import Bird
from pipe import Pipe
pygame.init()
screen_info=pygame.display.Info()
size=(width,height)=(int(screen_info.current_w), int(screen_info.current_h))

window=pygame.display.set_mode(size)
clock=pygame.time.Clock()
background = pygame.image.load('background1.png')

background = pygame.transform.scale(background, (width,height))

startPos=(width/8, height/2)
pipes=pygame.sprite.Group()
player = Bird(startPos)
gapSize = 200
loopCount = 0

def lose():
    font = pygame.font.sys_fonts(None, 70)
    text = font.render("You died!", True, (0,0,255))
    text_rect=text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        window.fill(color)
        window.blit(text,text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pipes.empty()
                    player.reset(startPos)
                    return
def main():
    global loopCount
    while True:
        clock.tick(60)
        if loopCount % 60 == 0:
            topPos = random.randint(0, 200)
            pipes.add(Pipe((width + 100, topPos + gapSize + 380)))
            pipes.add(Pipe((width + 100, topPos), True))
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                sys.exit()
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.speed[1] = -10
        player.update()
        pipes.update()
        gets_hit = pygame.sprite.spritecollide(player,pipes,False) \
                or player.rect.center[1] > height
        window.blit(background,[0,0])
        pipes.draw(window)
        window.blit(player.image,player.rect)
        pygame.display.flip()
        loopCount+=1

        if gets_hit:
            lose()
if __name__ == '__main__':
    main()








