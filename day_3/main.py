print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

step1 = input("left or right?")



if step1 == "left":
    step2 = input("swim or wait?")
    if step2 == "wait":
        step3 = input("Which door? R, Y or B")
        if step3 == 'R':
            print('Burned by fire. Game Over.')
        elif step3 == 'Y':
            print('You win!')
        elif step3 == 'B':
            print('Eaten by beasts. Game Over.')
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")