import random
name = input()

if(name != ""):
    print("あなたの運勢は…")
    fortune = ["大吉","吉","中吉","小吉","末吉","凶","平"]
    print(random.choice(fortune))
