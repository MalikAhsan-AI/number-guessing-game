import random
moves = 0
flag = False
final_number = random.randint(1, 100)
while moves != 10 and not flag:
    number = int(input("enter a number:"))
    if 1 <= number <= 100:
        if number == final_number:
            print("good job you correctly guessed the number", final_number)
            flag = True
        else:
            print("try again you guessed wrong")
            moves += 1
    else:
        print("number is out of range")

if moves == 10 or not flag:
    print(f"Sorry, you used all 10 tries. The number was {final_number}.")
