import turtle
import pandas


# Screen setup
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
while is_game_on:

# User input
    guess = screen.textinput(f" {score} /{len(states)} states", prompt="Enter a US State").title()



    if guess in states:
        state_data = data[data.state == guess]
        x = int(state_data.x.item())
        y = int(state_data.y.item())
        score+=1
        guessed_state.append(guess)
        writer.goto(x, y)
        writer.write(guess, align="center", font=("Arial", 8, "normal"))
    else:
        if guess == "Exit" or guess not in states:
            is_game_on = False
            missing_states=[]
            for state in states:
                if state not in guessed_state:
                    missing_states.append(state)
            missing_data=pandas.DataFrame(missing_states)
            missing_data.to_csv("states_to_learn.csv")









