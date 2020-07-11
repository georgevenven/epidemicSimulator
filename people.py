#state is the state of its aliveness, white is safe, yellow is sick, and red is dead
import random 
import pygame
import constants

class Person():
  
    def __init__(self, s, X , Y, vectory, vectorx):
        self.state = s
        self.x = X
        self.y = Y
        self.vectorX = vectorx
        self.vectorY = vectory
        self.rect = 0 

# updates all the peoples states 
def updatePersons(ppl, screen, infected):
    
    length = len(ppl)

    for i in range(length):

        if ppl[i].x <= 20 or ppl[i].x >= 780 or ppl[i].y <= 20 or ppl[i].y >= 780:
            ppl[i].vectorX = random.randint(-3,3)
            ppl[i].vectorY = random.randint(-3,3)

        
        ppl[i].x += ppl[i].vectorX
        ppl[i].y += ppl[i].vectorY

    # a list of infected people is returned 

    temp = list()

    for i in range(length):
        temp = ppl[i].rect.collidelistall(ppl)

    length = len(temp)

    for i in range(length):
        ppl[temp[i]].state = constants.YELLOW
        temp.append(ppl[temp[i]])

    infected = temp + infected 

    return infected 

