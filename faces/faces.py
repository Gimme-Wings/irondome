def convert(text):
    if ":)" or ":(" not in text:
        print(text)
    if ":)" in text:
        text = text.replace(":)","🙂")
        print(text)

    if ":(" in text:
        text = text.replace(":(","🙁")
        print(text)
        return 0


def main ():
    emoji = input("input: ")
    convert(emoji)

main()
