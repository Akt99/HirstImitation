import colorgram
import turtle as tm
import random as r
#below code to extract all the colors from IMG.jpg file and put all the color combinations into a list(rgb_colors)
#rgb_colors=[]
#colors=colorgram.extract('IMG.jpg',30)
#for color in colors:
 #   r= color.rgb.r
 #   g= color.rgb.g
 #   b= color.rgb.b
 #   new_color=(r,g,b)
 #   rgb_colors.append(new_color)

#print (rgb_colors)
tt=tm.Turtle()
tm.colormode(255)
tt.speed("fastest")
tt.penup()
tt.hideturtle()
color_list=[(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 238), (145, 28, 66), (230, 237, 232), (239, 75, 36), (7, 148, 95), (222, 170, 45), (183, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92), (244, 219, 53), (178, 40, 98), (40, 168, 117), (208, 131, 165), (205, 56, 35), (239, 162, 194), (147, 26, 24), (242, 168, 158), (162, 211, 178), (140, 211, 232), (7, 115, 55), (26, 186, 225), (84, 133, 177), (163, 193, 227), (112, 9, 8)]#obtained by printing the rgb_colors earlier in the commented code
tt.setheading(218)
tt.forward(300)
tt.setheading(0)
num_of_dots=100
for dot_count in range(1, num_of_dots+1):
    tt.dot(20, r.choice(color_list))
    tt.forward(50)
    if dot_count%10==0:
        tt.setheading(90)
        tt.forward(50)
        tt.setheading(180)
        tt.forward(500)
        tt.setheading(0)

screen=tm.Screen()
screen.exitonclick()