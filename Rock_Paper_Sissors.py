from microbit import *
import random

rock_img = Image("00900:"
                 "09990:"
                 "09990:"
                 "09990:"
                 "00900")

paper_img = Image("99999:"
                  "90009:"
                  "90009:"
                  "90009:"
                  "99999")

scissors_img = Image("90009:"
                     "09090:"
                     "00900:"
                     "09090:"
                     "90009")


choices = [rock_img, paper_img, scissors_img]
names = ["Rock", "Paper", "Scissors"] # optional, if you want to debug or print via serial
index = 0


display.show(choices[index])

while True:
    if button_a.was_pressed():
        index = (index + 1) % len(choices)
        display.show(choices[index])
    
    if button_b.was_pressed():
        user_img = choices[index]
        comp_index = random.randrange(len(choices))
        comp_img = choices[comp_index]
        
        display.show(Image.SQUARE_SMALL)
        sleep(500)
        
        display.show(comp_img)
        sleep(1000)
       
        if comp_index == index:
            for _ in range(2):
                display.show(user_img)
                sleep(300)
                display.clear()
                sleep(300)
        elif (index == 0 and comp_index == 2) or \
             (index == 1 and comp_index == 0) or \
             (index == 2 and comp_index == 1):
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)
        
        sleep(1000)
        
        index = 0
        display.show(choices[index])
    
    sleep(100)

