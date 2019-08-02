import pgzrun

WIDTH = 1280
HEIGHT = 720
main_box = Rect(0,0,820,240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)
#placing boxes on the screen
main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
timeLeft = 15
q1 = ["what is the capital of France?", "London", "Paris", "Berlin", "Tokyo", 2]
q2 = ["what is the capital of Canada?", "New York", "London", "Ottawa", "San Francisco", 3]
q3 = ["what is the capital of Portugal?", "Lisbon", "Paris", "Berlin", "Tokyo", 1]
q4 = ["what is the capital of Russia?", "London", "Paris", "Moscow", "Tokyo", 3]
q5 = ["what is the capital of United Kingdom?", "London", "Paris", "Berlin", "Tokyo", 1]
questions = [q1, q2, q3, q4, q5]
question = questions.pop(0)

def draw():
  screen.fill("white")
  screen.draw.filled_rect(main_box, "sky blue")
  screen.draw.filled_rect(timer_box, "sky blue")
  for box in answer_boxes:
    screen.draw.filled_rect(box, "orange")

  screen.draw.textbox(str(timeLeft), timer_box, color="black")
  screen.draw.textbox(question[0], main_box, color="black")
  index = 1
  for box in answer_boxes:
    screen.draw.textbox(question[index], box, color="black")  
    index += 1

def game_over():
    global question, timeLeft
    message = "Game Over! You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    timeLeft = 0

def correct_ans():
    global question, score, timeLeft
    score += 1
    if questions:
        question = questions.pop()
        time_left = 10
    else:
        game_over()
        
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer", str(index))
            if index == question[5]:
                print("you got it correct!")
                correct_ans()
            else:
                game_over()
        index += 1
        
def update_time_left():
    global timeLeft
    if timeLeft:
        timeLeft -= 1
    else:
        game_over()
clock.schedule_interval(update_time_left, 1.0)

pgzrun.go()

