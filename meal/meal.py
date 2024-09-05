def main():
    time = input("What time is it? ")
    convert(time)
    print(time)

def convert(clock):
    type = clock.find(":")
    hour = float(clock[0:type])
    minute = float(clock[type+1:])
    clock = hour+(minute / 60)
    return clock

if __name__ == "__main__":
    main()


#7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
