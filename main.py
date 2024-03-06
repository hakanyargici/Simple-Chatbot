#Simple Chat Bot

#Question One
bot_name = "Yudu"
birth_year = 2024
print(f"Hello! My name is {bot_name}.\nI was created in {birth_year}.")

#Question Two
your_name = input("Please, remind me your name.\n> ")
print(f"What a great name you have, {your_name.title()}!")

#Question Three 
print("Let me guess your age.")

age_success = False
while not age_success:
    all_reaminders = input("Enter remainders of dividing your age by 3, 5 and 7(You should to enter all remainders with one whitespace.)")
    remainders = all_reaminders.split(" ")
    print(remainders)


    age = ((remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105) #0 ve 104 aralığını seçer.
