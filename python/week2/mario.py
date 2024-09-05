def main():
   while True: #induce a forvever loop
    height = int(input("what height? "))
    if height <= 0:
        continue
    else:
        return height
        for _ in range(height):
            print("#")

main()
