from sys import exit


print "Welcome to Star Wars the Game"
print "Please use all lower case for your answers"
print "You are green to engage Red leader"
print "You are flying in to engage the death star"
print "Do you wish to engage?"

engage = raw_input("> ")
if engage == "yes":
    print "You engage the enemy"

elif engage == "no":
    print "You are a coward."

else:
    print "You get hit by an asteroid and die."


def start():
    print "You see Vader behind you"
    print "Do you evade? Yes or No?"
    choice = raw_input("> ")
    if  choice == "yes":
        print "You did it, He missed"
        death_star_mission()
    elif  choice == "no":
        print "I have you now"
        print "Your x-wing was blown up."
        exit()

    else:
        print"learn how to read"

def death_star_mission():
    print "You have evaded vader, lets blow this thing and get out of here kid"
    print "Do you wish to fire proton torpedos?"
    torpedo = raw_input()
    if torpedo == "yes":
        print "You blew up the death star"
        exit()
    elif torpedo == "no":
        print "what are you doing?!?! fire that shit"
    else:
        print "You died"
        exit()

start()
















start()
