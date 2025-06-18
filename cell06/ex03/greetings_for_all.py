def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It wass not a name.")

greetings('Trent')
greetings('Alexander')
greetings()
greetings(23)