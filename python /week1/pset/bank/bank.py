def main ():
    greeting = input("Greetings: ")
    greeting = greeting.lower().lstrip()
    eval(greeting)


def eval(response):
    if "hello" in response:
        print("$0")
    elif "h" in response[0]:
        print("$20")
    else:
        print("$100")

main()
