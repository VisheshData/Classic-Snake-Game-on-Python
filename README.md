# Classic Snake Game 🐍
A classic Snake Game built using Python and the turtle graphics library. This project is a fun way to practice object-oriented programming (OOP) concepts, including classes, inheritance, and event-driven programming.

## Description
This repository contains a simple, interactive Snake Game where the player controls the snake to collect food and grow in length. The game ends when the snake hits the wall or collides with itself. The player's score is displayed at the top of the game window.

## Features
A dynamic snake that moves and grows as it consumes food.
Randomly generated food that spawns at new locations each time the snake eats.
Scoreboard that keeps track of the player's score.
Game over functionality when the snake hits the wall or itself.
## Technologies Used
Python 3.x
Turtle Module (for GUI graphics and game movement)
OOP (Object-Oriented Programming)
## How to Run
Clone the repository.
Run The Main.py file

## Game Instructions
Use the arrow keys to move the snake.
Up Arrow → Move Up
Down Arrow → Move Down
Right Arrow → Move Right
Left Arrow → Move Left
The snake will automatically move in the direction of the last key pressed.
The game ends when the snake hits the walls or collides with its own body.
Every time the snake eats food, it grows in length and the score increases by 10 points.
## Programming Concepts
### 1. Object-Oriented Programming (OOP)
Encapsulation: The Snake, Food, and Scoreboard are modeled as separate classes with their own methods and properties.
Inheritance: The Food and Scoreboard classes inherit from the Turtle class in Python’s turtle module to reuse its graphics-related methods. Class inheritance concept used.
### 2. Turtle Graphics
The game is built using Python’s turtle module, which provides a way to draw and move objects on the screen. The turtle objects are controlled to create the snake, food, and scoreboard elements.
### 3. Event-Driven Programming
The program listens for keypresses (Up, Down, Right, Left) to control the movement of the snake. This is handled using the screen.listen() and screen.onkey() methods.
### 4. Collision Detection
The program checks for collisions between the snake and the wall or itself by comparing the position of the snake’s head with either the screen boundaries or the positions of its body segments.
## Files Overview
1. main.py
The entry point for the game. This file handles the main game loop, user input, and collision detection.

```python

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Check for food collision
    if snake.segments[0].distance(food) < 15:
        score.score_update()
        snake.extend()
        food.refresh()
    # Check for wall collision
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        score.game_end()
    # Check for self-collision
    if snake.detect_self_collision():
        game_is_on = False
        score.game_end()
```
A screen size of 600x600 px is created. So Taking the playing area 280x280 px within which snake can move freely.

2. snake.py
Defines the Snake class that manages the behavior of the snake (movement, growing, and detecting collisions).

```python

class Snake:
    def move(self):
        for s in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[s-1].xcor()
            new_y = self.segments[s-1].ycor()
            self.segments[s].goto(new_x, new_y)
        self.segments[0].forward(move_distance)
```
3. food.py
Defines the Food class, which randomly places food on the screen for the snake to consume.

```python
class Food(Turtle):
    def refresh(self):
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 270)
        self.goto(rand_x, rand_y)
```
4. scoreboard.py
Defines the Scoreboard class, which displays and updates the player's score and shows a "Game Over" message when the game ends.

```python

class Scoreboard(Turtle):
    def score_update(self):
        self.score += 10
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
```
Contributing
Contributions are welcome! If you find any bugs or have feature suggestions, please create an issue or submit a pull request.
