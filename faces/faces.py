def convert(text):
    if ":)" in text:
        text = text.replace(":)","🙂")
        return text

    if ":(" in text:
        text = text.replace(":(","🙁")
        return text





def main ():
    emoji = input("input: ")
    new=convert(emoji)
    print(new)

main()

