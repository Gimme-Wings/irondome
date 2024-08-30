def convert(text):
    if ":)" in text:
        text = text.replace(":)","🙂")
        print(text)

    if ":(" in text:
        text = text.replace(":(","🙁")
        print(text)
        return 0
    else:
        print(text)

def main ():
    emoji = input("input: ")
    convert(emoji)

main()
