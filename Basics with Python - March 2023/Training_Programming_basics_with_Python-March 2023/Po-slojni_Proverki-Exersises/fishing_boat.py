budget = int(input())
season = input()
num_fishermans = int(input())

rent = 0

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if num_fishermans <= 6:
    rent *= 0.9
elif 7 <= num_fishermans <= 11:
    rent *= 0.85
elif num_fishermans > 12:
    rent *= 0.75

if num_fishermans % 2 == 0:
    if season != "Autumn":
      rent *= 0.95

diff = abs(budget - rent)

if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")

elif budget < rent:
    print(f"Not enough money! You need {diff:.2f} leva.")
