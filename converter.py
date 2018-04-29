print("How many kilometers did you bike ride today?")
kms = input()
miles = round(float(kms)/1.60934, 2)
print(f"Your {kms} kilometer ride is equal to {miles} miles.")