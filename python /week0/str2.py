#.lstrip() removbes from left rstrip removes from right
name = input ("whats your name? ").strip().title()
#or remove from line above and do name = name.strip()
first, last= name.split(" ")


print(f"hello, {name}")
