password = input("Enter the password: ")

results = []
if len(password) >= 8:
    results.append(True)
else:
    results.append(False)

digit = False
for user_input in password:
    if user_input.isdigit():
        digit = True
results.append(digit)

uppercase = False
for user_input in password:
    if user_input.isupper():
        uppercase = True
results.append(uppercase)

print(results)
print(all(results))
if all(results):
    print("Strong Password")
else:
    print("Weak Password")
