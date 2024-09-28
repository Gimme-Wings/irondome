my_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
def item_name():
    name = input("Item: ")
    name = name.lower()
    name = name.title()
    if name in my_dict:
        return name, True
    else:
        return name, False

def price(food_name):
    global total
    dollars = my_dict[food_name]
    total = total +  dollars
    print(f"Total: ${total:.2f}")



def main():
    while True:
        try:
            food, is_true = item_name()
        except EOFError:
            return False
        else:
            if is_true == True:
                price(food)
main()
