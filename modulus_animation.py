import time 
import os

repeats = 5
steps_per_second = 10


for i in range(11 * repeats):
    os.system("cls")

    if i % 11 == 0:
        print(" -^--------- ")
    elif i % 11 == 1:
        print(" --^--------- ")
    elif i % 11 == 2:
        print(" ---^-------- ")
    elif i % 11 == 3:
        print(" ----^------- ")
    elif i % 11 == 4:
        print(" -----^------ ")
    elif i % 11 == 5:
        print(" ------^------ ")
    elif i % 11 == 6:
        print(" -------^----- ")
    elif i % 11 == 7:
        print(" --------^---- ")
    elif i % 11 == 8:
        print(" ---------^--- ")
    elif i % 11 == 9:
        print(" ----------^-- ")
    elif i % 11 == 10:
        print(" -----------^- ")
      
    
    time.sleep(1/steps_per_second)
