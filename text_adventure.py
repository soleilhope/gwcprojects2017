start = '''
It's 11:00pm. You are bored out of your mind when suddenly..
Your friend texts you,"Hey! Big party to night you should come!"
You know your parents won't let you out..
Should you sneak out? Or ask your parents permission to leave the house?
'''
sneak_out = "You snuck out... and went to a party"
ask_parents = "You asked your parents... they said no"
dance = "You went to dance! But, somebody slipped a pill in your drink while it was unattended and you drink it."
sit = "You sit down on the couch and accidently fall asleep on it and shortly after the cops show up to the party!"
Yes = "Oh no! You have to sleep in the garage in your car!"
print(start)

    print("Type 'Sneak out' to "sneak out" or 'Go ask parents to get their permission' to "get parent permission".")
    user_input = input()
    if user_input == "Sneak out":
        print("You choose to sneak out and..") # finished the story by writing what happens
        print(sneak_out)
        done= True
    elif user_input == "Go ask parents to get their permission":
        print("You choose to go ask for your parents permission ...") # finished the story writing what happens
        print(ask_parents)
        print(sneak_out)
        done= True
    else:
        print("Wrong option")
        done = False

    print("You're at a party!")

    print("Type 'Dance' to "dance" or 'Sit' to "sit")

    user_input = input()
    if user_input == "Dance"
        print("You choose to dance and..")
        print(dance)
        done = True
    elif user_input == "Sit"
    print("You choose to sit and..")
    print(sit)
    done = True
else:
    print("Wrong option")
    done = False

    print("You're trashed dude! Go home?")

    print("Type 'Yes' to "go home" or 'No' to "stay")

user_input = input()
if user_input == "Yes"
    print("You chose to go home")
    print(Yes)
    done =
