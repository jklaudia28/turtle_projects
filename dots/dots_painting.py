# import colorgram
#
# colors = colorgram.extract('dots.png', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print (rgb_colors)


import random
import turtle as t

from turtle import Screen

t.colormode(255)
my_screen = Screen()
tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")

color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40),
 (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91),
 (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12),
 (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

tim.penup()
tim.setheading(225)
tim.forward(200)
tim.setheading(0)

def raws():
    for _ in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(40)

def draw():
    for _ in range (10):
        raws()
        tim.back(400)
        tim.left(90)
        tim.forward(40)
        tim.right(90)

draw()
my_screen.exitonclick()