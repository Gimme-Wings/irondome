my_dict = {}
my_dict["cat"]= "gatto"
my_dict["dog"]= "chien"
#or
my_dict2 = {
    "key 1": "value 1",
    "key 2": "value 2"
}
word = input("input a random word")
if word in my_dict:
    print("translation: ", my_dict[word])
else:
    print("word not found")

