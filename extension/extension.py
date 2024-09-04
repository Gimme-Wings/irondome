def main():
    name  = input("File name? ")
    name = name.lower().lstrip().rstrip()
    find()

#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip

def find(name):
    if "." not in name:
        print("application/octet-stream")
    else:
        if ".gif" in name:
            print("image/gif")
        elif ".jpg" or ".jpeg" in name:
            print("image/jpeg")
        elif ".png" in name:
            print("image/png")
        elif ".pdf" in name:
            print("application/pdf")
        elif ".txt" in name:
            print("text/plain")
        elif ".zip" in name:
            print("application.zip")

main()
