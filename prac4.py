import os
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
grade_test()
