password = input("Enter the password: ")

results = {}
if len(password) >= 8:
    results["length"] = True
else:
    results["length"] = False

digit = False
for user_input in password:
    if user_input.isdigit():
        digit = True
results["digits"] = digit

uppercase = False
for user_input in password:
    if user_input.isupper():
        uppercase = True
results["uppercase"] = uppercase

print(results)
print(all(results.values))
if all(results):
    print("Strong Password")
else:
    print("Weak Password")
