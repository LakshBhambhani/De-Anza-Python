import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400,300

tree = Actor("tree")
tree.pos = randint(800, 1600), 460

house = Actor("house")
house.pos = randint(800, 1600), 460

bird = Actor("bird-down")
bird.pos = randint(80,1600), randint(10, 200)

game_over = False
score = 0
up = False
bird_up = True
number_of_updates = 0

def draw():
    screen.blit("background", (0,0))
    if not game_over:
        balloon.draw()
        tree.draw()
        house.draw()
        bird.draw()  
        screen.draw.text("Score:"+str(score), (700,5), color="black")
    else:
        display_high_score()

def update():
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            balloon.y+=6
        if bird.x>0:
            bird.x-=4
            if number_of_updates ==8:
                flap()
                number_of_updates = 0
            else:
                number_of_updates+=1
        else:
            bird.x = randint(800,1600)
            bird.y = randint(10,200)
            score+=1
            number_of_updates = 0
        if house.right>0:
            house.x-=2
        else:
            house.x = randint(800, 1600)
            score+=1
        if tree.right>0:
            tree.x-=2
        else:
            tree.x = randint(800, 1600)
            score+=1
        if balloon.top <0 or balloon.bottom>560:
            game_over=True
            display_high_score()
        if balloon.collidepoint(bird.x, bird.y) or\
           balloon.collidepoint(house.x, house.y) or\
           balloon.collidepoint(tree.x, tree.y):
            game_over=True
            display_high_score()

def on_mouse_down(pos):
    global up
    up = True
    balloon.y-=50

def on_mouse_up():
    global up
    up = False
    
def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird.up = True
        
def display_high_score():
    screen.fill("red")
    screen.draw.text("Score: "+str(score), (350, 150), color="black")

pgzrun.go()
