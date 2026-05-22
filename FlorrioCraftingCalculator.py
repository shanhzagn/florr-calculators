# this program gives you the chance of crafting at least 1 petal of the desired rarity and the average amount you craft
DesiredRarity = input("insert the rarity you are trying to craft into e.g mythic ultra super")
PetalsAvailable = int(input("insert the number of petals you have to attempt"))
if DesiredRarity == "unusual":
    FailChance = 0.36
elif DesiredRarity == "rare":
    FailChance = 0.68
elif DesiredRarity == "epic":
    FailChance = 0.84
elif DesiredRarity == "legendary":
    FailChance = 0.92
elif DesiredRarity == "mythic":
    FailChance = 0.96
elif DesiredRarity == "ultra":
    FailChance = 0.98
elif DesiredRarity == "super":
    FailChance = 0.99
elif DesiredRarity == "eternal":
    FailChance = 0.999
else: print("invalid input")
SuccessChance = 1-FailChance
MaxSuccesses = int(PetalsAvailable/5)
PetalsLostPerAtt = 2.5*FailChance+5*SuccessChance
AverageAttempts = int(PetalsAvailable/PetalsLostPerAtt)
ChanceForOne = 1-FailChance**AverageAttempts
AverageSuccesses = int(AverageAttempts)
print(AverageAttempts)
print(ChanceForOne)