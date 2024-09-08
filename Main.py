from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard




screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on=True

while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)<15:
        score.score_update()
        snake.extend()
        food.refresh()
        
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        game_is_on=False
        score.game_end()

    if snake.detect_self_collision() == True:
        game_is_on=False
        score.game_end()


    
 
screen.exitonclick()