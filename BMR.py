#create a variable 'name' and input intro conversation to ask user's name
name = input("Hello, you beautiful Human. What's your name? ")

age = int(input("Well, HELLO " + name + "!!! My name is @nirdla_. You can find me on Instagram. \n May I say you look AMAZING today! \nAnyways, I am here to help you calculate your Basal Matabolic Rate using the Harris-Benedict Formula. \n First off, what is your age in years? "))
height = float(input("What is your height in inches?: "))
weight = float(input("Okay, cool. How much do you weigh in pounds?: "))
gender = int(input("Lastly, do you consider yourself\n1. MALE\n2. FEMALE\nPlease pick either 1 or 2: "))

if gender == 1: #male 
    rate = print("Using the Harris-Benedict formula, your BMR is ", 66 + (6.3*weight) + (12.9*height) - (6.8*age), " calories per day. Awesome!\n Have a great rest of your day and don't forget to follow @nirdla_ on Instagram! Buhbye for now!!")
else:
    rate = print("Using the Harris-Benedict formula, your BMR is ", 655 +(4.3*weight) + (4.7*height) - (4.7*age), " calories per day. Awesome!\n Have a great rest of your day and don't forget to follow @nirdla_ on Instagram! Buhbye for now!!")