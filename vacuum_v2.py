from turtle import Turtle, Screen
from random import choice
from time import sleep
from queue import SimpleQueue


w: int
w, h = (853, 480)
wn = Screen()
wn.screensize(w, h)
wn.bgcolor("#d3d3d3")

Room_state = {"Clean": "#FFFFFF",
              "Dirty": "#b5651d"}

cleaned = 0

def filler(t, color, delay=0, vacclean = False):
    global cleaned
    t.fillcolor(color)
    t.penup()
    if color == Room_state['Clean']:
        sleep(delay) #To avoid instant cleaning
        if vacclean:
            cleaned += 1
    t.begin_fill()
    t.circle(130)
    t.end_fill()


def setup():
    A = Turtle() # Draws Circle in A
    B = Turtle() # Draws Circle in B
    X = Turtle() # Text Below A
    Y = Turtle() # Text Below B

    A.ht()
    B.ht()
    X.ht()
    Y.ht()

    A.speed(100)
    B.speed(100)
    X.speed(100)
    Y.speed(100)

    A.penup()
    B.penup()
    X.penup()
    Y.penup()

    A.setpos(-w / 4, -120)
    B.setpos(w / 4, -120)
    X.setpos(-w / 4, -200)
    Y.setpos(w / 4, -200)

    A.pendown()
    B.pendown()

    filler(A, Room_state['Clean'], False)
    filler(B, Room_state['Clean'], False)

    # Creates rooms and boundary
    t1 = Turtle()
    t1.ht()
    t1.speed(20)
    t1.penup()
    t1.setposition(w / 2, h / 2)
    t1.pendown()
    t1.pensize(10)
    t1.right(90)
    t1.forward(h)
    t1.right(90)
    t1.forward(w)
    t1.right(90)
    t1.forward(h)
    t1.right(90)
    t1.forward(w)
    t1.backward(w / 2)
    t1.right(90)
    t1.pensize(5)
    t1.forward(h - 90)
    t1.penup()
    t1.setpos(-w / 4, h / 2 - 70)
    t1.write("Room A", align="center", font=("Arial", 20, "normal"))
    t1.setpos(w / 4, h / 2 - 70)
    t1.write("Room B", align="center", font=("Arial", 20, "normal"))

    return A, B, X, Y


A, B, X, Y = setup()

# Vaccum Cleaner
C = Turtle()
C.speed(8)
C.penup()
C.shape("circle")
C.setpos(A.xcor(), A.ycor() + 130)

count = 1
iter = Turtle()
cleanwriter = Turtle()
iter.ht()
cleanwriter.ht()
iter.penup()
cleanwriter.penup()
iter.setpos(0, -h / 2 + 50)
cleanwriter.setpos(0, -h / 2 + 20)

room_state = list(Room_state.keys())

state = SimpleQueue()
state.put_nowait(((choice(room_state)), choice(room_state)))


while True:
    iter.clear()
    cleanwriter.clear()
    iter.write("Iteration : " + str(count), align="center", font=("Arial", 16, "normal"))
    cleanwriter.write("Times Cleaned : " + str(cleaned), align="center", font=("Arial", 16, "normal"))

    condition = state.get_nowait()
    stateA = condition[0]
    stateB = condition[1]

    X.clear()
    Y.clear()

    nextA = choice(room_state)
    nextB = choice(room_state)

    state.put_nowait((nextA, nextB))

    filler(A, Room_state[stateA])
    filler(B, Room_state[stateB])

    X.write("Now : " + stateA + "\nNext : " + nextA, align="center", font=("Arial", 16, "normal"))
    Y.write("Now : " + stateB + "\nNext : " + nextB, align="center", font=("Arial", 16, "normal"))

    print("\nA : " + stateA, "\tB : " + stateB)

    if stateA == 'Dirty' and stateB == 'Dirty':
        if C.xcor() < 0:
            print("Both Dirty, Cleaned A going to B")
            # noinspection PyTypeChecker
            filler(A, Room_state['Clean'], 0.5, True)
            stateA = 'Clean'
            C.setpos(B.xcor(), B.ycor() + 130)
            # noinspection PyTypeChecker
            filler(B, Room_state['Clean'], 0.5, True)
            stateB = 'Clean'

        elif C.xcor() > 0:
            print("Both Dirty, Cleaned B going to A")
            # noinspection PyTypeChecker
            filler(B, Room_state['Clean'], 0.5, True)
            stateB = 'Clean'
            C.setpos(A.xcor(), A.ycor() + 130)
            # noinspection PyTypeChecker
            filler(A, Room_state['Clean'], 0.5, True)
            stateA = 'Clean'

    if stateA == 'Dirty':
        print("Cleaned A")
        C.goto(A.xcor(), A.ycor() + 130)
        # noinspection PyTypeChecker
        filler(A, Room_state['Clean'], 0.3, True)

    elif stateB == 'Dirty':
        print("Cleaned B")
        C.goto(B.xcor(), B.ycor() + 130)
        # noinspection PyTypeChecker
        filler(B, Room_state['Clean'], 0.3, True)

    count += 1
    sleep(0.5)