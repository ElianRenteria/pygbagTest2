import pygame
class Player:
    def __init__(self):
        self.x = 450
        self.y = 550
        self.sprite = pygame.transform.scale(pygame.image.load("cat.png"),(75, 75))
        self.jump = False
        self.gravity = 10
        self.hitbox = pygame.Rect(self.x+16, self.y+10, 40, 60)
        self.collideLeft = False
        self.collideTop = False
        self.collideBottom = False
        self.collideRight = False
    def draw(self, window, platforms):
        self.move(platforms)
        window.blit(self.sprite,(self.x, self.y))
        #pygame.draw.rect(window,(0, 0,0), self.hitbox, 2)
    def move(self, platforms):
        for platform in platforms:
            if self.hitbox.colliderect(platform.left) and not self.hitbox.colliderect(platform.top) and not self.hitbox.colliderect(platform.bottom):
                self.collideLeft = True
            if self.hitbox.colliderect(platform.right) and not self.hitbox.colliderect(platform.top) and not self.hitbox.colliderect(platform.bottom):
                self.collideRight = True
            if self.hitbox.colliderect(platform.top):
                self.collideTop = True
            if self.hitbox.colliderect(platform.bottom):
                self.collideBottom = True
        self.hitbox = pygame.Rect(self.x+16, self.y+10, 40, 60)
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_UP]and not self.jump:
            self.jump = True
            self.gravity = -14
            self.y -= 10
        if userinput[pygame.K_LEFT]and self.x > 0:
            self.x -= 5
        if self.collideLeft:
            self.x -= 3
            self.collideLeft = False
        if userinput[pygame.K_RIGHT] and self.x < 900:
            self.x += 5
        if self.collideRight:
            self.x += 3
            self.collideRight = False
        if self.collideTop:
            self.gravity = 0
            self.collideTop = False
            self.jump = False
        if self.y < 550:
            self.y += self.gravity
            if self.gravity <10:
                self.gravity += 1
            if self.collideBottom:
                self.gravity = 5
                self.collideBottom = False
                self.y += 30
        elif self.y > 550:
            self.y = 550
            self.gravity = 5
            self.jump = False
            self.collideTop = False
        else:
            self.gravity = 5
            self.collideTop = False
            self.jump = False
