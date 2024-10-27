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

def exchange_table():
    pound = 1.17
    print("euros\t | \t pounds")
    print("-"*20)
    for i in range(21):
        if i != 0:
            poval = i / pound
            povalreal = round(poval,2)
        else:
            povalreal = i
        print(f"{i:> 5} euros \t | \t pounds {povalreal:> 6.2f}") 


def make_inialism():
    user_input = input("enter a phrase ")
    words = user_input.split()
    firstlet =""
    for word in words:
        firstlet += word[0]
    firstlett = firstlet.upper()
    print(firstlett)


def file_in_caps():
    filename = input("enter a file name ")
    with open(filename,"r") as file:
        lines = file.readlines()
        content = ""
        for line in lines:
            content+=line
        content_up = content.upper()
        print(content_up)

def total_spending():
    total = 0.0
    with open("spending.txt","r") as file:
        for line in file:
            parts = line.strip()
            if len(parts) > 1:
                amount = float(parts.strip())
                total += amount
        print(total)

def test():
    list1=[]
    for i in range(100):
        list1.append(i)
    print(list1)
test()

