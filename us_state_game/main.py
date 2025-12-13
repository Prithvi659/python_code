import turtle
import pandas


screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Data
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
# Turtle for writing state names
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
is_game_on = True
score=0
guessed_state=[]
chance=0
while is_game_on:

# User input
    guess = screen.textinput(f" {score} /{len(states)} states | {chance}/5", prompt="Enter a US State")

    if guess is None:
        break
    guess=guess.title()

    if guess == "Exit":
       break


    if guess in guessed_state:
        continue

    if guess in states:
        state_data = data[data.state == guess]
        x = int(state_data.x.item())
        y = int(state_data.y.item())
        score+=1
        guessed_state.append(guess)
        writer.goto(x, y)
        writer.write(guess, align="center", font=("Arial", 8, "normal"))
    else:
        chance+=1
        if chance >= 5:
            is_game_on = False




missing_states = [state for state in states if state not in guessed_state]
missing_data = pandas.DataFrame(missing_states)
missing_data.to_csv("states_to_learn.csv", index=False)








