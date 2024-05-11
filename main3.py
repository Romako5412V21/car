import pygame 
pygame.init()
y = 1

class Player():
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect()
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота
        self.is_jump = False  # змінна для визначення стану прижку
        self.jump_count = 10  # лічильник для керування прижком
    def jumping(self):  # функція для виконання прижку
        if not self.is_jump:  # якщо персонаж не в стані прижку
            self.is_jump = True  # зміна стану прижку
            self.jump_count = 10  # початкове значення лічильника прижку


    def jump(self):  # метод для руху персонажа
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # якщо натиснута клавіша пробілу
            self.jumping()  # виконати прижок

        if self.is_jump:  # якщо персонаж у стані прижку
            if self.jump_count >= -10:  # поки лічильник більше або рівний -10
                neg = 1  # коефіцієнт для керування напрямком прижку
                if self.jump_count < 0:  # якщо лічильник менше 0
                    neg = -1  # змінити напрямок прижку
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg  # формула для прижку
                self.jump_count -= 1  # зменшення лічильника
            else:  # якщо лічильник вийшов за межі -10
                self.is_jump = False  # зміна стану прижку
    
     

    def move(self):
        keys = pygame.key.get_pressed() # зберігаємо всі можливі натиснуті клавіші в список keys
        if keys[pygame.K_a]: # якщо натиснута клавіша "стрілка ліворуч"
            self.rect.x -= 2  # змінюємо координати гравця по x на -2
    
    



window = pygame.display.set_mode((1366,700))
pygame.display.set_caption("Гра з персонажем")

background_image = pygame.image.load('pole.jpg')  # Замість 'background.jfif' вкажіть шлях до вашого зображення фону
background_image = pygame.transform.scale(background_image, (1366,700)) # задання розмірів фонового зображення

# Колір фону
bg_color = (255, 255, 255)
player = Player(100, 450, 50, 50, 'Dino.png')
kak = Player(633, 430, 100, 100, 'kak.png')
kak1 = Player(500, 430, 100, 100, 'kak.png')
kak2 = Player(500, 430, 100, 100, 'kak.png')
kak3 = Player(500, 430, 100, 100, 'kak.png')
kak4 = Player(500, 430, 100, 100, 'kak.png')

kaks = [kak,kak1,kak2,kak3,kak4]

# Головний цикл гри
clock = pygame.time.Clock()
game = True
while game:
    

       # Відображення фону
    window.blit(background_image, (0, 0))

    # Перевірка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    # виклик функції прижку до персонажу
    player.jump()

    

    
    # Оновлення екрану
    window.blit(player.image, (player.rect.x, player.rect.y))  # Відображення зображення гравця
    window.blit(kak.image, (kak.rect.x, kak.rect.y))  
    window.blit(kak1.image, (kak1.rect.x, kak1.rect.y))  
    window.blit(kak2.image, (kak2.rect.x, kak2.rect.y)) 
    window.blit(kak3.image, (kak3.rect.x, kak3.rect.y)) 
    window.blit(kak4.image, (kak4.rect.x, kak4.rect.y)) 

    
    if kak.rect.colliderect(player.rect):
       print('Зіткнення відбулося')
       game = False

    kaks.move()

    clock.tick(60)
    pygame.display.update()


pygame.quit()