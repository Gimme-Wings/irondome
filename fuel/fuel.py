def main():
    value = get_int()
    tried(value)

def get_int():
    perc = input("Fraction: ")
    return perc

def tried(value):
    try:
        a = value[0]/value[2]
    except ValueError:
        
