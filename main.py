from turtle import Turtle as Turt, Screen
import random
from snake import Snake
from movement import Movement as mv
from GameBoundary import GameBoundary as gb
from Food import Food
from scorecard import Scoreboard
import time


screen = Screen()
screen.setup(width=600,height=600)
food = Food()
screen.bgcolor("black")
screen.title("Snake Classic")
screen.tracer(0)

make_bound = gb()
make_bound.draw_boundary()

#Instance of Snake Class
snake = Snake()

#Instance of scorecard
scoreboard = Scoreboard()

#initialize the movment class as first block or block 0
move_1 = mv(snake.head())

screen.listen()
screen.onkeypress(fun=move_1.move_up,key="Up")
screen.onkeypress(fun=move_1.move_down,key="Down")
screen.onkeypress(fun=move_1.move_left,key="Left")
screen.onkeypress(fun=move_1.move_right,key="Right")

is_game = True

while is_game:
    snake.move()

    if snake.head().distance(food.food) < 15:
        food.food_spawn()
        snake.grow()
        scoreboard.increase_score()

    for segment in snake.segments[1: ]:
        if snake.head().distance(segment) < 10:
            is_game = False
            scoreboard.game_over()
            print("Game Over! You ate yourself up!")

    if make_bound.boundary_coll(snake.head()):
        is_game = False
        scoreboard.game_over()
        print("Game Over!,Collision Detected!")

    screen.update()
    time.sleep(0.1)

screen.exitonclick()

