from turtle import Turtle, Screen
import time


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self) -> None:
        self.body = []
        self.y = 0
        self.create_snake()
        self.head = self.body[0]        
    
    def create_snake(self):
        for i in range(3):
            segment_1 = Turtle("square")
            segment_1.color("white")
            segment_1.penup()
            segment_1.goto(self.y, 0)
            self.y -= 20
            self.body.append(segment_1)

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            x = self.body[i-1].xcor()
            y = self.body[i-1].ycor()
            self.body[i].goto(x, y)
        self.body[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def add_segment(self, position):
            segment_1 = Turtle("square")
            segment_1.color("white")
            segment_1.penup()
            segment_1.goto(position)
            self.body.append(segment_1)
        
    def extend(self):
        self.add_segment(self.body[-1].position()) 