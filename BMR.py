#Basal Metabolic Calculator

#create variable 'name' and assign input() for user to reply
name = input("Hello, you beautiful Human. What's your name? ")

#create variable 'age' and assign int(input()) for user to reply his/her age in years
age = int(input("Well, HELLO " + name + "!!! My name is @nirdla_. You can find me on Instagram. \n May I say you look AMAZING today! \nAnyways, I am here to help you calculate your Basal Matabolic Rate using the Harris-Benedict Formula. \n First off, what is your age in years? "))

#create variable 'height' and assign float(input()) for user to reply with his/her heigh in inches
#float allows user to reply in decimal form
height = float(input("What is your height in inches?: "))

#create variable 'weight' and assign float(input()) for user to reply with his/her weight
weight = float(input("Okay, cool. How much do you weigh in pounds?: "))

#create variable 'gender' and assign int(input()) for user to reply with his/her gender
#explain to user to reply in numeric form 1 or 2 to identify gender
gender = int(input("Lastly, do you consider yourself\n1. MALE\n2. FEMALE\nPlease pick either 1 or 2: "))

#create an if/else statement regarding user's gender
#if user's gender is male, or '1,' then use the Harris-Benedict formula for male BMR
if gender == 1: #male 
    rate = print("Using the Harris-Benedict formula, your BMR is ", 66 + (6.3*weight) + (12.9*height) - (6.8*age), " calories per day. Awesome!\n Have a great rest of your day and don't forget to follow @nirdla_ on Instagram! Buhbye for now!!")

#else, if user is female (or '2'), then use the Harris-Benedict formula for female BMR
else: #else 2, female
    rate = print("Using the Harris-Benedict formula, your BMR is ", 655 +(4.3*weight) + (4.7*height) - (4.7*age), " calories per day. Awesome!\n Have a great rest of your day and don't forget to follow @nirdla_ on Instagram! Buhbye for now!!")

#code complete!