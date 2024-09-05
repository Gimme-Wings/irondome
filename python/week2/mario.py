def main():
   x = ask_height()
   print_column(x)


def print_column(height):
   for _ in range(height):
      print("#")

def ask_height():
   ask = int(input("whats the height? "))
   return ask


main()
