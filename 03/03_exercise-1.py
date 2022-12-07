user_prompt = input("What country are you from: ")
user_prompt = user_prompt.strip()

match user_prompt:
    case 'USA' | 'usa':
        print("Hello")
    case 'India':
        print("Namaste")
    case 'Germany':
        print("Hallo")
    case _:
        print("Oh nice, I love ", user_prompt)
