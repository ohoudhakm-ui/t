import math
from turtle import*
def rosea(k):
    return 15*math.sin(k)**3
def roseb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(1000000)
bgcolor("pink")
for i in range(6000):
    goto(rosea(i)*20,roseb(i)*20)
    for j in range(5):
        color("#f73487")
        goto(0,0)
done()