name=input ("May I know your name? ")
print ("Hello," ,name+ """. Welcome to Xenon's Caffee!
I am an Autonomous Coffee Barista.
Sir, do you want the menu for today?""")

confirm= input ("Yes/No: ")
if confirm.lower() == "yes":
    print ("""Here is our Menu sir:
          
Hot Coffee          Cold Coffee            Tea               Dessert
""")
else:
    print ("Thank You Sir, Visit Us Again!")
    exit ()

more_menu= input ("Which one do you want? ")
if more_menu.lower()=="hot coffee":
    print ("Name:",name,"Order: One Hot Coffee.","Everthing Okay Sir?")


elif more_menu.lower()=="cold coffee":
    print ("Name:", name,"Order: One Cold Coffee.","Everthing Okay Sir?")

elif more_menu.lower()=="tea":
    print ("Name:", name,"Order: One Tea.","Everthing Okay Sir?")

elif more_menu.lower()=="dessert":
    print ("Name:", name,"Order: One Dessert.","Everthing Okay Sir?")
else:
    print ("Sorry, we don't have that item!")
    exit()

yes_no=input ("Yes/No: ")
if yes_no.lower()=="yes":
    print("Thank You,",name+". Your",more_menu,"will be prepared in few minutes!")
else:
    print ("See you again then!")


