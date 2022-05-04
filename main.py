import turtle
import pandas
from score import Score
screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = Score()
data = pandas.read_csv("50_states.csv")
state = data.state
state_list = []
for names in state:
    state_list.append(names)

true_answer_list = []
left_states = []
while len(true_answer_list) < 50:
    screen.tracer(0)
    answer_state = screen.textinput(title=f"{len(true_answer_list)}/50 States", prompt="What is another state's name?").title()

    if answer_state in state_list:
        true_answer_list.append(answer_state)
        score.increase_score()
        x_value = int(data[state == answer_state].x)
        y_value = int(data[state == answer_state].y)
        screen.update()
        turtle.goto(x_value, y_value)
        turtle.write(f"{answer_state}", align= "center", font=("Arial", 10, "normal"))
        turtle.goto(0,0)

    if answer_state == "Exit":
        break
for names in state_list:
    if names not in true_answer_list :
        left_states.append(names)

df = pandas.DataFrame(left_states)
df.to_csv("missing_states.csv")
screen = turtle.Screen()
turtle.write(f"These states : {df} are still to learn")

screen.exitonclick()


