def main():
    time = input("What time is it? ")
    convert(time)
    print(time)

def convert(time):
    type = time.find(":")
    hour = float(time[0:type])
    minute = float(time[type+1:])
    time = hour+(minute / 60)


if __name__ == "__main__":
    main()


#7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
