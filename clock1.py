import pygame,math,datetime
pygame.init()
dis=pygame.display.set_mode((600,600))
dis.fill((0,0,0))
pygame.display.update()
clock=pygame.time.Clock()
def dcircle(color,radius,angle):
    pygame.draw.arc(dis,color,(300-radius/2,300-radius/2,radius,radius),angle*math.pi/180,90*math.pi/180,10)
while(1):
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            quit()
    time=datetime.datetime.now()
    dis.fill((0, 0, 0))
    dcircle((225,0,0),350,90-6*time.second)#sec
    dcircle((0,225,0),325,90-6*time.minute)#min
    dcircle((0,0,225),300,90-30*time.hour)#hour


    pygame.display.update()
    clock.tick(1)