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
                        # print("Hello")
                        # playhover = pygame.image.load('assets/images/playhover.png').convert_alpha()
                        # self.image = pygame.transform.scale(playhover, (int(self.width * self.scale ), int(self.height * self.scale )))
                        
                        
                        # quithover = pygame.image.load('assets/images/quithover.png').convert_alpha()
                        # self.image = pygame.transform.scale(quithover, (int(self.width * self.scale ), int(self.height * self.scale )))

                
                        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                                self.clicked = True
                                action = True

                if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

                if self.rect.collidepoint(pos):
                        
                        playhover = pygame.image.load('assets/images/playhover.png').convert_alpha()
                        self.image = pygame.transform.scale(playhover, (int(self.width * self.scale ), int(self.height * self.scale )))
                else:
                        print("HELLO")
                        playbutton = pygame.image.load('assets/images/playbutton.png').convert_alpha()
                        self.image = pygame.transform.scale(playbutton, (int(self.width * self.scale ), int(self.height * self.scale )))
                
                # else:
                #         print("HELLO")
                #         start_img = pygame.image.load('assets/images/playbutton.png').convert_alpha()
                #         self.image = pygame.transform.scale(start_img, (int(self.width * self.scale ), int(self.height * self.scale )))




                surface.blit(self.image, (self.rect.x,self.rect.y))

                return action
        

        # def hover(self, surface):
        #         pos = pygame.mouse.get_pos()

        #         if self.rect.collidepoint(pos):
                        
        #                 playhover = pygame.image.load('assets/images/playhover.png').convert_alpha()
        #                 self.image = pygame.transform.scale(playhover, (int(self.width * self.scale ), int(self.height * self.scale )))
        #         else:
        #                 playbutton = pygame.image.load('assets/images/playbutton.png').convert_alpha()
        #                 self.image = pygame.transform.scale(playbutton, (int(self.width * self.scale ), int(self.height * self.scale )))
                
                        

