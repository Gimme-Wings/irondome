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
    for launch in range(e_launches):
        a,b,c,launch_point = missile_fire()
        land_point,bool = detect(a,b,c,launch_point,launch)
        e_city = e_cities()
        if bool == True:
            text,counter = alarm(e_city,land_point,launch)
            alarm_text += text 
        else:
            continue
    print_space()
    try:
        return alarm_text, counter
    except UnboundLocalError:
        return alarm_text,0
def northern_launch(n_launches):
    alarm_text2 = ''
    global counter2
    for launch in range(n_launches):
        a,b,c,launch_point = missile_fire()
        land_point,bool = detect(a,b,c,launch_point,launch)
        n_city = n_cities()
        if bool == True:
            text2,counter2 = alarm(n_city,land_point,launch)
            alarm_text2 += text2
        else:
            continue
    print_space()
    try:
        return alarm_text2, counter2
    except UnboundLocalError:
        return alarm_text2,0 
    
def missile_fire():
    launch_point = rd.uniform(0.0, 10.0)  # Generate random number
    launch_point_round = round(launch_point,1) # Print the rounded number
    a = -0.1
    #b = rd.randint(0,6)
    b = rd.uniform(.01,6)
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
        "sderot":{
            "lower" : 1,
            "upper" : 2.5
        },
        "bror hayil":{
            "lower":3,
            "upper": 3.3
        },
        "tlamim":{
            "lower": 3.7,
            "upper":3.9
        },
        "kiryat gat":{
            "lower": 5,
            "upper": 6
        },
        "bet shemesh 5":{
            "lower": 25,
            "upper": 26
        },
        "bet shemsh 3":{
            "lower": 26,
            "upper": 26.5
        },
        "bet shemesh 1":{
            "lower": 26.5,
            "upper": 27
        },
        "beitar illit":{
            "lower": 32,
            "upper": 34
        },
        "ora":{
            "lower": 43,
            "upper": 44.5
        },
        "western Jerusalem/bait vagan":{
            "lower": 44.5,
            "upper": 47
        },
        "Givat ram/central jerusalem":{
            "lower": 47,
            "upper": 48
        },
        "Rehavia":{
            "lower": 48,
            "upper": 50
        },
        "Old city":{
            "lower": 50,
            "upper": 53
        }

    }
    return e_city

def n_cities ():
    n_city = {
        "zikim":{
            "lower" : 0.3,
            "upper" : 0.6
        },
        "ashkelon":{
            "lower" : 1,
            "upper" : 1.7
        },
        "ashdod":{
            "lower" : 2.5,
            "upper" : 3.2
        },
        "port ashdod":{
            "lower": 3.2,
            "upper": 3.6
        },
        "Rishon letzion":{
            "lower": 20,
            "upper": 25
        },
        "Bat yam":{
            "lower": 27,
            "upper": 32
        },
        "Jaffa":{
            "lower":32,
            "upper":35
        },
        "Tel aviv":{
            "lower":35,
            "upper":40
        }
    }
    return n_city

def list_creator(alarm_text,alarm_text2,counter,counter2):
    counters = [counter,counter2]
    text = [alarm_text,alarm_text2]
    return text,counters

def alarm(city,land_point,launch_number):
    alarm_cities = ''
    global counter 
    for city,bounds in city.items():
        if bounds["lower"] < land_point < bounds["upper"]:
           text = f"!!!missile {launch_number+1}: alarm raised in the city of {city}!!!"
           alarm_cities+= text + "\n"
           counter = counter + 1
    return alarm_cities,counter

def alarm_or_safe(counter,alarm_text):
    if counter == 0:
        print("all eastern cities are safe")
    elif counter > 0:
        send_alarm(alarm_text)

def send_alarm(text):
    print(text)

def print_space():
    print("="*80)

def main():
    alarm_text = ''
    alarm_text2 = ''
    e_launches = east_input()#launches = rd.randint(1,5)
    n_launches = north_input()
    print(f"{e_launches+n_launches} missiles have been fired total")
    print_space()
    alarm_text,counter = eastern_launch(e_launches)
    alarm_text2,counter2 = northern_launch(n_launches)
    text, counters = list_creator(alarm_text,alarm_text2,counter,counter2)
    for enum,count_num in enumerate(counters):
        alarm_or_safe(count_num,text[enum])
        print(f"{count_num} alarms have been raised")#fix the counter issue
        print_space()
main()
