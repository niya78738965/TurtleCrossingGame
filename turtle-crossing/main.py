import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
cars=CarManager()
level=Scoreboard()
screen.listen()
screen.onkey(player.move_forward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    #if turtle collide with any car
    for car in cars.all_cars:
       if car.distance(player)<20:
          game_is_on = False
          level.game_over()

    #if turtle reach finish line
    if player.turtle_finish():
        player.go_to_start()
        cars.increase_speed()
        level.level_up()

screen.exitonclick()
