# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:28:12 2024

@author: CDSchaufelberger
"""
from tabulate import tabulate
import random  #use random.choice([-1,1])
import time
 

def onedim(moves):
    count = 0
    x = 0 #origin 
    for i in range(moves):
       direction = random.choice(["left","right"])
       if direction=="right":
           x+=1
       elif direction == "left":
           x-=1
       if x == 0:
           count += 1
           break 
    return count
#append percentage of times after running it 100 times 

def twodim(moves):
    count = 0 
    x = 0 
    y = 0 
    for i in range(moves):
        direction = random.choice(["left","right","up","down"]) #up down (y) 
        if direction == "right":
            x+=1
        elif direction == "left":
            x-=1
        if direction == "up":
            y+=1
        elif direction == "down":
            y-=1 
        if x == 0 and y == 0:
            count += 1
            break
    return count

def threedim(moves):
    count = 0
    x = 0
    y = 0
    z = 0
    for i in range(moves):
        direction = random.choice(["left","right","up","down","in","out"]) # in, out (z)
        if direction == "right":
            x+=1
        elif direction == "left":
            x-=1
        if direction == "up":
            y+=1
        elif direction == "down":
            y-=1
        if direction == "in":
            z+=1 
        elif direction == "out":
            z-=1 
        if x == 0 and y == 0 and z == 0:
            count += 1
            break
    return count 

def main():
    steps = [20,200,2000,20000,200000,2000000]
    finalvalues1 = ["1D"]
    finalvalues2 = ["2D"]
    finalvalues3 = ["3D"]
    timevalues3 = ["3D"]
    
    for move in steps:
        finalcount = 0 
        for i in range(100):
            finalcount += onedim(move)
        finalvalues1.append(finalcount)
        
    for move in steps:
        finalcount = 0
        for i in range(100):
            finalcount += twodim(move)
        finalvalues2.append(finalcount)
        
    for move in steps:
        finalcount = 0 
        start_time = time.time()
        for i in range(100):
            finalcount += threedim(move)
        finalvalues3.append(finalcount)
        end_time = time.time()
        elapsed_time = end_time - start_time
        timevalues3.append(elapsed_time)
        
        #return onedim(20, 100)
       # print()
   #     onedim(moves)
   #nested for loop 
        
        # do this for two and three 
        #start time and end time for results one two and three
        
    data = [
        finalvalues1, 
        finalvalues2,
        finalvalues3,
        ["Run Time(s):"],
        timevalues3
    ]
    
    # Table headers
    # header1 = ["Percentage of time particle returned to origin:"]
    header = ["Number of steps:","20", "200", "2000", "20000", "200000", "2000000"]
    
    # Use the tabulate function to format the data into a table
    table = tabulate(data, header)
    #, tablefmt="grid")
    
    # Print the formatted table
    print(table)
    

main()


    

        
        
           


       
        
  