from turtle import *
from random import randint

jim = Turtle()
jim.color('medium spring green')

john = Turtle()
john.color('dark violet')

joe = Turtle()
joe.color('gold')

gerald = Turtle()
gerald.color('tomato')

turt = [jim, john, joe, gerald]
turtnames = ['Jim', 'John', 'Joe', 'Gerald']

for i in turt:
    i.shape('turtle')
    i.speed('fastest')
    i.penup()
    i.goto(-200, (turt.index(i) * 50) + 100)
    i.pendown()
    i.speed('normal')

for movement in range(100):
    for i in turt:
        i.forward(randint(1,5))

winner = None

for i in turt:
    print(turtnames[turt.index(i)] + " : " + str(i.pos()[0]))
    if winner == None or turt[winner].pos()[0] < i.pos()[0]:
        winner = turt.index(i)

print("The winner is " + turtnames[winner] + "!")

input("Press enter on terminal window to exit")