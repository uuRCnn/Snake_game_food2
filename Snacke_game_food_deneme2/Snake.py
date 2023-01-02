from turtle import Screen
import turtle as t
import random
import time


UP = 90
DOWN = 270
LEFT = 180
RİGHT = 0
STARTİNG_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTENCE = 20


class Snake:

    def __init__(self):

        self.segments = []  # a-b-c
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTİNG_POSITION:
                new_segment = t.Turtle(shape="square")
                new_segment.color("white")
                new_segment.penup()
                new_segment.goto(position)
                self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTENCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RİGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RİGHT)

