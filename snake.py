from turtle import Turtle


starting_positions=[(0,0),(-20,0),(-40,0)]
move_distance=20
class Snake:
    def __init__(self):
        
        self.segments=[]
        self.create_snake()
    
    def create_snake(self):
        for i in starting_positions:
            new_turtle=Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(i)
            self.segments.append(new_turtle)
    
    def move(self):
        for s in range(len(self.segments)-1,0,-1):
            new_x=self.segments[s-1].xcor()
            new_y=self.segments[s-1].ycor()
            self.segments[s].goto(new_x,new_y)
        self.segments[0].forward(move_distance)
    
    def extend(self):
         new_turtle=Turtle("square")
         new_turtle.color("white")
         new_turtle.penup()
         new_turtle.goto(self.segments[-1].xcor(),self.segments[-1].ycor())
         self.segments.append(new_turtle)

    def detect_self_collision(self):
        for i in self.segments[1:]:
            if self.segments[0].distance(i)<10:
                self.status=True
                return self.status
                

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


    
        