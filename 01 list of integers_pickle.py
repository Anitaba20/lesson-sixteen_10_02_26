# Task 1
# The user types in a list of integers. Pack the received data and save it to a file.
# After that, upload the data from the file to a new list.
#
# Úloha 1
# Používateľ zadá zoznam celých čísel. Zabaľte prijaté údaje a uložte ich do súboru.
# Potom načítajte údaje zo súboru do nového zoznamu.

# verzia1:
import pickle

numbers = [1, 2, 3, 4, 5]

with open("data.pkl", "wb") as file:
    pickle.dump(numbers, file)

with open("data.pkl", "rb") as file:
    loaded = pickle.load(file)

# verzia2:
import pickle

numbers = []

while True:
    cislo = int(input("Zadaj cislo: "))

    if cislo == -1:
        break

    numbers.append(cislo)


with open("data.pkl", "wb") as file:
    pickle.dump(numbers, file)


with open("data.pkl", "rb") as file:
    loaded = pickle.load(file)

print(loaded)

# verzia3:
import pickle

numbers = []
user = input("numbers: ")
parts = user.split(",")

for part in parts:
    part = part.strip()
    if part != "":
        numbers.append(part)

with open("data.pkl", "wb") as file:
    pickle.dump(numbers, file)

with open("data.pkl", "rb") as file:
    loaded = pickle.load(file)
    print(loaded)
