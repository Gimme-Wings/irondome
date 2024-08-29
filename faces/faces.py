def convert(emoji):
    if ":)" in emoji:
        print("🙂")
    if ":(" in emoji:
     print("🙁")

def main ():
    emoji = input("input: ")
    convert(emoji)

main()
