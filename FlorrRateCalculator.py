while True:
    FarmedRarity = input("Do you farm ultra mobs or mythic mobs? (ultra/mythic)").strip().lower()
    if FarmedRarity == "mythic":
        Urate = 0
        while True:
            Mrate = input("Insert rate of mythic drop of desired petal as a percentage from the farmed mob e.g. glass from mythic soldier ant would be 0.9:")
            try:
                Mrate = float(Mrate)/100
            except Exception:
                print("invalid")
                continue
            break
        while True:
            Lrate = input("Insert rate of legendary drop of desired petal as a percentage from the farmed mob:")
            try:
                Lrate = float(Lrate)/100
            except Exception:
                print("invalid")
                continue
            break
    elif FarmedRarity == "ultra":
        while True:
            Urate = input("Insert rate of ultra drop of desired petal as a percentage from the farmed mob e.g. glass from ultra soldier ant would be 0.5:")
            try:
                Urate = float(Urate)/100
            except Exception:
                print("invalid")
                continue
            break
        while True:
            Mrate = input("Insert rate of mythic drop of desired petal as a percentage from the farmed mob:")
            try:
                Mrate = float(Mrate)/100
            except Exception:
                print("invalid")
                continue
            break
        while True:
            Lrate = input("Insert rate of legendary drop of desired petal as a percentage from the farmed mob:")
            try:
                Lrate = float(Lrate)/100
            except Exception:
                print("invalid")
                continue
            break
    elif FarmedRarity not in ["mythic", "ultra"]:
        print("invalid, try again!")
        continue
    break
if (Urate+Mrate+Lrate) > 1:
    print("The total rate for all drops cannot exceed 100%, please rerun and enter the correct values")
else:
    while True:
        UltrasNeeded = input("How many ultras do you want?")
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