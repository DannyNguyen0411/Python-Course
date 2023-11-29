print("Welcome to the love calculator")

name_first = input("What is your name?\n")
name_second = input("What is the name of your crush?\n")

name_collector = name_first + name_second

t = name_collector.count("t")
r = name_collector.count("r")
u = name_collector.count("u")
e = name_collector.count("e")

true = int(t + r + u + e) * 10

l = name_collector.count("l")
o = name_collector.count("o")
v = name_collector.count("v")
e = name_collector.count("e")

love = int(l + o + v + e)

true_love = true + love

if (true_love <= 10 or true_love >= 90):
    print(f"Your score is: {true_love}, you go together like coke and mentos.")
elif(true_love >= 40 and true_love <= 50):
    print(f"Your score is: {true_love}, you are alright together.")
else:
    print(f"Your score is: {true_love}")
    redeem = input("Do you want to know more?")
    
    if redeem.lower() == "yes":
        d = name_collector.count("d")
        o = name_collector.count("o")
        w = name_collector.count("w")
        n = name_collector.count("n")

        down = int(d + o + w + n) * 10
         
        b = name_collector.count("b")
        a = name_collector.count("a")
        d = name_collector.count("d")


        bad = int(b + a + d)

        fake_love = down + bad

        if (fake_love < 10 or fake_love > 90):
            print(f"Your score is: {fake_love}, you are so downbad, that you want to rape your crush.")
        elif(fake_love >= 40 and fake_love <= 50):
            print(f"Your score is: {fake_love}, you actually simp for your crush.")
        else:
            print(f"Your score is: {fake_love}")
    else:
        print("Ok, that's your result!")

