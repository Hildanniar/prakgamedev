import pygame, sys #library
from pygame import rect
from pygame.locals import *
import time


WIDTH, HEIGHT = 400, 400  #lebar dan panjang layar
pygame.display.set_caption('Smooth Movement') #pemberian nama output saat di running

pygame.init() #menginisialisasi semua modul yang diperlukan untuk PyGame
win = pygame.display.set_mode((WIDTH, HEIGHT)) #Memanggil nilai WIDTH, HEIGHT
clock = pygame.time.Clock() #mengetahui waktu yang diperlukan untuk benda bergerak

#mengatur warna RGB Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (210, 43, 140, 1.0)
YELLOW = (255, 253, 0, 1.0)
GGRN = (25, 145, 112, 1.0)


#membuat sebuah objek
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self): #mengupdate properti-properti pada object
        self.velX = 0 #arah gerak pada object yaitu secara horizontal, dimulai dari titik 0
        self.velY = 0 #arah gerak pada object yaitu secara vertical, dimulai dari titik 0
        if self.left_pressed and not self.right_pressed: #jika menekan tombol kiri maka arah gerak menuju arah kiri (koordinat x negatif)
            if self.x >0: #memberikan batas untuk tidak melewati display window (horizontal)
                self.velX = -self.speed
        if self.right_pressed and not self.left_pressed: #jika menekan tombol kanan maka arah gerak menuju arah kanan (koordinat x positif)
            if self.x < 400 -32: #memberikan batas untuk tidak melewati display window (horizontal)
                self.velX = self.speed
        if self.up_pressed and not self.down_pressed: #jika menekan tombol atas maka arah gerak menuju arah atas (koordinat y positif)
            if self.y > 0: #memberikan batas untuk tidak melewati display window ( vertical)
                self.velY = -self.speed
        if self.down_pressed and not self.up_pressed: #jika menekan tombol bawah maka arah gerak menuju arah bawah (koordinat y negatif)
            if self.y < 400 - 32: #memberikan batas untuk tidak melewati display window (vertical)
                self.velY = self.speed

        self.x += self.velX 
        self.y += self.velY 

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

#membagi Hegiht dan Widht menjadi 2
player = Player(WIDTH/2, HEIGHT/2)
#merubah warna Huruf
font_color = (255, 255, 255)
#memberi nama Font beserta ukurannya
font_obj = pygame.font.Font("BerthaMelanie.TTF",23)
#deskripsi yang akan muncul
text = "Hildanniar Fauzi"
#Font akan muncul dan warna menjadi putih
img = font_obj.render(text, True, (WHITE))

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))


#mengatur arah keyboard
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
            if event.type == QUIT:
                    running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]

                else:
                    text += event.unicode
                    img = font_obj.render(text, True, PINK)
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright
                    
    #menampilkan warna background
    win.fill((RED))
    pygame.draw.rect(win, (WHITE), player)

    win.blit(img,rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(win, RED, cursor)
    pygame.display.update()

    player.update()
    #Menampilkan hasil keselurahn
    pygame.display.flip()

    clock.tick(120)
    pygame.display.update()
    
pygame.quit()
