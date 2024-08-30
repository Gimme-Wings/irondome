def convert(text):
    text
    if ":)" in text:
        text.replace(":)","🙂")
        print(text)
    if ":(" in text:
        text.replace(":(","🙁")
        print(text)

def main ():
    emoji = input("input: ")
    convert(emoji)

main()
