def convert(text):
    if ":)" or ":(" not in text:
      return text

    if ":)" in text:
        text = text.replace(":)","🙂")


    if ":(" in text:
        text = text.replace(":(","🙁")






def main ():
    emoji = input("input: ")
    convert(emoji)
    print(emoji)

main()

