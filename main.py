import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
position = turtle.Turtle()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

game_is_on = True
number = 0

while game_is_on:
    answer_state = (screen.textinput(f"{number}/50 Guess the state", "What's another state name? ")).title()
    guessed_states = []

    for state in states_list:
        coordinates = data[data.state == state]
        x_cord = int(coordinates.x.iloc[0])
        y_cord = int(coordinates.y.iloc[0])

        if answer_state == "Exit":
            game_is_on = False

        elif state == answer_state:
            position.hideturtle()
            position.penup()
            position.goto(x_cord, y_cord)
            position.write(f"{state}")
            number += 1
            guessed_states.append(state)

