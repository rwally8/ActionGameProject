import pygame
pygame.init()
class States:
    def Statechanger(curstate):
        if curstate=="Start Menu":
            while curstate=="Start Menu":
                eventnw=pygame.event.get()
                for events in eventnw:
                    if events.type == pygame.MOUSEBUTTONDOWN:
                        xmse=pygame.mouse.get_pos()[0]
                        ymse=pygame.mouse.get_pos()[1]
                        if ((xmse>=250)&(xmse<=510)&(y>=165)&(y<=220)):
                            state="Game"
                        elif ((xmse>=295)&(xmse<=355)&(y>=325)&(y<=360)):
                            state="Instructions"
                        elif ((xmse>=480)&(xmse<=575)&(y>=325)&(y<=360)):
                            state="Credits"
                    elif events.type==pygame.QUIT:
                        exit()
        elif curstate=="Instructions":
            while curstate=="Instructions":
                eventnw=pygame.event.get()
                for events in eventnw:
                    if events.type == pygame.K_ESCAPE:
                        state="Start Menu"
                    elif events.type==pygame.QUIT:
                        exit()
        elif curstate=="Credits":
            while curstate=="Credits":
                eventnw=pygame.event.get()
                for events in eventnw:
                    if events.type == pygame.K_ESCAPE:
                        state="Start Menu"
                    elif events.type==pygame.QUIT:
                        exit()
        elif curstate=="Pause":
            while curstate=="Pause":
                eventnw=pygame.event.get()
                for events in eventnw:
                    if events.type == pygame.K_ESCAPE:
                        state="Game":
                    elif events.type==pygame.QUIT:
                        exit()
        else:
            exit()
