import pygame
import sys
from pygame.locals import*

#variables generales
game_state = 1
WIDTH = 480
HEGIHT = 320
tiempo = 0
floor_y =260
clock = pygame.time.Clock()

#variables prota
x = 50
y = 260
prota_w=50
prota_h=37
prota_flipped = False
prota_vidas = 3
prota_tocado = False
prota_run_L = False
prota_run_R = False
frame_count_prota = 0
animation_prota_end = False
tiempo_invul = 0
prota_vivo = True
speed = 8

#variables saltar
jump_h = 100
jump_speed = -4
jump_speed_up = -4
jump_speed_down = 3
jumping = False
fall = False


#variables malo
maloso_y = 236
maloso_x = WIDTH - 100
maloso_vivo = True
maloso_vidas= 3
maloso_Tam_X =60
maloso_Tam_Y = 60
maloso_speed = 4


#variables boton
button_y = 233
button_x= WIDTH/2 - 50


#variables disparar
bullet_x = x
bullet_y = y
fire = False
bullet_speed = 8
bullet_dir = 1
bullet_flipped = False
shoot_rate = 30
shoot_rate_counter = 30
start_counter_shoot = False

#variables de la ventana
pygame.init()
screen= pygame.display.set_mode((WIDTH, HEGIHT))
pygame.display.set_caption("Intro programació Juegos")
pygame.mouse.set_visible(0)

#fuente i textos
pygame.font.init()
fuente_txt = pygame.font.SysFont("Comic Sans MS",30 )
tutorial_saltar = fuente_txt.render("space", False, (255,255,255))
tutorial_mover = fuente_txt.render("<-- -->", False, (255,255,255))
tutorial_disparar = fuente_txt.render("F", False, (255,255,255))
titulo = fuente_txt.render("Juegaco", False, (255,255,255))
score = 0




#Animaciones del prota
prota_idle_L = [pygame.image.load("idle/adventurer-idle-00.png"),pygame.image.load("idle/adventurer-idle-01.png"),pygame.image.load("idle/adventurer-idle-02.png")]
prota_idle_D = [pygame.image.load("idle/adventurer-idle-00.png"),pygame.image.load("idle/adventurer-idle-01.png"),pygame.image.load("idle/adventurer-idle-02.png")]
walk_prota_R = [pygame.image.load("walk/adventurer-run-00.png"), pygame.image.load("walk/adventurer-run-01.png"), pygame.image.load("walk/adventurer-run-02.png"),pygame.image.load("walk/adventurer-run-03.png"),pygame.image.load("walk/adventurer-run-04.png"), pygame.image.load("walk/adventurer-run-05.png")]
walk_prota_L = [pygame.image.load("walk/adventurer-run-00.png"), pygame.image.load("walk/adventurer-run-01.png"), pygame.image.load("walk/adventurer-run-02.png"),pygame.image.load("walk/adventurer-run-03.png"),pygame.image.load("walk/adventurer-run-04.png"), pygame.image.load("walk/adventurer-run-05.png")]
cast_prota_L = [pygame.image.load("cast/adventurer-cast-00.png"),pygame.image.load("cast/adventurer-cast-01.png"), pygame.image.load("cast/adventurer-cast-02.png"),pygame.image.load("cast/adventurer-cast-03.png")]
cast_prota_D = [pygame.image.load("cast/adventurer-cast-00.png"),pygame.image.load("cast/adventurer-cast-01.png"), pygame.image.load("cast/adventurer-cast-02.png"),pygame.image.load("cast/adventurer-cast-03.png")]
jump_prota_L = [pygame.image.load("jump/adventurer-jump-00.png"),pygame.image.load("jump/adventurer-jump-01.png"), pygame.image.load("jump/adventurer-jump-02.png"), pygame.image.load("jump/adventurer-jump-03.png")]
jump_prota_D = [pygame.image.load("jump/adventurer-jump-00.png"),pygame.image.load("jump/adventurer-jump-01.png"), pygame.image.load("jump/adventurer-jump-02.png"), pygame.image.load("jump/adventurer-jump-03.png")]
fall_prota_L = [pygame.image.load("fall/adventurer-fall-00.png"), pygame.image.load("fall/adventurer-fall-00.png")]
fall_prota_D = [pygame.image.load("fall/adventurer-fall-00.png"), pygame.image.load("fall/adventurer-fall-00.png")]
prota = prota_idle_L[0]

#darle la vuelta a todas las imagenes de caminar
count = 0
while len(cast_prota_D)-1 >= count:
    cast_prota_D[count] = pygame.transform.flip(cast_prota_D[count] , True ,False)
    count += 1
    
count = 0    
while len(walk_prota_L)-1 >= count:
    walk_prota_L[count] = pygame.transform.flip(walk_prota_L[count] , True ,False)
    count += 1
    
count = 0    
while len(jump_prota_L)-1 >= count:
    jump_prota_D[count] = pygame.transform.flip(jump_prota_L[count] , True ,False)
    count += 1
    
count = 0    
while len(fall_prota_L)-1 >= count:
    fall_prota_D[count] = pygame.transform.flip(fall_prota_L[count] , True ,False)
    count += 1
    
count = 0    
while len(prota_idle_L)-1 >= count:
    prota_idle_D[count] = pygame.transform.flip(prota_idle_L[count] , True ,False)
    count += 1

#cargar imagenes
bg = pygame.image.load("background.jpg")
maloso = pygame.image.load("maloso.png")
bullet = pygame.image.load("proyectil.gif")
button_start=pygame.image.load("button.png")
button_replay =pygame.image.load("replay.png")
button_start = pygame.transform.scale(button_start,(100,40))
button_replay = pygame.transform.scale(button_replay,(100,40))
maloso = pygame.transform.scale(maloso, ( maloso_Tam_X, maloso_Tam_Y))
bg = pygame.transform.scale(bg, (WIDTH,HEGIHT))
bullet = pygame.transform.scale(bullet, (48,48))
    
#efectos de sonido i musica
shoot_sound = pygame.mixer.Sound('Music/shoot.wav')
shoot_sound.set_volume(0.1)
hit_sound = pygame.mixer.Sound('Music/hit.wav')
hit_sound.set_volume(0.1)
music = pygame.mixer.music.load("Music/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

#volver a los valores iniciales
def reset_partida():
    
    global x
    global y
    global prota_flipped
    global prota_vidas
    global prota_tocado
    global tiempo
    global maloso_y
    global maloso_x
    global maloso_vivo
    global maloso_vidas
    global jumping
    global bullet_flipped
    global bullet
    global score
    global prota
    global fire
    global maloso
    global tiempo_invul
    global fall
    global prota_vidas
    global frame_count_prota
    global animation_prota_end
    global shoot_rate
    global start_counter_shoot
    global shoot_rate_counter
    global prota_vivo
    global prota_idle
    global bullet_dir
    global walk_prota
    global maloso_Tam_X
    global maloso_Tam_Y
    global maloso_speed
    
    maloso_y = 236
    maloso_x = WIDTH - 100
    maloso_vivo = True
    maloso_vidas= 3
    maloso_Tam_X =60
    maloso_Tam_Y = 60
    maloso_speed = 4
    score = 0
    
    x = 50
    y = 260
    prota_flipped = False
    prota_vidas = 3
    prota_tocado = False
    prota_run_L = False
    prota_run_R = False
    frame_count_prota = 0
    animation_prota_end = False
    tiempo_invul = 0
    prota_vivo = True
    
    jumping = False
    fall = False
   
    fire = False
    bullet_speed = 8
    bullet_dir = 1
    
    shoot_rate = 30
    shoot_rate_counter = 30
    start_counter_shoot = False
    maloso = pygame.image.load("maloso.png")
    maloso = pygame.transform.scale(maloso, ( maloso_Tam_X, maloso_Tam_Y))
    if prota_flipped:
        prota_flipped = False
        prota_idle = pygame.transform.flip(prota, True ,False)
        walk_prota[walkCount] = pygame.transform.flip(walk_prota[walkCount], True, False)

    if bullet_flipped:
        bullet_flipped = False
        bullet = pygame.transform.flip(bullet, True ,False)
        
   
        
    return 2

#funcion para poder hacer animaciones del prota
def play_anim_prota(array_anim, frames_second, loop):
    
    global frame_count_prota
    global animation_prota_end
    
    
        
    if tiempo  % frames_second == 0:
        frame_count_prota += 1
        
    if frame_count_prota >= len(array_anim):
        if loop:
            frame_count_prota =0
        else:
            animation_prota_end = True
            frame_count_prota =0
            
    return array_anim[frame_count_prota]    
      
     
        
#saltar
def saltando() :
    global y
    global jumping
    global jump_speed
    global jump_h
    global fall
    
    y= y + jump_speed
    #si llegamos al tope, bajamos
    if y <= floor_y - jump_h:
        fall = True
        y=floor_y - jump_h
        jump_speed = jump_speed_down
        fall = True
        
    #si llegamos al suelo reiniciamos
    if y >= floor_y:
        y = floor_y
        jump_speed = jump_speed_up
        fall = False
        jumping = False
        
#actitud del malo
def maloso_move ():
    global maloso_x
    global maloso_speed
    global maloso
    global prota_tocado
    global prota_vidas
    global prota_vivo
    global maloso_fliped
    
    maloso_x = maloso_x -maloso_speed
    
    if maloso_x<=0:
        maloso_x = 0
        maloso_speed = -maloso_speed
        maloso = pygame.transform.flip(maloso, True, False)
       
    if maloso_x >= WIDTH - 64:
        maloso_x = WIDTH - 64
        maloso_speed = -maloso_speed
        maloso = pygame.transform.flip(maloso, True ,False)
       
    if not prota_tocado:
        if (x >= maloso_x and x<= maloso_x + 64) or (x + prota_w >= maloso_x and x + prota_w <= maloso_x + 64):
            if (y >= maloso_y and y<= maloso_y + 64) or (y + prota_h >= maloso_y and y + prota_h <= maloso_y + 64):
                print("golpe")
                prota_vidas =  prota_vidas - 1
                #matar el jugador
                if prota_vidas <= 0:
                    prota_vivo = False
                prota_tocado=True
#movimiento de la bala                
def bullet_move():
    global bullet_x
    global bullet_y
    global bullet
    global fire
    global maloso_vivo
    global maloso_vidas
    global maloso_x
    global vidas_maloso
    global score
    global hit_sound
    
    
    bullet_x = bullet_x + bullet_dir*bullet_speed
    if bullet_x <= 0:
        fire = False
    elif bullet_x+48 >= WIDTH:
        fire = False    
    if maloso_vivo:
        
        if (bullet_x >= maloso_x and bullet_x<= maloso_x + 64) or (bullet_x + 48 >= maloso_x and bullet_x + 48 <= maloso_x + 64):
                
            if (bullet_y >= maloso_y and bullet_y<= maloso_y + 64) or (bullet_y + 48 >= maloso_y and bullet_y + 48 <= maloso_y + 64):
                hit_sound.play()
                fire = False
                maloso_vidas = maloso_vidas -1
                
                print(maloso_vidas)
                
                #matar al malo
                if maloso_vidas <= 0:
                    score = score +10
                    maloso_vivo = False 
                
        
#juego
if __name__ == "__main__":
    
    while True:
        #pantalla inicial
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        
        #MENU INICIAL
        if game_state == 1:
            pygame.mouse.set_visible(True)
            #boton para empezar la partida, en principio creo que sería mas logico que se empezara pulsando un boton del teclado, pero de esta forma aprendo a crear un boton que se aprieta con el ratón
            if event.type == MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pos()[0] >= button_x) and (pygame.mouse.get_pos()[0]<= button_x+ 100):
                    
                    if (pygame.mouse.get_pos()[1] >= button_y and pygame.mouse.get_pos()[1]<= button_y+ 40):
                        game_state =2
                
                
                
                
            screen.fill([0,0,0])
            screen.blit(bg, (0,0))
            #Recorad que se puede obtener el witdh y Hegiht con el get_width y get_hegiht
            screen.blit(titulo,(WIDTH/2-titulo.get_width()/2, 0))
            screen.blit(button_start,(button_x,button_y))
            #tutorial
            screen.blit(jump_prota_L[2], (35,HEGIHT/2.5))
            screen.blit(walk_prota_L[3], (tutorial_saltar.get_width()+WIDTH/3.8 +15,HEGIHT/2.5))
            screen.blit(cast_prota_L[3], (tutorial_saltar.get_width()+WIDTH/1.6-15 ,HEGIHT/2.5))
            screen.blit(tutorial_mover, (tutorial_saltar.get_width()+WIDTH/3.8, HEGIHT/2))
            screen.blit(tutorial_disparar, (tutorial_saltar.get_width()+WIDTH/1.6, HEGIHT/2))
            screen.blit(tutorial_saltar, (WIDTH/24,HEGIHT/2))    
                
                
                
        if game_state == 2:
            
            #logica de los comando cuando juegas
            #controles
            if keys[K_LEFT]:
                print("Izquierda")
                prota_run_L = True
                prota_run_R = False
                
                if not prota_flipped:
                    prota_flipped = True
                    
                    
                x = x - speed
                if x <= 0:
                    x = 0
                
            elif keys[K_RIGHT]:
                print("Derecha")
                
                prota_run_L = False
                prota_run_R = True
                
                if prota_flipped:
                    prota_flipped = False
                    
                if x >= WIDTH - 50:
                    x = WIDTH - 50
                
                x = x + speed    
            
            elif keys[K_r]:
                game_state = reset_partida()
            
            elif keys[K_f]:
                
                if not fire and shoot_rate <= shoot_rate_counter:
                    start_counter_shoot = True
                    fire = True
                    shoot_sound.play()
                    animation_prota_end = False
                    bullet_x=x
                    bullet_y=y
                    bullet_dir = 1
                    if prota_flipped:
                        bullet_dir = -1    
                        if not bullet_flipped:
                            bullet = pygame.transform.flip(bullet, True ,False)
                            bullet_flipped = True
                    else:
                        if bullet_flipped:
                            bullet = pygame.transform.flip(bullet, True ,False)
                            bullet_flipped = False
            elif keys[K_SPACE]:
                print("Salto")
                if not jumping:
                    animation_prota_end = False
                    jumping = True           
            else :
                prota_run_L = False
                prota_run_R = False
            if jumping:
                saltando()   
            

                    
            
            
            
            screen.fill([0,0,0])
            
            screen.blit(bg, (0,0))
            #Todo lo que se muestra en pantalla mientras el jugador esta vivo
            if prota_vivo:
            #logica de las animaciones del jugador
                
                if prota_run_L == True and jumping == False:
                    prota = play_anim_prota(walk_prota_L,5, True)
                    
                elif prota_run_R == True and jumping == False:
                    prota = play_anim_prota( walk_prota_R, 5, True)
                    
                elif animation_prota_end == False and fire == True and prota_flipped == False and jumping == False:
                    prota = play_anim_prota(cast_prota_L,5, False);
                    
                elif animation_prota_end == False and fire == True and prota_flipped == True and jumping == False:
                    prota = play_anim_prota(cast_prota_D,5, False);
                    
                elif jumping == True and animation_prota_end == False and prota_flipped == False and fall == False:
                    prota = play_anim_prota(jump_prota_L ,4, False);
                
                elif jumping == True and animation_prota_end == False and prota_flipped == True and fall == False:
                    prota = play_anim_prota(jump_prota_D , 4 , False);
                    
                elif prota_flipped == False and fall == True:
                    prota = play_anim_prota(fall_prota_L ,5, True);
                
                elif prota_flipped == True and fall == True:
                    prota = play_anim_prota(fall_prota_D , 5 , True);
                    
                elif not jumping and prota_flipped == False:
                    prota = play_anim_prota(prota_idle_L , 5 , True);
                    
                elif not jumping and prota_flipped == True:
                    prota = play_anim_prota(prota_idle_D , 5 , True);   
                 
                #dibujar el prota 
                if not prota_tocado:
                    
                    screen.blit(prota, (x,y))
                #si es golpeado hacer invulnerable i que parpade
                else:
                    # El % vol dir modulo que fa referencia a lo que sobra de la divisió o altra manera de dir que es multiple, en aquest cas volem fer referencia a als numeros pars
                    #ja que si la resta de la divisió del numero del prota entre 2 es 0 vol dir que el numero es par
                    
                    fire = False
                    tiempo_invul = tiempo_invul +1
                    if tiempo % 2== 0:
                        screen.blit(prota, (x,y))
                    if tiempo_invul >= 30:
                        prota_tocado = False
                        tiempo_invul = 0
          
                #Si el malo esta vivo que se mueva
                if maloso_vivo:
                    maloso_move()
                    screen.blit(maloso, (maloso_x,maloso_y))
                    vidas_maloso = fuente_txt.render("Maloso: " + str (maloso_vidas), False, (255,255,255))
                    vidas_prota = fuente_txt.render ("Vidas: " + str (prota_vidas), False, (255,255,255))
                    screen.blit(vidas_maloso,(WIDTH - vidas_maloso.get_width(), 0))
                    screen.blit(vidas_prota,(0, 0))
               #Si el malo muere que salga otro mas grande
                else:
                    if x <= WIDTH/2:
                    
                        maloso_x = WIDTH + 200
                    else:
                        maloso_x = 0
                        
                    maloso_vidas = 3
                    if maloso_Tam_Y <= 100:
                        maloso_Tam_X = maloso_Tam_X + 5
                        maloso_Tam_Y = maloso_Tam_Y + 5
                        maloso_y = maloso_y - 3
                        maloso = pygame.transform.scale(maloso, ( maloso_Tam_X, maloso_Tam_Y))
                    
                     
                    maloso_vivo = True
                    
           
                
                #Dibujar la bala
                if fire:
                    bullet_move()
                    screen.blit(bullet, (bullet_x, bullet_y))
                #La cuenta atras para poder disparar
                if start_counter_shoot == True:    
                    shoot_rate_counter =  shoot_rate_counter -1
                    print(shoot_rate_counter)
                if shoot_rate_counter <= 0:
                    shoot_rate_counter = shoot_rate
                    start_counter_shoot = False
            else:
                #si muere el jugador ir a la pantalla de GameOver
                game_state = 3
                 
               
                
            score_titulo = fuente_txt.render("score "+str (score), False, (255,255,255))
            screen.blit(score_titulo,(WIDTH/2-titulo.get_width()/2, 0))
        #Pantalla de Game Over   
        if game_state == 3:
            pygame.mouse.set_visible(True)
          
            if event.type == MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pos()[0] >= button_x) and (pygame.mouse.get_pos()[0]<= button_x+ 100):
                    
                    if (pygame.mouse.get_pos()[1] >= button_y and pygame.mouse.get_pos()[1]<= button_y+ 40):
                        #Restablecer valores iniciales                        
                        
                        game_state = reset_partida()
                        
            
            screen.fill([0,0,0])
            screen.blit(bg, (0,0))
            screen.blit(titulo,(WIDTH/2-titulo.get_width()/2, 0))
            
            screen.blit(button_replay,(button_x,button_y))
            vidas_maloso = fuente_txt.render("Tu puntuacuión ha sido: " + str (score),False, (255,255,255))
            screen.blit(vidas_maloso,(WIDTH/2 - vidas_maloso.get_width()/2, HEGIHT/2))
        tiempo = tiempo +1
        pygame.display.flip()    
        clock.tick(30)
