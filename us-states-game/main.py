from turtle import Turtle, Screen
import pandas as pd

states = pd.read_csv("50_states.csv")
image = "blank_states_img.gif"

s = Screen()
s.title("U.S. States Game")
s.addshape(image)

bg_image = Turtle()
bg_image.shape(image)

writer = Turtle(visible=False)
writer.penup()

#def get_coords(x, y):
#    print(x, y)
#
#s.onscreenclick(get_coords)

states_list = states.state.to_list()
total = len(states_list)
correct_states = []

state_answer = s.textinput(title=f"({len(correct_states)}/{total})", prompt="What's a state's name?").title()

while len(states_list) > 0:

    if state_answer == "Exit":
        pd.DataFrame(states_list).to_csv("missed_states.csv")
        break

    if state_answer in states_list:
        correct_states.append(state_answer)
        states_list.remove(state_answer)

        state = states[states.state == state_answer].state.item()
        x = states[states.state == state_answer].x.item()
        y = states[states.state == state_answer].y.item()

        writer.goto(x, y)
        writer.write(state, align="left", font=("Arial", 8, "normal"))

    state_answer = s.textinput(title=f"({len(correct_states)}/{total})", prompt="What's another state's name?").title()
