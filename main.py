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

#Sorgu başlangıcı
input_success = False
while not input_success:
    all_remainders = input("Enter remainders of dividing your age by 3, 5 and 7(You should to enter all remainders with one whitespace.)")
    remainders = all_remainders.split(" ")

    #age değişkeniminiz çalışması için en az 3 input girilmesi gerektiğini belirten koşul 
    if len(remainders) != 3:
        print("Retry: Ensure that you provide 3 inputs.")
        continue
    
    #all_remainder'a girilenlerin integer olduğunu sorgulayan koşul
    rem3, rem5, rem7 = remainders
    if not (rem3.isdigit() and rem5.isdigit() and rem7.isdigit()):
        print("Retry: Non integer input")    
        continue

    #input'u int ifadeye çevirme
    rem3, rem5, rem7 = int(rem3), int(rem5), int(rem7)
    
    #Girdilerin hem büyüklük kontrolünü sağlatan koşul (1 2 1)
    if not (0 <= rem3 < 3 and 0 <= rem5 < 5 and 0 <= rem7 < 7):
        print("Retry: Ensure that remainder ranges are proper.")
        continue

    #0 ve 104 aralığınıdaki sayıları girilen bilgiye göre hesaplayarak bulur.
    age = ((rem3 * 70 + rem5 * 21 + rem7 * 15) % 105)

    print(f"Your age is {age}; that's a good time to start programming!")

    input_success = True