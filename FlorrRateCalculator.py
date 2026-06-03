while True:
    FarmedRarity = input("Do you farm ultra mobs or mythic mobs? (ultra/mythic)").strip().lower()
    if FarmedRarity == "mythic":
        Urate = 0
        Mrate = float(input("Insert rate of mythic drop of desired petal as a percentage from the farmed mob e.g. glass from mythic soldier ant would be 0.9:"))/100
        Lrate = float(input("Insert rate of legendary drop of desired petal as a percentage from the farmed mob:"))/100
    elif FarmedRarity == "ultra":
        Urate = float(input("Insert rate of ultra drop of desired petal as a percentage from the farmed mob e.g. glass from ultra soldier ant would be 0.5:"))/100
        Mrate = float(input("Insert rate of mythic drop of desired petal as a percentage from the farmed mob:"))/100
        Lrate = float(input("Insert rate of legendary drop of desired petal as a percentage from the farmed mob:")) / 100
    elif FarmedRarity not in ["mythic", "ultra"]:
        print("invalid, try again!")
        continue
    break
while True:
    UltrasNeeded = int(input("How many ultras do you want?"))
    try:
        UltrasNeeded = int(UltrasNeeded)
    except Exception:
        print("Not a number")
        continue
    break
Mrate = Mrate+Lrate/65
Urate = Urate+Mrate/128
RequiredKills = int(UltrasNeeded/Urate)
print(f"On average, you need to kill {RequiredKills} {FarmedRarity}s to get {UltrasNeeded} ultra petals.")
