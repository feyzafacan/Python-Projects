# PROJECT 4 -CHOOSE YOUR OWN ADVENTURE GAME-  (easy)

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?: ").lower()

if answer  == "left":
    
    q2 = input("You come to a river, you can walk around it or swim across? Type walk or swim: ").lower()
    
    if q2 == "swim":
        print("You swim across and were eaten by alligator.")
    elif q2 == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose.")
        
        
elif answer == "right":
    
    q2 = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back): ").lower()
    
    if q2 == "back":
        print("You go back and lose.")
    elif q2 == "cross":
        
        q3 = input("You cross the bridge and meet a stranger. Do you talk to them?: (yes/no) ").lower()
        if q3 == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif q3 == "no":
            print("You ignore the stranger and they are offened and you lose.")
        else:
            print("Not a valid option. You lose.")
    
    else:
        print("Not a valid option. You lose.")
    
else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)








