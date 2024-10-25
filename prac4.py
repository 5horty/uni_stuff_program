import os
from graphix import Window,Text,Point
def personal_greeting():
    name = input("please enter your name ")
    print(f"Hello {name}, nice to see you!")

def formal_name():
    namef = input("enter your forename ")
    nameS =input("enter your surname ")
    namef_formal = namef[0]
    print(f"{namef_formal}. {nameS}")

def kilos_to_ounces():
    kilos = float(input("enter kilos "))
    ounces = kilos * 35.2739619
    kilos = round(kilos,2)
    ounces = round(ounces,2)
    print(f"here is {kilos} and {ounces}")

def generate_surnameemail():
    forename = input("enter your first name ")
    forename = forename[0]
    surname = input("enter you last name ")
    year = input("enter the year you joined uni")
    surname = surname[:4]
    email_back = "@myport.ac.uk"
    email = surname + "." + forename +"."+year+email_back
    print(email)

def grade_test():
    grades = "FFFFCCBBAAA"
    grade = int(input("pls enter a a number 1-10 "))
    gradeletter = grades[grade]
    print(f"your letter grade is {gradeletter} and number is {grade}")

def graphics_letters():
    user_word = input("enter a word ")
    win = Window()
    for i in user_word:
        click=win.get_mouse()
        text = Text(Point(click.x,click.y),"")
        text.text = i
        text.draw(win)
    win.get_mouse()
    win.close()

def sing_a_song():
    user_word = input("enter a word pls ")
    user_lines = int(input("enter how many lines "))
    user_wordperLine = int(input("enter how many words peer line"))
    user_wordsp = user_word + " "
    for i in range(user_lines):
        user_wordpl = user_wordsp * user_wordperLine + "\n" 
        user_wordpl.strip("\n")
        print(user_wordpl) 

sing_a_song()



