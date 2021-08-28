import time
import sys
import os
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import pygame
import random
from tkinter import *



print("Donut Emulator Version 1.0 'Thunderbolt' (12/7/21). Welcome to Donut Emulator.")
time.sleep(0.05)

invalid_input = True


def main():
    start = input("user@donut:-$ ")
    
    if start == "calculator":
        num1 = float(input("Enter your first number: "))

        op = input("Enter your operator: ")

        num2 = float(input("Enter your second number: "))

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "*":
            print(num1 * num2)
        else:
            print("Invalid operator!")

    elif start == "change path":
        path = input("Enter your new path string: ")
        os.chdir(path)
        invalid_input = False

    elif start == "cp path":
        print(os.getcwd())
        invalid_input = False

    elif start == "create doc-python":
        def createPythonDoc():

            PythonDoc = open("doc.py", "w")
            PythonDoc.write("")

            PythonDoc.close
            invalid_input = False

    elif start == "exit":
        sys.exit()
        invalid_input = False

    elif start == "fahrenheit to celcius":
        lower = 0
        upper = 300
        step = 20

        fahr = lower
        while(fahr <= upper):
            celcius = (5.0/9.0) * (fahr-32.0)
            print(fahr, celcius)
            fahr = fahr + step
        invalid_input = False

    elif start == "games":
        print("snake - type in 'play snake' to play.")
        invalid_input = False

    elif start == "help":
        print("Donut Emulator Version 1.0 'Thunderbolt'.")
        print("This is a default shell command. Type `help' to see this list.")
        print("For more information, visit https://netfruittechnologies.wordpress.com/donut-emulator/.")
        print("calculator - opens up the calculator.")
        print("change path - Changes your path")
        print("cp path - Views your current Python path.")
        print("create doc-python - Creates a Python Document.")
        print("exit - Exits the terminal.")
        print("fahrenheit to celcius - Converts Fahrenheit temperatures from 0 to 300 degrees into Celcius temperatures")
        print("games - views a list of games to play.")
        print("help - Display help.")
        print("play snake - Launches a snake game")
        print("sample form - Prints out a sample form.")
        print("sys info - Displays system information.")
        print("term info - Displays terminal information.")
        print("timer - Sets a timer.")
        invalid_input = False
    
    elif start == "play snake":
        pygame.init()


        white = (255, 255, 255)
        yellow = (255, 255, 102)
        black = (0, 0, 0)
        red = (216, 50, 80)
        green = (0, 255, 0)
        blue = (100, 153, 213)

        dis_width = 1000
        dis_height = 600

        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game by Rayyan Taha Copied For Some')

        clock = pygame.time.Clock()

        snake_block = 10
        snake_speed = 7

        font_style = pygame.font.SysFont("snellroundhand", 45)
        score_font = pygame.font.SysFont("comicsansms", 35)


        def Your_score(score):
            value = score_font.render("Score: " + str(score), True, black)
            dis.blit(value, [0, 0])


        def our_snake(snake_block, snake_list):
            for x in snake_list:
                pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])


        def gameLoop():
            game_over = False
            game_close = False

            x1 = dis_width / 2
            y1 = dis_height / 2

            x1_change = 0
            y1_change = 0

            snake_List = []
            Length_of_snake = 1

            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            while not game_over:

                while game_close == True:
                    dis.fill(green)
                    message("You Lose! Press C to Play Again or Q to Quit.", red)
                    Your_score(Length_of_snake - 1)
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                            if event.key == pygame.K_c:
                                gameLoop()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0

                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(green)
                pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]

                for x in snake_List[:-1]:
                    if x == snake_Head:
                        game_close = True

                our_snake(snake_block, snake_List)
                Your_score(Length_of_snake - 1)

                pygame.display.update()

                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(
                        0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(
                        0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1

                clock.tick(snake_speed)

            pygame.quit()
            


        gameLoop()

        invalid_input = False

    elif start == "sample form":

        root = Tk()


        entry1 = Entry(root, width=50, borderwidth=5)
        entry1.grid(row=0, column=0)
        entry1.insert(0, "First Name")

        entry2 = Entry(root, width=50, borderwidth=5)
        entry2.grid(row=1, column=0)
        entry2.insert(0, "Last Name")

        entry3 = Entry(root, width=50, borderwidth=5)
        entry3.grid(row=2, column=0)
        entry3.insert(0, "Email")


        def execution():
            entries = entry1.get()
            entries2 = entry2.get()
            entries3 = entry3.get()
            label = Label(root, text=entries)
            label.grid(row=4, column=0)
            label2 = Label(root, text=entries2)
            label2.grid(row=5, column=0)
            label3 = Label(root, text=entries3)
            label3.grid(row=6, column=0)


        button = Button(root, text="Enter", command=execution)
        button.grid(row=3, column=0)


        root.mainloop()
    
    elif start == "sys info":
        print('System info:', platform.system())
        invalid_input = False

    elif start == "term info":
        print("Donut Emulator Version 1.0 'Thunderbolt'. Date: 12/7/21")
        invalid_input = False

    elif start == "timer":
        def countdown(t):
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
            print('Blast Off!!!')
        t = input("Enter the time in seconds: ")
        countdown(int(t))
        invalid_input = False
    
    elif start == "":
        pass

    else:
        print("donutshell: {}".format((start)),": command is not recognized.")


while invalid_input:  # this will loop until invalid_input is set to be True
    main()
