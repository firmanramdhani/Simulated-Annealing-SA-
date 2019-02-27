import random
import math


x1=random.uniform(-10,10)
y1=random.uniform(-10,10)
cr=0.9999
t0=1000000
tmin=1
rand=random.uniform(0,1)

def f(x1,x2):
    return (-1*(abs(math.sin(x1)*math.cos(x2)*math.exp(abs(1-((math.sqrt(pow(x1,2) + pow(x2,2))/math.pi)))))))


#Current State

currentState = f(x1,y1)

while (t0>tmin):
    x2 = (random.uniform(-10, 10))
    y2 = (random.uniform(-10, 10))
 
   
    #New StateS

    newState = f(x2,y2)
    
    if (newState >= currentState):
         if (math.exp((currentState - newState)/t0)> rand):
            currentState = newState
            x1hasil = x2
            x2hasil = y2
    else:
        currentState = newState
        x1hasil=x2
        x2hasil=y2
    t0=t0*cr


print("X1 Minimun       = ",x1hasil)
print("X2 Minimun       = ",x2hasil)
print("Nilai Minimun    = ",currentState)
