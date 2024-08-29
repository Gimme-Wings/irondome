#.lstrip() removbes from left rstrip removes from right
#title captilizes
name = input ("whats your name? ").strip().title()
#or remove from line above and do name = name.strip()
#splits name into two parts
first, last= name.split(" ")


print(f"hello, {first}")
