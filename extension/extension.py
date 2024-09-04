def main():
    name  = input("File name? ")
    name = name.lower().lstrip().rstrip()
    find(name)

#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip

def find(file):
    if "." not in file:
        print("application/octet-stream")
    else:
        if ".gif" in file:
            print("image/gif")
        elif ".jpg" or ".jpeg" in file:
            print("image/jpeg")
        elif ".png" in file:
            print("image/png")
        elif ".pdf" in file:
            print("application/pdf")
        elif ".txt" in file:
            print("text/plain")
        elif ".zip" in file:
            print("application/zip")

main()
