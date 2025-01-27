from tkinter import *
import random



GAME_WIDTH = 1000
GAME_HEIGTH = 800
SPEED = 300
space_size = 50
body_parts = 1
snake_color = "#0000ff"
food_color = "#ff0000"
background_color = "#000000"


class Snake:
  def __init__(self):
    self.body_size = body_parts
    self.coordinates = []
    self.squares = []

    for i in range(0, body_parts):
      self.coordinates.append([0,0])

    for x,y in self.coordinates:
      square = canvas.create_rectangle(x,y,x + space_size,y + space_size, fill = snake_color, tag = "snake")
      self.squares.append(square)


class Food:

  def __init__(self):
    x = random.randint(0,(GAME_WIDTH/space_size)-1) * space_size
    y = random.randint(0,(GAME_HEIGTH/space_size)-1) * space_size

    self.coordinates = [x,y]

    canvas.create_oval(x,y,x + space_size, y + space_size, fill = food_color, tag = "food")


def next_turn(snake, food,food2):
  x,y = snake.coordinates[0]
  if direction == "up":
    y -= space_size
  elif direction == "down":
    y += space_size
  elif direction == "left":
    x -= space_size
  elif direction == "right":
    x += space_size

  if x > GAME_WIDTH:
    x = 0
  if x < 0:
    x = GAME_WIDTH

  if y > GAME_HEIGTH:
    y = 0
  if y < 0:
    y = GAME_HEIGTH

  snake.coordinates.insert(0, (x,y))
  square = canvas.create_rectangle(x,y,x + space_size,y + space_size, fill = snake_color)
  snake.squares.insert(0, square)


  if x == food.coordinates[0] and y == food.coordinates[1] or x == food2.coordinates[0] and y == food2.coordinates[1] :
    global score,SPEED

    score += 1 
    if SPEED > 100:
      SPEED -= 20

    label.config(text = f"Score: {score}")

    canvas.delete("food")

    food = Food()
    food2 = Food()
  else:

    del snake.coordinates[-1]

    canvas.delete(snake.squares[-1])

    del snake.squares[-1]

  if check_collisions(snake):
    game_over()

  else:
    window.after(SPEED, next_turn,snake, food,food2)



def change_direction(new_direction):
  global direction
  if new_direction == "left":
    if direction != "right":
      direction = new_direction

  elif new_direction == "right":
    if direction != "left":
      direction = new_direction

  elif new_direction == "up":
    if direction != "down":
      direction = new_direction

  elif new_direction == "down":
    if direction != "up":
      direction = new_direction

def check_collisions(snake):
  x, y = snake.coordinates[0]

  # if x < 0 or x >= GAME_WIDTH:
  #   return True
  # elif y < 0 or y >= GAME_HEIGTH:
  #   return True
  
  for body_part in snake.coordinates[1:]:
    if x == body_part[0] and y == body_part[1]:
      print("game over")
      return True
  
  return False

def game_over():
  canvas.delete(ALL)

  canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font = ("Courier New", 70), text = "GAME OVER", fill = "red", tag = "Game Over")

window = Tk()
window.title("snake game")
window.resizable(False,False)

score = 0
direction = "down"

label = Label(window, text = f"Score:{score}", font = ("Courier New",40))
label.pack()

canvas = Canvas(window, bg = background_color, height = GAME_HEIGTH, width = GAME_WIDTH)
canvas.pack()




window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>",lambda event: change_direction("down"))


snake = Snake()
food = Food()
food2 = Food()

next_turn(snake, food, food2)





window.mainloop()