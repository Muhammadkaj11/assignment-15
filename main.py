import turtle


screen = turtle.Screen()
screen.bgcolor("red")  


square_turtle = turtle.Turtle()
square_turtle.shape("turtle")  
square_turtle.color("blue")    
square_turtle.speed(2)         


def draw_square(size):
    for _ in range(4):  
        square_turtle.forward(size)  
        square_turtle.left(90)       
draw_square(100)  


square_turtle.hideturtle()


screen.exitonclick()
