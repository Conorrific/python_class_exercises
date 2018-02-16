#coins
print("you are starting with 0 coins.. ")
answer = input("would you like a coin? ")
answer.lower()
coins = 0
if answer == "yes":
    coins += 1
    print("you currently have " + str(coins) + " coin(s)")
    more = input("do you want another? ")
    if more == "yes":
        coins += 1
        print("here you go!")
        print("new current coin count is.. " + str(coins))
    else:
        print("That's all for now then..")
    if coins >= 2:
        cont = input("shall we continue? ")
        if cont == "yes":
            more = input("do you want another? ") 
            if more == "yes":
                coins += 1
                print("here you go!")
                print("new current coin count is.. " + str(coins) + " and that's all you get!")
            elif more != "yes":
                print("Oh no!")
        else:
            print("Well ok then.. bye!!")    
else:
    print("Goodbye!")


