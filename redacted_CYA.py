###########################################################################################
# Date: 11 - 13 - 19
# Description: choose your own adventure; bonus assignment
###########################################################################################

from tkinter import*
from random import randint

# constants so gui can be easily modified for testing, etc
HEIGHT = 850
WIDTH = 800
STAM = 0
STR = 0
LUCK = 0
GOLD = 0
STAGE = 0

#intro window
class StartingScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.mainsetup(master)
        self.master.title("a choose your own adventure game")

    def mainsetup(self, master):
        for r in range(4):
            self.master.rowconfigure(r, weight=1)
        for c in range(2):
            self.master.columnconfigure(c, weight=1)
        frame_intro = Frame(master, bg="red", bd=1, relief=GROOVE)
        frame_intro.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=W + E+N+S)
        frame_options = Frame(master, bg="blue", bd=1, relief=GROOVE)
        frame_options.grid(row=3, column=0, rowspan=1, columnspan=2, sticky=W + E + N+S)

        intro=Label(frame_intro, bg="white", height = 0, width = 0, text="Welcome, Adventurer.\nIf you are sitting comfortably,\nthen we shall begin.", font=("Comic Sans MS", 30))
        intro.pack(expand=True, fill='both', padx=(10), pady=(10), anchor="n")

        roll1 = Button(frame_options, text="ROLL STATS AND START GAME", font=("Comic Sans MS", 20), command=lambda: begin())
        roll1.pack(expand=True, fill='both', padx=(30), pady=(30), anchor="n")



# creates primary window
class FrameMake(Frame):
    # inherit from frame, because it has a bunch of useful stuff i guess
    def __init__(self, master):
        Frame.__init__(self, master)
        self.mainsetup(master)
        self.master.title("game interface")

    def mainsetup(self, master):
        for r in range(3):
            self.master.rowconfigure(r, weight=1)
        for c in range(4):
            self.master.columnconfigure(c, weight=1)

        frame_text = Frame(master, bg="red", bd=1, relief=GROOVE)
        frame_text.grid(row=0, column=1, rowspan=3, columnspan=3, sticky=W + E + N + S)

        frame_info = Frame(master, bg="blue", bd=1, relief=GROOVE)
        frame_info.grid(row=0, column=0, rowspan=5, columnspan=1, sticky=W + E + N + S)

        frame_choices = Frame(master, bg="cyan", bd=1, relief=GROOVE)
        frame_choices.grid(row=3, column=1, rowspan=1, columnspan=3, sticky=W + E + N + S)
        frame_choices.columnconfigure(0, weight=1)

        self.text1 = Text(master=frame_text, width=0, height=0, spacing1=5, spacing2=1, spacing3=12, font=("Times New Roman", 14), wrap=WORD)
        self.text1.pack(expand=True, fill='both', padx=(10), pady=(10))
        # binds input to break, to prevent entering text to the text box
        self.text1.bind("<Key>", lambda e: "break")

        # for E+W stretching of labels
        frame_info.columnconfigure(0, weight=1)

        self.stats1 = Label(master=frame_info, height=3, font=("Times New Roman", 14), text="Stamina = {}".format(STAM), bd=1, relief=GROOVE)
        self.stats1.grid(row=0, sticky=W+E, padx=(1), pady=(1))
        self.stats2 = Label(master=frame_info, height=3, font=("Times New Roman", 14), text="Strength = {}".format(STR), bd=1, relief=GROOVE)
        self.stats2.grid(row=1, sticky=W+E, padx=(1), pady=(1))
        self.stats3 = Label(master=frame_info, height=3, font=("Times New Roman", 14), text="Luck = {}".format(LUCK), bd=1, relief=GROOVE)
        self.stats3.grid(row=2, sticky=W+E, padx=(1), pady=(1))
        self.stats4 = Label(master=frame_info, height=3, font=("Times New Roman", 14), text="Gold = {}".format(GOLD), bd=1, relief=GROOVE)
        self.stats4.grid(row=3, sticky=W+E, padx=(1), pady=(1))

        ###############choices

        self.choice1 = Button(frame_choices, height=2, text="none", font=("Times New Roman", 14),
                       command=lambda: answer(1))
        self.choice1.grid(row=0, sticky=W+E, padx=(1), pady=(1))
        self.choice2 = Button(frame_choices, height=2, text="none", font=("Times New Roman", 14),
                       command=lambda: answer(2))
        self.choice2.grid(row=1, sticky=W+E, padx=(1), pady=(1))
        self.choice3 = Button(frame_choices, height=2, text="none", font=("Times New Roman", 14),
                       command=lambda: answer(3))
        self.choice3.grid(row=2, sticky=W+E, padx=(1), pady=(1))




###################################
def roll_new_stats():
    # ISTR as in initial strength, for restarting game with same stats potentially
    global STAM, STR, LUCK, ISTR, ISTAM, ILUCK
    # rolls 1d6 + 6 for STR and LUCK
    ISTR = STR = randint(1, 6) + 6
    ILUCK = LUCK = randint(1, 6) + 6
    # rolls 2d6+12 for STAMINA
    ISTAM = STAM = randint(1, 6) + randint(1, 6) + 12


#destroy "startup window", roll stats, and create game window
def begin():
    global mainframe, w1
    roll_new_stats()
    w1.destroy()
    w1=Tk()
    w1.geometry("{}x{}".format(WIDTH, HEIGHT))
    mainframe = FrameMake(w1)
    intro()
    story()

#restart
def begin_again(option):
    global STAM, STR, LUCK, ISTR, ISTAM, ILUCK, GOLD, STAGE
    if option == "same stats":
        LUCK=ILUCK
        STR=ISTR
        STAM=ISTAM
    else:
        roll_new_stats()
    GOLD=0
    STAGE=0
    mainframe.stats1.config(text="Stamina = {}".format(STAM))
    mainframe.stats2.config(text="Strength = {}".format(STR))
    mainframe.stats3.config(text="Luck = {}".format(LUCK))
    mainframe.stats4.config(text="Gold = {}".format(GOLD))
    intro()

#changes textbox in window and text on buttons correspondingly
def story():
    mainframe.text1.delete('1.0', END)
    mainframe.text1.insert('1.0', "{}".format(textbox))
    mainframe.choice1.config(text= "{}".format(choice1))
    mainframe.choice2.config(text= "{}".format(choice2))
    mainframe.choice3.config(text= "{}".format(choice3))

#main "choice tree"
def answer(choicenumber):
    if STAGE==-1:   #death screen
        if choicenumber==1:
            begin_again("same stats")
        elif choicenumber==2:
            begin_again("new stats")
        else:
            quit()
    elif STAGE == 0:
        stage0()

    elif STAGE==1:
        if choicenumber==1:
            stage1()
        elif choicenumber==2:
            #head down road to town
            stage5()
        else:
            # go to forest
            stage3()
    #looting corpses
    elif STAGE==2:
        temp = roll_luck()
        if temp == "PASS":
            stage2a()
        else:
            stage2b()
        stage2()
    elif STAGE==3:
        if choicenumber==1:
            #head down road to town
            stage5()
        else:
            #go to forest
            stage3()
    elif STAGE==4:
        #forest death
        stage4()
    elif STAGE==6:
        #help the man
        if choicenumber==1:
            stage6a()
        #rob the man
        elif choicenumber==2:
            stage6b()
        #ignore the man
        else:
            stage6c()
    elif STAGE==7:
        #fight
        if choicenumber == 1:
            stage7a()
        #give him your money
        elif choicenumber == 2:
            stage7b()
        #try to run
        else:
            stage7c()
    #trying to run, pass or fail
    elif STAGE==8:
        temp = roll_luck()
        if temp == "PASS":
            stage8a()
        else:
            stage8b()
    #if failed to run, you have to fight
    elif STAGE==9:
        stage7a()
    #last meaningful stage, to town
    elif STAGE==10:
        #only choice is to keep going down road
        stage10()
    else:
        print("you've broken this somehow")
    story()

def roll_luck():
    #roll 2d6, if <= LUCK then you succeed
    global LUCK, textbox, ROLL1, ROLL2
    ROLL1 = randint(1,6)
    ROLL2 = randint(1,6)
    if ROLL1+ROLL2 <= LUCK:
        LUCK = LUCK-1
        mainframe.stats3.config(text = "Luck = {}".format(LUCK))
        return "PASS"
    else:
        return "FAIL"

#shorthand for hiding and showing buttons in GUI
def hide_1():
    mainframe.choice1.grid_forget()
def hide_2():
    mainframe.choice2.grid_forget()
def hide_3():
    mainframe.choice3.grid_forget()
def show_1():
    mainframe.choice1.grid(row=0, sticky=W + E, padx=(1), pady=(1))
def show_2():
    mainframe.choice2.grid(row=1, sticky=W + E, padx=(1), pady=(1))
def show_3():
    mainframe.choice3.grid(row=2, sticky=W + E, padx=(1), pady=(1))

#update gold value
def update_gold(gold_to_add):
    global GOLD
    if gold_to_add == 0:    #0 as a shorthand for "lose all gold"
        GOLD = 0
    else:
        GOLD=GOLD+gold_to_add
    mainframe.stats4.config(text="Gold = {}".format(GOLD))


def fight(enemy_stam, enemy_str):
    #you and enemy roll 2d6 + strength. On win, you deal 2 damage to enemy, on lose they deal 2 damage to you
    global STAM
    text = ""
    while enemy_stam >0 and STAM > 0:
        text = text + "Your strength: {}, Your stamina: {}\n" \
               "Enemy strength: {}, Enemy Stamina: {}".format(STR, STAM, enemy_str, enemy_stam)
        a=randint(1,6)
        b=randint(1,6)
        c=randint(1,6)
        d=randint(1,6)
        hero_roll = STR + a + b
        enemy_roll = enemy_str + c + d
        text = text + "\nYou roll: '{} + {} + {} STR = {}'".format(a,b,STR,hero_roll) + \
               "\nEnemy roll: '{} + {} + {} STR = {}'".format(c,d,enemy_str,enemy_roll)
        if hero_roll == enemy_roll:
            text = text + "\nDRAW\n\n"
        elif hero_roll > enemy_roll:
            text = text + "\nWIN\n\n"
            enemy_stam = enemy_stam - 2
        else:
            text = text + "\nLOSE\n\n"
            STAM=STAM-2
    mainframe.stats1.config(text="Stamina = {}".format(STAM))
    if STAM <= 0:
        text = text + "You have been slain.\n"
        return "defeat", text
    else:
        text = text + "The enemy is slain.\n\n"
        return "victory", text



########### bulk of text
def death_choices():
    global death_text, choice1, choice2, choice3, STAGE
    #make sure all options visible
    show_1(), show_2(), show_3()
    death_text = "\n\nYour adventure ends here.\nWould you like to try again from the start?"
    choice1="Yes, please! And with the same stats, if you don't mind"
    choice2="Yes, and roll me new stats as well"
    choice3="No. I'm done."
    STAGE=-1


def intro():
    global choice1, choice2, choice3, textbox, STAGE
    textbox="You've sat quietly for hours. The thunderous rumble of hooves and the creaks of the wagon wheels have been more than sufficient to occupy your mind. "\
            "\nYou're in a transport cart. It's dark except for the light seeping through the cracks of the wooden walls. The bench you're sitting on is uncomfortable, and you have to shift your weight periodically to keep your legs from falling asleep."\
            "\nYour hands are bound tightly with rope. There are two other men in the cart. One beside you, propped against the corner, fast asleep. The other man sits across from you, clearly deep in thought."\
            "\nHe's surprisingly well dressed for a prisoner, but his bindings are the same as yours. As you're looking him over, he looks you in the eyes and raises his hands to point at you."\
            '\n"So, what are you in for?"'
    choice1 = "''Theft.''"
    choice2 = "''Murder.''"
    choice3 = "''I haven't done anything. This is all some big mistake.''"

def stage0():
    global choice1, choice2, choice3, textbox, STAGE, GOLD
    textbox="''Must've been something serious for you to end up here. We're off to the headsman, you know?'' he says with candor.\n''I wouldn't worry too much though. I've got a feeling we'll be getting out of this one pretty soon.''" \
            "\nNot a moment later, the cart comes to an abrupt halt. You hear shouting and fighting, before the back door of the cart swings open." \
            "\n''Right on time!'' the well dressed man exclaims.\nAll three of you exit the cart. A group of well armed men cut your bindings free.\nThese are not the guards who were escorting you. These are bandits, or mercenaries. The cart driver and guards lay bleeding out on the ground" \
            "\n''It's your lucky day, friend'' the well dressed man says with a grin. ''You're free to go. Shame about the guards, but my boys are ruthless.''" \
            "\n''There's a town just up the road, only an hours walk or so. You'd best not stick around, but you're no enemy of mine,'' he says." \
            "\n''Oh, and here's something for the journey. It's dangerous out there''\nThe well dressed man tosses you a knife and a small pouch of coins. He raises a finger to his brow in a mock salute, before taking a horse and setting off with his gang of men."
    choice1 = "Search the bodies of the guards for more loot"
    choice2 = "Walk down the road to the town the man mentioned"
    choice3 = "Head off into the forest"
    STAGE=1
    update_gold(5)

#try to loot guards, if success, go to stage 2a, if fail go to stage 2b
def stage1():
    global choice1, textbox, STAGE
    textbox="Any opportunity to get your grubby fingers on more loot is a worthwhile one!" \
            "\nUnfortunately, not all of these guards are as dead as they seem." \
            "\n\nTEST YOUR LUCK!"
    choice1="Roll LUCK"
    hide_2(), hide_3()
    STAGE=2

def stage2a():
    global textbox, GOLD
    textbox="You roll a {} and a {}.\n{} <= {} (LUCK). LUCK goes down by 1.".format(ROLL1, ROLL2, ROLL1+ROLL2, LUCK+1) + "\nSuccess!\n\nA guard in the throes of death tries to lash out at you with a blade, but you nimbly dodge out of the way. You help yourself to the definitely dead ones, and find yourself 5 gold richer for your troubles." \
            "\nNow, with your pack heavy with gold, you can begin your travels in earnest."
    update_gold(5)


def stage2b():
    global textbox, STAM
    textbox="You roll a {} and a {}.\n{} > {} (LUCK) ".format(ROLL1, ROLL2, ROLL1+ROLL2, LUCK) + "\nFailure!\n\nA guard in the throes of death tries to lash out at you with a blade, driving it into your leg. You take 2 points of damage." \
            "\nYou think it's best to leave the bodies alone, lest you end up with more than just a stab wound."
    STAM=STAM-2
    mainframe.stats1.config(text="Stamina = {}".format(STAM))


def stage2():
    global choice1, choice2, STAGE
    choice1 = "Walk down the road to the town the man mentioned"
    choice2 = "Head off into the forest"
    show_2()
    STAGE=3

#go in woods
def stage3():
    global choice1, textbox, STAGE
    textbox="Not long after setting off into the forest, you realize you are totally lost.\nEach tree looks like the one before it. Have you been here before? No... Surely you're not going in circles.\nEventually, the sun sets behind the thick foliage, and you are plunged into darkness."
    hide_2(), hide_3()
    choice1="Onwards! To adventure!"
    STAGE=4

#die in woods
def stage4():
    global textbox
    death_choices()
    textbox="You find yourself whipping your head from side to side, squinting to make out any shape in the darkness of the forest. Every twig that breaks underfoot sends a chill up your spine. Your heart races in your chest. What are you doing out here?" \
            "\nWith that thought, you hear a low growling. A wolf blocks your path. You ready your knife, but you stand no chance against this ferocious beast. It leaps at you, and knocks you to the ground." \
            "\nYou stab in vain, before the beast delivers the killing blow. It rips out your throat, and you go limp." + death_text

#spot man
def stage5():
    global textbox, choice1, choice2, choice3, STAGE
    textbox = "The walk along the road to town is rather peaceful. The weather is nice, and it's even nicer now that you're no longer imprisoned. You wonder what this town will have to offer. Maybe you can find work. Maybe you can put your life of heinous crimes behind you. Maybe settle down and raise a family." \
              "\nAt that moment, you spot a man laying down in the road, clutching his side. Is he wounded? Maybe he was robbed by the same brigands that freed you."
    show_2(), show_3()
    choice1 = "Stop and help the man"
    choice2 = "Attempt to rob the man, surely he's got SOMETHING of value"
    choice3 = "Ignore the man and continue on your journey"
    STAGE=6

#help man
def stage6a():
    global textbox, choice1, choice2, choice3, STAGE
    textbox = "You rush to the man and say a silent prayer, hoping he's okay.\nHe's wincing with pain. You crouch down and ask if he's hurt." \
              "\n''No,'' he says, ''but you're going to be, if you don't cough up your money.''" \
              "\nQuick as a flash, the man is on his feet. He flashes a dagger and pulls a sly grin." \
              "\n''So what's it going to be? Your money or your life.''"
    choice1 = "Fight the man"
    choice2 = "Hand over all your gold"
    choice3 = "Try to run away"
    STAGE=7

#rob man
def stage6b():
    global textbox, GOLD
    textbox = "There's no easier prey than the injured. You saunter up to the man on the ground and place your knife under his chin." \
              "\n''Whoa whoa whoa whoa! Take it easy!'' the man cries out." \
              "\n''I'm just a kid! I'm only 19!'' he pleads. ''Look, take my money, I've just been sticking up travellers that come through here. I've got 5 gold pieces on me that's all I've got I swear.''" \
              "\nYou pocket the money and sheath your blade. Can you believe this degenerate? Taking advantage of a traveller's good will for his own financial gain." \
              "\nYou spit on the ground in front of the man and curse at him."
    update_gold(5)
    stage6()

#ignore man
def stage6c():
    global textbox
    textbox = "It's not your job to play doctor. After all, that man will be fine on his own. It's a dog eat dog world out here, and you're looking out for numero uno.\n"
    stage6()

#keep heading to town
def stage6():
    global choice1, STAGE
    hide_2(), hide_3()
    choice1="Keep heading to the town"
    STAGE=10

#fight robber
def stage7a():
    global textbox
    result, text = fight(9,9)
    textbox = text
    if result == "victory": #you win
        textbox = textbox + "After a hard fight, the robber lays in a bloodied heap on the ground. You brush yourself off and help yourself to whatever gold he had on his person. You find 10 gold pieces in a pouch on his waist."
        update_gold(10)
        stage6()
    else: #you lose
        death_choices()
        textbox = textbox + death_text


#give robber gold
def stage7b():
    global textbox
    textbox = "You're no fool. A handful of coins is not worth dying over. You turn out your pockets and give them to the robber." \
              "\n''That wasn't so hard was it?'' he says with feigned sympathy. ''Now, get the fuck out of here,'' he barks, gesturing you onward with his knife." \
              "\n\nYou lose {} gold pieces".format(GOLD)
    update_gold(0)
    stage6()

#flee robber
def stage7c():
    global textbox, choice1, STAGE
    textbox = "While you're certainly not the most quick-witted (who could have expected a robber to be out on this uninhabited road of all places!), you are most assuredly quick of foot. Why fight when you can flee? \n\nTEST YOUR LUCK!"
    choice1="Roll LUCK"
    hide_2(), hide_3()
    STAGE = 8

def stage8a():
    global textbox, GOLD
    textbox = "You roll a {} and a {}.\n{} <= {} (LUCK). LUCK goes down by 1.".format(ROLL1, ROLL2, ROLL1 + ROLL2, LUCK + 1) + \
              "\nSuccess!\nWith a quick shove, you topple the would-be robber. As he's picking himself up, you're already well away from him. You turn back to see him shaking his fist and yelling expletives."
    stage6()

def stage8b():
    global textbox, choice1, STAGE, STAM
    textbox="You roll a {} and a {}.\n{} > {} (LUCK) ".format(ROLL1, ROLL2, ROLL1+ROLL2, LUCK) + \
            "\nFailure!\n\nYou try to slip past the robber but he grabs the back of your shirt and drives his knife into your side. You take 4 points of damage and drop to one knee." \
            "\nThe robber stands over you with a wicked grin, flipping his knife in one hand. He prepares to stab you again."
    choice1 = "Stand and fight!"
    STAM=STAM-4
    mainframe.stats1.config(text="Stamina = {}".format(STAM))
    STAGE=9

def stage10():
    global textbox, choice1, choice2, STAGE
    textbox="After some walking, you find yourself at the gates of a village. Calling it a 'Town' would be disingenuous, this place is a dump. " \
            "However, it's a far better sight than the inside of a prison cart, or a headsman's block.\nThere's a bar near the front of the town, and further on, market stalls are setup. " \
            "There's a blacksmith, and a tannery. Surely someone like yourself could find work in a place like this, but that is a tale for another day."
    #while technically this is a "victory" it's still the end of the game
    death_choices()
    textbox = textbox + death_text


####
#fire it up
w1 = Tk()
introscreen=StartingScreen(w1)
mainloop()