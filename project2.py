print("Welcome to Naomi's personality quiz! Today lets see which starbucks drink you are!")
print("For your answers, just type the letter of the option you pick!")
strawberryacailemonade_points=0
hotcoffee_points=0
icedchai_points=0
icedmatcha_points=0
vanillabeanfrapwithcaramel_points=0

answer1=input("Pick your favorite season: A, Spring, B, Summer, C, Fall, D, Winter: ")
if answer1=="A" or answer1=="a":
    icedmatcha_points+=1
elif answer1=="B" or answer1=="b":
    strawberryacailemonade_points+=1
elif answer1=="C" or answer1=="c":
    icedchai_points+=1
    vanillabeanfrapwithcaramel_points+=1
elif answer1=="D" or answer1=="d":
    hotcoffee_points+=1

answer2=input("Which of these sports would you rather try? A, tennis, B, soccer, C, basketball, or D, volleyball: ")
if answer2=="A" or answer1=="a":
    icedmatcha_points+=1
    hotcoffee_points+=1
elif answer2=="B" or answer1=="b":
    strawberryacailemonade_points+=1
elif answer2=="C" or answer1=="c":
    vanillabeanfrapwithcaramel_points+=1
elif answer2=="D" or answer1=="d":
    icedchai_points+=1

answer3=input("Which vacation would you choose? A, ski resort, B, cruise, C, beach, D, mountains: ")
if answer3=="A" or answer1=="a":
    hotcoffee_points+=1
    vanillabeanfrapwithcaramel_points+=1
elif answer3=="B" or answer1=="b":
    icedmatcha_points+=1
    strawberryacailemonade_points+=1
elif answer3=="C" or answer1=="c":
    strawberryacailemonade_points+=1
elif answer3=="D" or answer1=="d":
    hotcoffee_points+=1
    icedchai_points+=1

answer4=input("Which of these colors do you like the most? A, pink, B, dark blue, C, butter yellow, or D, green: ")
if answer4=="A" or answer1=="a":
    strawberryacailemonade_points+=1
elif answer4=="B" or answer1=="b":
    vanillabeanfrapwithcaramel_points+=1
    hotcoffee_points+=1
elif answer4=="C" or answer1=="c":
    icedchai_points+=1
elif answer4=="D" or answer1=="d":
    icedmatcha_points+=1

answer5=input("What's your favorite holiday? A, Christmas/Hanukkah, B, Halloween, C, Easter, D, Saint Patrick's Day: ")
if answer5=="A" or answer1=="a":
    vanillabeanfrapwithcaramel_points+=1
elif answer5=="B" or answer1=="b":
    icedchai_points+=1
    hotcoffee_points+=1
elif answer5=="C" or answer1=="c":
    strawberryacailemonade_points+=1
elif answer5=="D" or answer1=="d":
    icedmatcha_points+=1

if strawberryacailemonade_points > icedchai_points and strawberryacailemonade_points > icedmatcha_points and strawberryacailemonade_points > hotcoffee_points and strawberryacailemonade_points > vanillabeanfrapwithcaramel_points:
    print("Your personality is like a Strawberry Acai Lemonade! You are an outgoing and funny person who loves to hang out with their friends but is sometimes overbearing.")
elif icedchai_points > strawberryacailemonade_points and icedchai_points > icedmatcha_points and icedchai_points > hotcoffee_points and icedchai_points > vanillabeanfrapwithcaramel_points:
    print("Your personality is like a Iced Chai! You are chill and funny and maybe a little basic.")
elif icedmatcha_points > strawberryacailemonade_points and icedmatcha_points > icedchai_points and icedmatcha_points > hotcoffee_points and icedmatcha_points > vanillabeanfrapwithcaramel_points:
    print("Your personality is like an iced matcha! You are outgoing and probably love Labubus and have a Coach bag.")
elif hotcoffee_points > strawberryacailemonade_points and hotcoffee_points > icedmatcha_points and hotcoffee_points > icedchai_points and hotcoffee_points > vanillabeanfrapwithcaramel_points:
    print("Your personality is like a hot cup of coffee! You are a warm and caring person and probably a middle aged mom.")
elif vanillabeanfrapwithcaramel_points > strawberryacailemonade_points and vanillabeanfrapwithcaramel_points > icedchai_points and vanillabeanfrapwithcaramel_points > icedmatcha_points and vanillabeanfrapwithcaramel_points > hotcoffee_points:
    print("Your personality is like a Vanilla Bean Frappuchino with Caramel Drizzle! You are funny and adventurous but love a sweet treat and you are probably a middle school boy.")
else:
    print("You are a Unicorn Frappuchino! You are unique and vibrant!")