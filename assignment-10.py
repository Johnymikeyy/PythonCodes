#Estimating the risk of death from coronavirus

age = int(input("Are you a cigarette addict older than 75 years old?\n"))
chronic = input("Do you have a severe chronic disease?\n").capitalize().strip()
immune = input("Is your immune system too weak?\n").capitalize().strip()

if age >75 or chronic == "Yes" or immune == "Yes":
    print("You are in risky group")
else:
    print("You are not in risky group")