while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("throw the coin and Enter heads or tails here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")