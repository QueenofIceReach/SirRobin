from sys import exit

print "You are brave Sir Robin of the knights of the Round Table."
print "All of the knights have been given a mission to find the Holy Grail."
print "You delay as long as possible before packing up your things and leaving the castle."
print "The drawbridge closes behind you.  There is no turning back now."
print "You follow along the path through the village outside the castle walls with your trusted minstrels."



penis = '"8===>"'
run = ["run", "away", "back", "turn back"]
good = ["good", "great", "fantastic", "super",]
bad = ["bad", "awful"]
poop = ["poop", "turds", "shit", "crap", "crappy"]
shrubbery = 1
gold = int(50)

def town():
    print "You are in a typical village.  Beard shop... gourd shop...cart."
    print "To the left is a forest.  To the right is a swamp."
    print "What would you like to do?"

    choice = raw_input(penis)
    if choice in run:
        print "The drawbridge is already up.  Get on with it."
        town()
    elif "cart" in choice:
        cart()
    elif choice == "left" or choice == "forest":
        forest()
    elif choice == "right" or choice == "swamp":
        swamp()
    else:
         print "That's a terrible option.  Stop being a weenie and make up your damn mind."
         town()


def cart():
    print "You see a man with a cart.  Do you approach?"
    approach_cart = raw_input(penis)
    if approach_cart in run:
        print "CMON......  STOP THAT...."
        town()
    elif "no" in approach_cart:
        print "ok.... fine....The cart travels on."
        town()
    elif "yes" in approach_cart:
        shrubchoice()
    else:
        print "WHAAT??"
        cart()

def shrubchoice():
    print "You approach the cart.  'Hello kind sir.  My name is Roger.  Roger the shrubber.'"
    if shrubbery == 1:
        print "'May I interest you in some shrubbery?  These fine shrubs cost a mere 7 gold.'"
        shrubbuy()
    elif shrubbery == 2:
        print "Wait.  We've met before.  You already purchased a shrubbery.  I hope you enjoy it.  Have a fine day."
        town()
    else:
        print "turds."

def shrubbuy():
    shrubbuy = raw_input(penis)
    if "yes" in shrubbuy:
        print "Ok fantastic.  I hope you enjoy your new shrubbery! "
        global shrubbery
        shrubbery = 2
        print shrubbery
        town()
    else:
        print "Ok, thats fine then.  Have a nice day sir."
        town()

def forest():
    if shrubbery > 1:
        forest_shrub()
    else:
        print "The forest is dark and creepy.  You see a lot of trees.  You hear spooky sounds."
        print "Do you go forward or turn back? "
        forest_choice = raw_input(penis)
        if "turn" in forest_choice or "back" in forest_choice:
            town()
        else:
            print "You see a group of very large mythical Knights."
            print "'We are the Knights who say NI, keepers of the sacred words NI, PENG and NE-WOMB!'"
            print "'iF YOU ARE TO PASS YOU MUST DELIVER TO US ONE SHRUBBERY!!'"
            print "How do you respond?"
            ni_response = raw_input(penis)
            if "fight" in ni_response or "no" in ni_response:
                dead("The nights scream NI NI NI NI NI and chop off your head.")
            elif "run" in ni_response or "away" in ni_response:
                print "You bravely run away away!"
                town()
            else:
                print "It sounds like its best to do what they say.  You turn around."
                town()

demands = ["another shrubbery!", "cut down the largest tree in the forest with a herring!"]

def forest_shrub():
    print "The forest is dark and creepy, as always.   Your minstrels continue to sing about how badly you will be maimed.  It is not helping."
    print "You return to the area with the Knights that say NI and present to them the offering of a shrubbery."
    print "The knights tell you they have further demands!"
    for demand in demands:
        print "We demand %r" %demand
    print "What do you say in response?"
    response = raw_input(penis)
    if "it" in response:
        print "They cower in fear holdding their ears.  You pass by them.  You win!"
    elif "run" in response:
        print "You are such a weenie."
        town()
    else:
        dead("The Knights chop off your head.")


def swamp():
    print "The swamp is mucky. It smells like fungus and rot.... or is that death?"
    print "How are you feeling about your adventure so far?"
    feeling = raw_input(penis)
    if feeling in good:
        print "You are a terrible liar.  Your knees are shaking you sorry sot."
    elif feeling in poop:
        print "That is just unfortunate."
    elif feeling in bad:
        print "You've got that right.  Now grow a pair and lets do this."
    else:
        print "You are so scared you aren't even making sense.  Lets move along."
    print "Now where to?  Right?  Left?  Straight?"

    swampchoice = raw_input(penis)
    if "run" in swampchoice or "away" in swampchoice:
        print "Oh for the love of god.  Really?  You're going to make me do this? FINE."
        town()
    elif "straight" in swampchoice:
        print "You keep walking and somehow avoid all the dangers of the swamp!"
        print "You see more and more trees."
        forest()
    elif "right" in swampchoice:
        dead("You get eaten whole by an enormous rat.")
    else:
        dead("You fall into a mucky part of the swamp and remember you can't swim.  How unfortunate.")



def dead(why):
    print why, "Oh Good Job, you're dead!"
    exit(0)


town()
