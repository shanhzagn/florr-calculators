Mrate = float(input("Insert rate of mythic drop of desired petal as a percentage e.g. glass would be 0.9:"))/100
Wastedrate = float(input("Insert rate of below legendary drop as a percentage e.g. glass would be 4.5:"))/100
Lrate = float(1 - Mrate - Wastedrate)
Ultra = int(input("How many ultras do you want?"))
RequiredMythics = int(Ultra * 128)
RequiredKills = int(RequiredMythics / ((65 / Lrate) + (1 / Mrate)))
print(RequiredKills)