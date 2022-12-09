date = input("Enter today's date: ")
mood = input("How do you rate your mood today? ")
thoughts = input("Let your thoughts flow:\n ")

with open(f"{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)