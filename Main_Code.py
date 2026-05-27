gender =input ("Are you Male/Female?\n")
if gender.lower() == "male":
    print ("""Hello Sir, Welcome to Xenon's Caffee!
I am an Autonomous Coffee Barista.
Sir, do you want the menu for today?""")
else:
    print ("""Hello Ma'am, Welcome to Xenon's Caffee!
I am an Autonomous Coffee Barista.
Ma'am, do you want the menu for today?""")

confirm= input ("Yes/No: ")
if confirm.lower() == "yes":
    print ("""Here is our Menu sir:
          
Hot Coffee          Cold Coffee            Tea               Bakery & Desserts""")
else:
    print ("Thank You Sir, Visit Us Again!")
more_menu= input ("Which one do you want?")
