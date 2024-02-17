from math import *
from numpy import *
import time
import sys
import os
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import pygame
import random
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from itertools import repeat
import time as t
from time import strftime
from tkinter import Tk
import turtle
from pyperclip import *
from tkcalendar import *
from segno import *
from os import *
from github import Github

pathdec = os.getcwd()

os.system("cls")

print("Donut Emulator Version 3.0 'Blitz'. Welcome to Donut Emulator.")

invalid_input = True

def main():

    pathdec = os.getcwd()

    start = input("user@donut:-$ ")

    if start == "bmi calc":

        root = Tk()

        root.title("BMI Calculator By @SmashedFrenzy16")

        root.geometry("600x400")

        def execute():

            global weight

            weight = float(weight_e.get())

        def execute2():

            global height

            height = float(height_e.get())

        def execute3():

            bmi = (weight/(pow(height, 2))) * 703

            blank_label2 = Label(root, text="")

            blank_label2.pack()

            result = Label(root, text=str(bmi))

            result.pack()

        title_label = Label(
                    root, fg="black", text="BMI Calculator", font=("Arial", 48))

        title_label.pack()

        blank_label = Label(root, text="")

        blank_label.pack()

        weight_e = Entry(root, width=100, borderwidth=5)

        weight_e.pack()

        weight_e.insert(0, "Enter in your weight (lb)")

        weight_button = Button(root, text="Enter", command=execute)

        weight_button.pack()

        height_e = Entry(root, width=100, borderwidth=5)

        height_e.pack()

        height_e.insert(0, "Enter in your height (in)")

        height_button = Button(root, text="Enter", command=execute2)

        height_button.pack()

        result_button = Button(root, text="Get Result", command=execute3)

        result_button.pack()

        root.mainloop()


    if start == "calc":

        class SciCalc:

            def __init__(self, master):

                self.master = master

                master.title("Scientific Calculator")

                self.total = StringVar()

                self.entry = Entry(
                    master, textvariable=self.total, borderwidth=5)
                self.entry.grid(row=0, column=0, columnspan=6, pady=6)

                self.button_creator()

            def button_creator(self):

                b_list = [
                    ['sin', 'cos', 'tan', '^2', '^3'],
                    ['log(x)', '1/x', 'x!', 'sqrt', 'cbrt'],
                    ['7', '8', '9', 'C', 'pi'],
                    ['4', '5', '6', '*', '/'],
                    ['1', '2', '3', '+', '-'],
                    ['0', '.', '10^x', 'e', '=']
                ]

                for i, row in enumerate(b_list):

                    for j, b_text in enumerate(row):

                        button = Button(self.master, text=b_text, width=5,
                                        height=3, command=lambda text=b_text: self.click(text))

                        button.grid(row=i + 1, column=j, sticky="nsew")

                    self.master.rowconfigure(i + 1, weight=1)
                self.master.columnconfigure(0, weight=1)
                self.master.columnconfigure(1, weight=1)
                self.master.columnconfigure(2, weight=1)
                self.master.columnconfigure(3, weight=1)
                self.master.columnconfigure(4, weight=1)
                self.master.columnconfigure(5, weight=1)

            def click(self, b_text):

                if b_text == '=':

                    try:

                        result = eval(self.entry.get())

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == 'C':

                    self.total.set("")

                elif b_text == 'sin':

                    try:

                        result = sin(radians(float(self.entry.get())))

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == 'cos':

                    try:

                        result = cos(radians(float(self.entry.get())))

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == 'tan':

                    try:

                        result = tan(radians(float(self.entry.get())))

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == '^2':

                    try:

                        result = float(self.entry.get()) ** 2

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == '^3':

                    try:

                        result = float(self.entry.get()) ** 3

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == 'log(x)':

                    try:

                        result = log(float(self.entry.get()))

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == '1/x':

                    try:

                        result = 1 / float(self.entry.get())

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == 'x!':

                    try:

                        result = factorial(int(self.entry.get()))

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == 'sqrt':

                    try:

                        result = sqrt(float(self.entry.get()))

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == 'cbrt':

                    try:

                        result = cbrt(float(self.entry.get()))

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == '10^x':

                    try:

                        result = 10 ** float(self.entry.get())

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == 'pi':

                    try:

                        result = pi

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                elif b_text == 'e':

                    try:

                        result = e

                        self.total.set(result)

                    except:

                        self.total.set("Error!")

                else:

                    self.total.set(self.entry.get() + b_text)

        if __name__ == "__main__":

            root = Tk()

            calc = SciCalc(root)

            root.mainloop()

    elif start == "calendar":

        root = Tk()

        root.geometry("400x400")

        root.title("Calendar")

        title = Label(
            root, fg="red", text="Calendar", font=("Arial", 96))

        title.pack()

        elabel = Label(root, text="")

        elabel.pack()

        c = Calendar(root, selectmode='day', day=12, month=7, year=2021)

        c.pack()

        def copy_date():

            copy(c.get_date())

        elabel2 = Label(root, text="")

        elabel2.pack()

        button = Button(root, text="Copy Date", command=copy_date)

        button.pack()

        root.mainloop()

    elif start == "cd":

        try:

            path = input("Enter your new path string: ")
            os.chdir(path)

            pathdec = path

        except FileNotFoundError as fnfe:

            print(f"Error 404 - No such file or directory: \'{path}\'")

        invalid_input = False

    elif start == "cat":

        cimp = input(
            "Enter in the file you want to display (with file extension): ")

        print(Path(cimp).read_text())

        invalid_input = False

    elif start == "cls":

        os.system("cls")

    elif start == "c path":
        print(pathdec)
        invalid_input = False

    elif start == "create doc":
        def createDoc():

            name = input(
                "What is the name of the file that you want to create (include file extension)?: ")

            ask = input(
                "What do you want to write as a template (leave blank if not needed)?: ")

            Doc = open(name, "w")
            Doc.write(ask)

            Doc.close
            invalid_input = False

        createDoc()

    elif start == "play adventure-game":

        name = input("Enter your name: ")

        print(f"Hello {name}, welcome to your adventure in the cave.")

        time.sleep(2)

        start = input("Do you want to start the game? (y/n): ")

        time.sleep(2)

        if start == "y" or start == "Y":
            print("You enter the cave...")
        elif start == "n" or start == "N":
            print(f"{name}, you are not living up to your full potential. Please come back when you are ready.")
            sys.exit
        if start == "y" or start == "Y":
            first_encounter = input("You walk to a passage that is divided, you can either go right (r) or left (l). Which one do you you choose?: ") 
            time.sleep(2)
            if first_encounter == "r" or first_encounter == "R":
                print("You chose to go right and met a bear.")
                time.sleep(1)
            else:
                print("You have walked to a dead end. You walk out of the cave and hope to restart the game. See you in the cave soon!")
                sys.exit
            if first_encounter ==  "r" or first_encounter == "R":
                fight = input("Do you choose to fight it with a sword (s) or with a hammer (h)?: ")
                if fight == "s" or fight == "S":
                    print("You killed the bear!")
                if fight == "h" or fight =="H":
                    print("You died! The bear is feeding on you! Better luck next time!")
                    sys.exit
                if fight == "s" or fight == "S":
                    time.sleep(2)
                    diamond_room = input("You walk into the room with a bag of diamonds. You pick the bag up, but the two ways out are: Going through a room of one year old boiling lava (bl), or going through the room of a really savage bull (sb). Which one do you choose?: ")
                    if diamond_room == "bl":
                        print("You win! Congratulations!")
                else:
                    print("You were torn apart by the bear and now are hanging on the wall. You are dead")
                    sys.exit

    elif start == "play digibingo":

        def num_maker(counter):
            xy = counter
            num = Label(d, anchor=CENTER, font=(
                'Arial', 25), text=("%02d" % (xy,)))
            counter = xy - 1
            i = ("%02d" % (counter,))
            z = int(i[1]) * 78
            if int(i[1]) > 4:
                z += 63
            x_pos = z + 55
            y_pos = int(i[0]) * 64 + 62
            num.place(x=x_pos, y=y_pos)

        def m10maker(n):
            maker = True
            qwerty = 0
            if qwerty > int((n - 1)/10) - 1:
                return
            while maker == True:
                if qwerty == int((n - 1)/10) - 1:
                    maker = False
                qwerty += 1
                multiples_of_10.append((qwerty * 10)-1)

        def getplayersnames(p, t, an, num):
            for counter in range(int(p)):
                n = num[an]
                the = simpledialog.askstring(
                    'Name', 'Who is your ' + n + ' player? ')
                t.insert(an, the)
                an = an + 1
                list_of_players = ', '.join(t)
            ans1 = messagebox.askyesno('Players', 'These are the players playing:\n' +
                                       list_of_players + '\nAre these the only people playing(y/n)?')
            if ans1 == False:
                play = simpledialog.askstring(
                    'Players', 'How many more players are playing?')
                getplayersnames(play, t, an, num)
            if ans1 == True:
                messagebox.askquestion(
                    'Part 2: Players Cards', 'Now for the player\'s cards. Are you ready to continue')
            else:
                play = simpledialog.askstring(
                    'Players', 'How many more players are playing?')
                getplayersnames(play, t, an, num)

        def makecards(clen, cnums, p, n):
            for a in range(p):
                num90 = list(range(1, n))
                for counter in range(clen):
                    cardnum = random.choice(num90)
                    num90.remove(cardnum)
                    cnums[a].append(cardnum)

        def getnumbers(num90, finnums, a, names, cards, fincards, an, nums, an2, finnames, an3):
            z = []
            while len(num90) > 0:
                chosen_number = random.choice(num90)
                num90.remove(chosen_number)
                finnums.append(chosen_number)
                cd.config(text=str(chosen_number))
                num_maker(chosen_number)
                time.sleep(1)
                an = 0
                an2 = 0
                for counter in range(len(names)):
                    an3 = 0
                    plural = ' numbers'
                    if chosen_number in cards[counter]:
                        an += 1
                        fincards[counter].append(chosen_number)
                        cards[counter].remove(chosen_number)
                        if len(cards[counter]) == 0:
                            an2 += 1
                            an3 += 1
                            messagebox.askquestion(
                                names[counter], (names[counter] + ' has finished their numbers and is ' + nums[0] + '\n Are you ready to continue?'))
                            finnames.append(names[counter])
                        if an3 != 1:
                            if len(cards[counter]) == 1:
                                plural = ' number'
                            messagebox.askquestion(names[counter], (names[counter] + ', you have ' + str(chosen_number) + ' in your card, and have ' + str(
                                len(cards[counter])) + plural + ' left to finish' + '\n Are you ready to continue?'))
                        time.sleep(0.5)
                if an2 >= 1:
                    z.append(an2)
                    nums.remove(nums[0])
                a = a + 1
                messagebox.askquestion('Ready', 'Are you ready to continue?')
            return [z, finnames]

        # Variables/Lists
        winner = 'winners are'
        finnumbers = []
        z = []
        the_players = []
        finplayers = []
        donenums = []
        any_use = 0
        anyuse = 0
        anyuses = 0
        any_uses = 0
        numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eigth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth',
                   'nineteenth', 'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'twenty-fourth', 'twenty-fifth', 'twenty-sixth', 'twenty-seventh', 'twenty-eigth', 'twenty-ninth', 'thirtieth', 'thirty-first', 'thirty-second']
        global multiples_of_10
        multiples_of_10 = []
        posTextList = []

        #Screens and Setup
        main = Tk()
        main.geometry('+90+10')
        display = Canvas(main, width=510, height=500)
        display.pack()

        board = Toplevel(main)
        board.geometry('+600+10')
        d = Canvas(board, width=920, height=700)
        d.pack()

        introDisp = Toplevel(main)
        introDisp.geometry('+90+620')
        introCanvas = Canvas(introDisp, width=900, height=400)
        introCanvas.pack()

        main.attributes("-topmost", True)
        board.attributes("-topmost", True)
        introDisp.attributes("-topmost", True)

        # Intro
        introText = '''Welcome to DigiBingo(2 - 30 players)!
        DigiBingo:
            1. Asks for details
            2. Makes each player a card of numbers
            3. Chooses a random number not chosen already 
            and shows which people have that number
            4. Displays the winner and the position of players
        Click on the screen above to get started.'''
        introLabel = Label(introCanvas, font=('Arial', 14),
                           text=introText, justify=LEFT)
        introLabel.pack()
        main.attributes("-topmost", False)
        board.attributes("-topmost", False)
        introDisp.attributes("-topmost", False)

        # Get player's names and Setup
        player = simpledialog.askstring(
            'Part 1: Players', 'How many players are playing DigiBingo?')
        getplayersnames(player, the_players, any_use, numbers)
        n = 91
        numbers_to_n = list(range(1, n))
        m10maker(n)

        # Make the cards
        cardnums = [[] for counter in repeat(None, len(the_players))]
        cardlen = 15
        makecards(int(cardlen), cardnums, len(the_players), n)
        for a in range(len(the_players)):
            l = ', '.join(map(str, cardnums[a]))
            messagebox.askquestion(
                the_players[a], (the_players[a] + ', your numbers are: ' + l + '\n Are you ready to continue?'))
        messagebox.askquestion('Ready', 'Are you ready to continue?')

        # Setup
        display.create_text(
            255, 25, text='The chosen number is:', font=('Arial', 20))
        cd = Label(display, text='', font=('Arial', 285))
        cd.place(x=255, y=250, anchor='center')

        # Calling the numbers
        fincardnums = [[] for counter in repeat(None, len(the_players))]
        y = getnumbers(numbers_to_n, finnumbers, any_use, the_players, cardnums,
                       fincardnums, anyuse, numbers, anyuses, finplayers, any_uses)
        z = y[0]
        finplayers = y[1]

        # Who wins?
        display.delete("all")
        cd.destroy()
        if z[0] == 1:
            winner = 'winner is'
        smt = Label(display, text=('The ' + winner + '...'),
                    font=('Arial', 20))
        smt.place(y=30, x=30)
        time.sleep(0.5)
        sm = Label(display, text=(
            ', '.join(finplayers[:z[0]])), font=('Arial', 20))
        sm.place(x=240, y=30)
        numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th',
                   '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31th', '32th']
        for counter in range(len(z)):
            posTextList.append(
                f"{numbers[counter]}: {', '.join(finplayers[:z[0]])}")
            for counter in range(z[0]):
                finplayers.remove(finplayers[0])
            z.remove(z[0])
        h = Label(display, text='\n'.join(posTextList),
                  font=('Arial', 20), justify=LEFT)
        h.place(y=60, x=30)
        main.mainloop()

        invalid_input = False

    elif start == "exit":
        sys.exit()
        invalid_input = False

    elif start == "fahrenheit to celcius":
        lower = 0
        upper = 300
        step = 20

        fahr = lower
        while (fahr <= upper):
            celcius = (5.0/9.0) * (fahr-32.0)
            print(fahr, celcius)
            fahr = fahr + step
        invalid_input = False

    elif start == "games":

        root = Tk()

        title = Label(root, text="Games").pack()
        blank = Label(root, text="").pack()
        agamelabel = Label(root, text="Adventure Game - Command: \"play adventure-game\"")
        snakelabel = Label(root, text="Snake - Command: \"play snake\"").pack()
        dblabel = Label(
            root, text="DigiBingo - Command: \"play digibingo\"").pack()
        tttlabel = Label(
            root, text="Tic-Tac-Toe - Command: \"play tic-tac-toe\"").pack()

        root.mainloop()

        invalid_input = False

    elif start == "gtoken add":

        global githubtoken

        tok = input("Enter in your GitHub token: ")

        githubtoken = tok

    elif start == "gfind repo topic":

        g_cred = Github(githubtoken)

        topic = input("Enter in the topic name: ")

        count = int(input("Enter in the number of repositories to display: "))

        repo_count = count

        icount = 0

        for i in g_cred.search_repositories(f"topic:{topic}"):

            print(f"{icount + 1}. {i}")

            icount += 1

            if icount >= repo_count:

                break
            
    elif start == "github commands":

        root = Tk()

        title = Label(root, text="GitHub Commands").pack()
        blank = Label(root, text="").pack()
        starslabel = Label(root, text="Find the number of stars in a GitHub repository - Command: \"gstars repo\"").pack()
        repofinderlabel = Label(root, text="Find a GitHub repository based on a topic - Command: \"gfind repo topic\"").pack()
        tokenlabel = Label(root, text="Enter in your GtiHub token - Command: \"gtoken add\"").pack()

        root.mainloop()

        invalid_input = False

    elif start == "gstars repo":

        g_cred = Github(githubtoken)

        f_repo = input("Enter repository name to see its stars (eg. User/Repo): ")

        repo = g_cred.get_repo(f_repo)

        print(repo.stargazers_count)

    elif start == "help":
        print("Donut Emulator Version 3.0 'Blitz'.")
        print("This is a default shell command. Type `help' to see this list.")
        print("For more information, visit https://netfruittechnologies.wordpress.com/donut-emulator/.")
        print("bmi calc - Opens up a BMI calculator")
        print("calc - Opens up the calculator.")
        print("calendar - Opens up a calendar.")
        print("cat - prints the contents of a file in the current directory.")
        print("cd - Changes your path to what you specify.")
        print("cls - Clears the terminal screen.")
        print("c path - Views your current Python path.")
        print("create doc - Creates a document that you specify.")
        print("exit - Exits the terminal.")
        print("fahrenheit to celcius - Converts Fahrenheit temperatures from 0 to 300 degrees into Celcius temperatures.")
        print("games - Views a list of games to play.")
        print("github commands - Opens a list of GitHub commands to utilize.")
        print("help - Displays help.")
        print("ls - Lists files and folders in current directory.")
        print("ping - Ping an IP address/website.")
        print("qr code gen - Generates a QR code of your choice, and opens up a URL or text on scanning.")
        print("sample form - Prints out a sample form.")
        print("sys info - Displays system information.")
        print("term info - Displays terminal information.")
        print("time - Displays local time.")
        print("timer - Sets a timer.")
        
        invalid_input = False

    elif start == "ls":

        contents = scandir(pathdec)

        for i in contents:

            if i.is_file():

                print(i.name)

            elif i.is_dir():

                print(f"/{i.name}")

        invalid_input = False

    elif start == "ping":

        ipAddress = input("Enter in IP address/website to ping: ")

        subprocess.call(f"ping {ipAddress}", shell=False)

        invalid_input = False

    elif start == "qr code gen":

        contents = input("Enter in a URL or any text: ")

        backg = input("Enter in background color: ")

        foreg = input("Enter in foreground color: ")

        data_b = input("Enter in background color for data: ")

        data_f = input("Enter in foreground colour for data: ")

        file_name = input("Enter in a file name for your QR code (with extension): ")

        code = make_qr(contents)

        code.save(
            file_name,
            scale = 10,
            dark = foreg,
            light = backg,
            data_dark = data_b,
            data_light = data_f

        )

    elif start == "play snake":
        delay = 0.1

        score = 0
        high_score = 0

        win = turtle.Screen()
        win.title("Snake")
        win.bgcolor("black")
        win.setup(width=800, height=600)
        win.tracer(0)

        head = turtle.Turtle()
        head.shape("square")
        head.color("white")
        head.up()
        head.goto(0, 0)
        head.direction = "Stop"

        food = turtle.Turtle()
        colors = random.choice(['red', 'orange', 'green'])
        food.speed(0)
        food.shape("square")
        food.color(colors)
        food.up()
        food.goto(0, 100)

        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 250)
        pen.write("Score: 0  High Score: 0", align="center",
                  font=("arial", 24, "bold"))

        def go_up():
            if head.direction != "down":
                head.direction = "up"

        def go_down():
            if head.direction != "up":
                head.direction = "down"

        def go_left():
            if head.direction != "right":
                head.direction = "left"

        def go_right():
            if head.direction != "left":
                head.direction = "right"

        def move():
            if head.direction == "up":
                y = head.ycor()
                head.sety(y+20)
            if head.direction == "down":
                y = head.ycor()
                head.sety(y-20)
            if head.direction == "left":
                x = head.xcor()
                head.setx(x-20)
            if head.direction == "right":
                x = head.xcor()
                head.setx(x+20)

        win.listen()
        win.onkeypress(go_up, "w")
        win.onkeypress(go_down, "s")
        win.onkeypress(go_left, "a")
        win.onkeypress(go_right, "d")
        win.onkeypress(go_up, "Up")
        win.onkeypress(go_down, "Down")
        win.onkeypress(go_left, "Left")
        win.onkeypress(go_right, "Right")

        segments = []

        while True:

            win.update()

            if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:

                time.sleep(1)

                head.goto(0, 0)

                head.direction = "Stop"

                colors = random.choice(['red', 'blue', 'green'])

                for segment in segments:

                    segment.goto(1000, 1000)

                segments.clear()

                score = 0

                delay = 0.1

                pen.clear()

                pen.write("Score: {} High Score: {} ".format(
                    score, high_score), align="center", font=("arial", 24, "bold"))

            if head.distance(food) < 20:

                x = random.randint(-270, 270)

                y = random.randint(-270, 270)

                food.goto(x, y)

                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("white")
                new_segment.up()
                segments.append(new_segment)

                delay -= 0.001

                score += 1

                if score > high_score:

                    high_score = score

                pen.clear()

                pen.write("Score: {} High Score: {} ".format(
                    score, high_score), align="center", font=("arial", 24, "bold"))

            for index in range(len(segments)-1, 0, -1):
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x, y)
            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x, y)
            move()

            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0, 0)
                    head.direction = "stop"
                    colors = random.choice(['red', 'blue', 'green'])
                    for segment in segments:
                        segment.goto(1000, 1000)
                    segment.clear()

                    score = 0
                    delay = 0.1
                    pen.clear()
                    pen.write("Score : {} High Score : {} ".format(
                        score, high_score), align="center", font=("arial", 24, "bold"))
            time.sleep(delay)

        win.mainloop()

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
        print("Donut Emulator Version 3.0 'Blitz'.")
        invalid_input = False

    elif start == "play tic-tac-toe":

        theBoard = {'7': ' ', '8': ' ', '9': ' ',
                    '4': ' ', '5': ' ', '6': ' ',
                    '1': ' ', '2': ' ', '3': ' '}

        board_keys = []

        for key in theBoard:

            board_keys.append(key)

        def printBoard(board):

            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('-+-+-')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('-+-+-')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])

        def game():

            turn = 'X'

            count = 0

            for i in range(10):

                printBoard(theBoard)
                print('It is your turn, ' + turn +
                      '. Where would you like to move?')

                move = input()

                if theBoard[move] == ' ':

                    theBoard[move] = turn

                    count += 1

                else:

                    print(
                        "That place has already been taken.\nWhere do you want to move?")

                    continue

                if count >= 5:

                    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':

                        printBoard(theBoard)

                        print('Game over\n')

                        print(' **** ' + turn + ' won ****')

                        break

                    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':

                        printBoard(theBoard)

                        print('Game over\n')

                        print(' **** ' + turn + ' won ****')

                        break

                    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':

                        printBoard(theBoard)

                        print('Game over\n')

                        print(' **** ' + turn + ' won ****')

                        break

                    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':

                        printBoard(theBoard)

                        print('Game over\n')

                        print(' **** ' + turn + ' won ****')

                        break

                    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':

                        printBoard(theBoard)

                        print('Game over\n')

                        print(' **** ' + turn + ' won ****')

                        break

                    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':

                        printBoard(theBoard)

                        print('Game over\n')

                        print(' **** ' + turn + ' won ****')

                        break

                    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':

                        printBoard(theBoard)

                        print('Game over\n')

                        print(' **** ' + turn + ' won ****')

                        break

                    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':

                        printBoard(theBoard)

                        print('Game over\n')

                        print(' **** ' + turn + ' won ****')

                        break

                if count == 9:
                    print("\nGame Over!\n")
                    print("It's a tie!")

                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

            restart = input("Do you want to play again? (y/n)? ")
            if restart == "y" or restart == "Y":
                for key in board_keys:
                    theBoard[key] = " "

                game()

        if __name__ == "__main__":
            game()

    elif start == "time":

        root = Tk()

        root.title("Digital Clock")

        root.geometry("235x60")

        clock = Label(root, fg="black", font=("Arial", 30, 'bold'))

        clock.place(x=0, y=0)

        def digital_clock():
            time = strftime('%H: %M: %S')

            clock.configure(text=time)

            clock.after(1000, digital_clock)

        digital_clock()

        root.mainloop()

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
        print(f"donutshell: {start}: command is not recognized.")


while invalid_input:  # this will loop until invalid_input is set to be True
    main()