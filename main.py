import turtle as t
import random

thi = t.Turtle(shape = "turtle", visible = False)
thi.speed("fastest")

directions = [0, 90, 180, 270]
t.colormode(255)

# Gerar número de lados do polígono
n = random.randint(3,13)

# Calcular ângulo externo do polígono
a = 360/n

# Mudando a posição inicial do thi
thi.penup()
for i in range(2):
    thi.left(90)
    thi.forward(100)
thi.showturtle()
thi.pendown()

thi.pensize(5)

def main():
  for i in range (20):
      draw_poligon(n, a)
      thi.forward(50)
      thi.setheading(random.choice(directions))
      thi.forward(50)
      n = random.randint(3, 13)
      a = 360 / n

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_poligon(n, a):
    for side in range(n):
        # Escolhendo cor para o lado
        thi.color(random_color())
        thi.forward(25)
        thi.right(a)
      
main()

screen = t.Screen()
screen.exitonclick()
