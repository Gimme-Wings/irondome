def convert(text):
    if ":)" or ":(" not in text:
      return text

    if ":)" in text:
        text = text.replace(":)","🙂")


    if ":(" in text:
        text = text.replace(":(","🙁")

    print(text)




def main ():
    emoji = input("input: ")
    convert(emoji)

main()

