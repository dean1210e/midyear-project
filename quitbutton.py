import pygame

class Button():
        def __init__(self,x,y,image, scale):
                self.width = image.get_width()
                self.height = image.get_height()
                self.scale = scale
                self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x,y)
                self.clicked = False
        def draw(self, surface):
                action = False
                pos = pygame.mouse.get_pos()

                if self.rect.collidepoint(pos):
                
                        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                                self.clicked = True
                                action = True

                if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

                if self.rect.collidepoint(pos):
                        
                        quithover = pygame.image.load('assets/images/quithover.png').convert_alpha()
                        self.image = pygame.transform.scale(quithover, (int(self.width * self.scale ), int(self.height * self.scale )))
                else:
                        
                        quitbutton = pygame.image.load('assets/images/quitbutton.png').convert_alpha()
                        self.image = pygame.transform.scale(quitbutton, (int(self.width * self.scale ), int(self.height * self.scale )))
            

                surface.blit(self.image, (self.rect.x,self.rect.y))

                return action
        

                        

