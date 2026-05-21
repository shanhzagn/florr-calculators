# this program gives you the chance of crafting at least 1 petal of the desired rarity
DesiredRarity = input("insert the rarity you are trying to craft into e.g mythic ultra super")
PetalsAvailable = int(input("insert the number of petals you have to attempt"))
if DesiredRarity == "unusual":
    FailChance = int(0.36)
else:
    if DesiredRarity == "rare":
        FailChance = int(0.68)
    else:
        if DesiredRarity == "epic":
            FailChance = int(0.84)
        else:
            if DesiredRarity == "legendary":
                FailChance = int(0.92)
            else:
                if DesiredRarity == "mythic":
                    FailChance = int(0.96)
                else:
                    if DesiredRarity == "ultra":
                        FailChance = int(0.98)
                    else:
                        if DesiredRarity == "super":
                            FailChance = int(0.99)
                        else:
                            if DesiredRarity == "eternal":
                                FailChance = int(0.999)
                            else:
                                print("invalid input")
SuccessChance = int(1-FailChance)
PetalsLostPerAtt = int(2.5*FailChance+5*FailChance)
AverageAttempts = int(PetalsAvailable/PetalsLostPerAtt)
print(AverageAttempts)