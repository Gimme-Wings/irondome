def convert(text):
    if ":)" in text:
        text = text.replace(":)","🙂")
        print(text)
        return 0
    if ":(" in text:
        text = text.replace(":(","🙁")
        print(text)
        return 0

def main ():
    emoji = input("input: ")
    convert(emoji)

main()
