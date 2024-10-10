import random as rd
import math
counter = 0
counter2 = 0
#y = a(x-x0)^2
def east_input():
    launches = int(input("how many missiles would you like to launch east? "))
    return launches

def north_input():
    launches = int(input("how many missiles would you like to launch north? "))
    print_space()
    return launches

def eastern_launch(e_launches):
    alarm_text = ''
    city_list = []
    for launch in range(e_launches):
        a,b,c,launch_point = missile_fire()
        land_point,bool = detect(a,b,c,launch_point,launch)
        e_city = e_cities()
        if bool == True:
            text,counter,cities_list_alarmed = alarm(e_city,land_point,launch)
            alarm_text += text 
            if len(cities_list_alarmed)>0:
                city_list.append(cities_list_alarmed)
        else:
            continue
    print_space()
    try:
        return alarm_text, counter,city_list
    except UnboundLocalError:
        return alarm_text,0,city_list
    
def northern_launch(n_launches):
    alarm_text2 = ''
    city_list2 = []
    global counter2
    for launch in range(n_launches):
        a,b,c,launch_point = missile_fire()
        land_point,bool = detect(a,b,c,launch_point,launch)
        n_city = n_cities()
        if bool == True:
            text2,counter2,cities_alarm_list2 = alarm(n_city,land_point,launch)
            alarm_text2 += text2
            if len(cities_alarm_list2)>0:
                city_list2.append(cities_alarm_list2)
        else:
            continue
    print_space()
    try:
        return alarm_text2, counter2,city_list2
    except UnboundLocalError:
        return alarm_text2,0, city_list2
    
def missile_fire():
    launch_point = rd.uniform(0.0, 10.0)  # Generate random number
    launch_point_round = round(launch_point,1) # Print the rounded number
    a = -0.1
    #b = rd.randint(0,6)
    b = rd.uniform(.01,8.8)
    b = round(b,2)
    c = 0
    return a,b,c,launch_point_round

def detect(a,b,c,launch_point_round,launch_number):
    disc = (b**2) - (4*a*c)
    pos_root = (-b -math.sqrt(disc))/(2*a)
    pos_root = round(pos_root,2)
    flight_dist = pos_root
    land_point = flight_dist-launch_point_round
    print(f"missile {launch_number+1}: lands {land_point:.1f} km outside gaza")
    if land_point>0:
        return land_point,True
    else:
        return land_point,False

def e_cities():
    e_city = {
        "Sderot":{
            "lower" : 1.9,
            "upper" : 4.5
        },
        "Ibim":{
            "lower":4.6,
            "upper":5.0
        },
        "Bror Hayil":{
            "lower":7.45,
            "upper": 8.35
        },
        "Tlamim":{
            "lower": 9.88,
            "upper": 11.05
        },
        "Sde David":{
            "lower": 11.31,
            "upper": 12.36
        },
        "Kiryat Gat":{
            "lower": 18.93,
            "upper": 21.81
        },
        "Bet Shemsh 3":{
            "lower": 43.05,
            "upper": 44.7
        },
        "Bet Shemesh 1":{
            "lower": 44.7,
            "upper": 45.86
        },
        "Beitar Illit":{
            "lower": 53.69,
            "upper": 56.35
        },
        "Ora":{
            "lower": 59.25,
            "upper": 61.58
        },
        "Western Jerusalem/Bait Vagan":{
            "lower": 61.6,
            "upper": 65.15
        },
        "Givat Ram/Central Jerusalem":{
            "lower": 65.15,
            "upper": 66.5
        },
        "Rehavia":{
            "lower": 66.5,
            "upper": 68.05
        },
        "Old City":{
            "lower": 68.05,
            "upper": 69.34
        },
        "Ma'ale Adumin":{
            "lower": 73.72,
            "upper": 76.3
        }

    }
    return e_city

def n_cities ():
    n_city = {
        "Netiv HaAsara":{
            "lower":.7,
            "upper": 1.9
        },
        "Zikim":{
            "lower" : 15.8,
            "upper" : 16.6
        },
        "Ashkelon":{
            "lower" : 18.5,
            "upper" : 25.33
        },
        "Ashdod":{
            "lower" : 23.22,
            "upper" : 28.95
        },
        "Port Ashdod":{
            "lower": 29,
            "upper": 32.65
        },
        "Rishon Letzion":{
            "lower": 48.84,
            "upper": 52.44
        },
        "Bat Yam":{
            "lower": 52.45,
            "upper": 57
        },
        "Jaffa":{
            "lower":57,
            "upper":64
        },
        "Tel Aviv":{
            "lower":64,
            "upper":73.4
        }
    }
    return n_city

def list_creator(alarm_text,alarm_text2,counter,counter2):
    counters = [counter,counter2]
    text = [alarm_text,alarm_text2]
    return text,counters

def alarm(city,land_point,launch_number):
    alarm_cities = ''
    alarm_cities_list = []
    global counter 
    for city,bounds in city.items():
        if bounds["lower"] < land_point < bounds["upper"]:
           text = f"!!!missile {launch_number+1}: alarm raised in the city of {city}!!!"
           alarm_cities+= text + "\n"
           alarm_cities_list.append(city)
           counter = counter + 1
    return alarm_cities,counter,alarm_cities_list

def alarm_or_safe(counter,alarm_text):
    if counter == 0:
        print("all eastern cities are safe")
    elif counter > 0:
        send_alarm(alarm_text)
def correct_alarm_counter(counters):
    counters.append(counters[1]-counters[0])
    counters.pop(1)
    return counters

def send_alarm(text):
    print(text)

def all_alarms(cities_alarm_list,cities_alarm_list2):
    all_cities_list = cities_alarm_list + cities_alarm_list2
    flat_list = [city for sublist in all_cities_list for city in sublist]
    unique_cities = list(set(flat_list))
    if counter>0 or counter2>0:
        print("Alarms raised in: ", end = '')
        for i,alarm in enumerate(unique_cities):
            if alarm == unique_cities[-1]:
                print(f"{alarm}")
            else: 
                print(f"{alarm}, ", end='')

def print_space():
    print("="*80)

def main():
    alarm_text = ''
    alarm_text2 = ''
    e_launches = east_input()#launches = rd.randint(1,5)
    n_launches = north_input()
    print(f"{e_launches+n_launches} missiles have been fired total")
    print_space()

    alarm_text,counter,cities_alarm_list = eastern_launch(e_launches)
    alarm_text2,counter2,cities_alarm_list2 = northern_launch(n_launches)
    
    text, counters = list_creator(alarm_text,alarm_text2,counter,counter2)
    correct_alarm_counter(counters)
    for enum,count_num in enumerate(counters):
        alarm_or_safe(count_num,text[enum])
        print(f"{count_num} alarms have been raised")
        print_space()
    all_alarms(cities_alarm_list,cities_alarm_list2)
main()
