def convert(text):
    if ":)" or ":(" ! in text:
      return text

    if ":)" in text:
        text = text.replace(":)","🙂")


    if ":(" in text:
        text = text.replace(":(","🙁")






def main ():
    emoji = input("input: ")
    new=convert(emoji)
    print(new)

main()

