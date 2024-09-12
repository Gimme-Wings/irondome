text = input("Input: ")
length = len(text)
text_list = list(text)
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u','U']

print("Output: ", end ='')
while length > 0:
        for i in text_list:
            if i in vowels:
                length = length -1
                continue
            else:
                print(f"{i}", end ='')
                length = length - 1

print()

