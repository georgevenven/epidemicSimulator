import pygame
import constants
import people 
import stats 
import random

def initialization(n, s, i, r, l, d, ):
    # n is number of people, s is number of safe, i is number of infected
    # r is the transmission rate, l is length of infection, d is death rate

    ppl = list()

    #the creation of safe people
    for n in range(n - i): 
        vectorX = random.randint(-3,3)
        vectorY = random.randint(-3,3)

        X = random.randint(50,750)
        Y = random.randint(50,750)

        ppl.append(people.Person(constants.WHITE, X, Y, vectorY, vectorX)) # should add a person to the list of people 

    #the creation of infected people 
    for n in range(i):
        vectorX = random.randint(-3,3)
        vectorY = random.randint(-3,3)

        X = random.randint(50,750)
        Y = random.randint(50,750)

        ppl.append(people.Person(constants.YELLOW, X, Y, vectorY, vectorX))

    return ppl 

def main():
    pygame.init()

    screen = pygame.display.set_mode((800,800))
    clock = pygame.time.Clock()

    on = True

    ppl = initialization(35, 30, 5, .10, 14, .02)
    
    infected = list() 

    while on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

        screen.fill(constants.BLACK)

        length = len(ppl)
    
        for i in range(length):
            temp = ppl[i]
            ppl[i].rect = pygame.draw.rect(screen, temp.state, (temp.x, temp.y, 8, 8), 8)
            
        infected = people.updatePersons(ppl, screen, infected)
        pygame.display.flip()
        clock.tick(60)
        stats.cycle+=1 # 300 cycles = day? 
        #print(stats.cycle)

main()