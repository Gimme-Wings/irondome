import random as rd
import math
import numpy as np
import time
#!!different types of missiles!
#map pictures with alarms
#if launch distance is within a certain range, print where its being launched from and where to
#animation
counter = 0
counter2 = 0
#y = a(x-x0)^2
def east_input_short():
    launches = int(input("how many missiles would you like to launch east(short range)? "))
    return launches
def east_input_medium():
    launches = int(input("how many missiles would you like to launch east(medium range)? "))
    return launches
def east_input_long():
    launches = int(input("how many missiles would you like to launch east(long range)? "))
    direction = "e"
    return launches,direction

def north_input_short():
    launches = int(input("how many missiles would you like to launch north(short range)? "))
    return launches
def north_input_medium():
    launches = int(input("how many missiles would you like to launch north(medium range)? "))
    return launches
def north_input_long():
    launches = int(input("how many missiles would you like to launch north(long range)? "))
    direction = "n"
    print_space()
    return launches,direction

def eastern_launch(e_launches_short,e_launches_medium,e_launches_long,dir):
    alarm_text = ''
    city_list = []
    launch_dict = {e_launches_short:"short",
                   e_launches_medium:"medium",
                   e_launches_long:"long"}
    for num_launches, dist_label in launch_dict.items():
        if num_launches == 0:
            continue
        for launch in range(num_launches):
            three_points = missile_fire(dist_label,dir)
            land_point,bool = detect(three_points,launch)
            e_city = e_cities()
            if bool == True:
                text,counter,cities_list_alarmed = alarm(e_city,land_point,launch,dist_label)
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
    
def northern_launch(n_launches_short,n_launches_medium,n_launches_long,dir):
    alarm_text2 = ''
    city_list2 = []
    global counter2
    launch_dict = {n_launches_short:"short",
                   n_launches_medium:"medium",
                   n_launches_long:"long"}
    for num_launch,dist_label in launch_dict.items():
        if num_launch == 0:
            continue
        for launch in range(num_launch):
            three_points = missile_fire(dist_label,dir)
            land_point,bool = detect(three_points,launch)
            n_city = n_cities()
            if bool == True:
                text2,counter2,cities_alarm_list2 = alarm(n_city,land_point,launch,dist_label)
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
    
def missile_fire(dist,dir):#if possible split this into a separate function and call it radar
    if dist == "short":
        lower = 0.1
        upper = 3.0
    elif dist == "medium":
        lower = 3.0
        upper = 6.0
    elif dist == "long":
        lower = 6.0
        upper = 8.8
    
    if dir == "n":
        launch_point = rd.uniform(0,10.0)  # Generate random number
        launch_point_round = round(launch_point,1) 
       # launch_point_z = 0.0# Print the rounded number
        neg_root = -1*launch_point_round
    elif dir == "e":
        launch_point = rd.uniform(0,7.0)  # Generate random number(0,7.0)
        launch_point_round = round(launch_point,1) # Print the rounded number
        neg_root = -1*launch_point_round
    a = -0.1
    b = rd.uniform(lower,upper)#b = rd.randint(0,6)
    b = round(b,2)
    #theta = rd.randint(30,90)
    #pos_root = (b*10)-launch_point_round# b is times ten because if its .5 it will fly for 5 km
    point1_x = neg_root + .25 #flight_dist = pos_root - (neg_root)
    point1_y = (a*((point1_x-neg_root)*(point1_x-neg_root))) + b*(point1_x-neg_root)
    xy_list1 = [point1_x,point1_y]
    point2_x = neg_root + .5
    point2_y = (a*((point2_x-neg_root)*(point2_x-neg_root))) + b*(point2_x-neg_root)
    xy_list2 = [point2_x,point2_y]
    point3_x = neg_root + .4
    point3_y = (a*((point3_x-neg_root)*(point3_x-neg_root))) + b*(point3_x-neg_root)
    xy_list3 = [point3_x,point3_y]
    three_points = [xy_list1,xy_list2,xy_list3]
    return three_points

def detect(three_points,launch_number):#erase land_point and just find negative root and thats the launch point
    x1,y1 = three_points[0][0],three_points[0][1]
    x2,y2 = three_points[1][0],three_points[1][1]
    x3,y3 = three_points[2][0],three_points[2][1]
    A = np.array([[x1**2,x1,1],
                  [x2**2,x2,1],
                  [x3**2,x3,1]])
    B= np.array([y1,y2,y3])
    a,b,c = np.linalg.solve(A,B)
    a = round(a,2)
    b = round(b,2)
    disc = (b**2) - (4*a*c)
    pos_root = (-b - math.sqrt(disc))/(2*a)
    neg_root = (-b + math.sqrt(disc))/(2*a)
    pos_root = round(pos_root,2)
    neg_root = round(neg_root,2)
    land_point = pos_root+neg_root#change this here and work out if its correct us neg root
    print(f"missile {launch_number+1}: lands {land_point:.1f} km outside gaza")
    if land_point>0:
        return land_point,True
    else:
        return land_point,False

def e_cities():
    e_city = {
        "Sderot":{
            "lower" : 1.9,
            "upper" : 4.5,
            "time" : 15
        },
        "Ibim":{
            "lower":4.6,
            "upper":5.0,
            "time" :15
        },
        "Bror Hayil":{
            "lower": 7.45,
            "upper": 8.35,
            "time" : 30
        },
        "Tlamim":{
            "lower": 9.88,
            "upper": 11.05,
            "time" :30
        },
        "Sde David":{
            "lower": 11.31,
            "upper": 12.36,
            "time" : 30
        },
        "Kiryat Gat":{
            "lower": 18.93,
            "upper": 21.81,
            "time" : 45
        },
        "Bet Shemsh 3":{
            "lower": 43.05,
            "upper": 44.7,
            "time" : 90
        },
        "Bet Shemesh 1":{
            "lower": 44.7,
            "upper": 45.86,
            "time" : 90
        },
        "Beitar Illit":{
            "lower": 53.69,
            "upper": 56.35,
            "time" : 90
        },
        "Ora":{
            "lower": 59.25,
            "upper": 61.58,
            "time" : 90
        },
        "Western Jerusalem/Bait Vagan":{
            "lower": 61.6,
            "upper": 65.15,
            "time" : 90
        },
        "Givat Ram/Central Jerusalem":{
            "lower": 65.15,
            "upper": 66.5,
            "time" : 90
        },
        "Rehavia":{
            "lower": 66.5,
            "upper": 68.05,
            "time" : 90
        },
        "Old City":{
            "lower": 68.05,
            "upper": 69.34,
            "time" : 90
        },
        "Ma'ale Adumin":{
            "lower": 73.72,
            "upper": 76.3,
            "time" : 90
        }

    }
    return e_city

def n_cities ():
    n_city = {
        "Netiv HaAsara":{
            "lower":.7,
            "upper": 1.9,
            "time" : 15
        },
        "Zikim":{
            "lower" : 15.8,
            "upper" : 16.6,
            "time" : 15
        },
        "Ashkelon":{
            "lower" : 18.5,
            "upper" : 25.33,
            "time" : 30
        },
        "Ashdod":{
            "lower" : 23.22,
            "upper" : 28.95,
            "time" : 45
        },
        "Port Ashdod":{
            "lower": 29,
            "upper": 32.65,
            "time" : 45
        },
        "Rishon Letzion":{
            "lower": 48.84,
            "upper": 52.44,
            "time" : 90
        },
        "Bat Yam":{
            "lower": 52.45,
            "upper": 57,
            "time" : 90
        },
        "Jaffa":{
            "lower":57,
            "upper":64,
            "time" : 90
        },
        "Tel Aviv":{
            "lower":64,
            "upper":73.4,
            "time" : 90
        }
    }
    return n_city

def list_creator(alarm_text,alarm_text2,counter,counter2):
    counters = [counter,counter2]
    text = [alarm_text,alarm_text2]
    return text,counters
def story():
    print("")
    print("Its a quiet day in central israel")
    print("noone is excpecting anything but the usual...")
    print()
    time.sleep(5)

def alarm(city,land_point,launch_number,dist_label):
    alarm_cities = ''
    alarm_cities_list = []
    global counter 
    for city,bounds in city.items():
        if bounds["lower"] < land_point < bounds["upper"]:
           text = f"!!!missile {launch_number+1} {dist_label}: alarm in {city}, you have {bounds['time']} seconds to shelter!!!"
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
    e_launches_short = east_input_short()#launches = rd.randint(1,5)
    e_launches_medium = east_input_medium()#launches = rd.randint(1,5)
    e_launches_long,dir_e = east_input_long()#launches = rd.randint(1,5)
    n_launches_short = north_input_short()#launches = rd.randint(1,5)
    n_launches_medium = north_input_medium()#launches = rd.randint(1,5)
    n_launches_long,dir_n = north_input_long()#launches = rd.randint(1,5)
    print(f"{e_launches_short+e_launches_medium+e_launches_long+n_launches_short+n_launches_medium+n_launches_long} missiles have been fired total")
    print_space()

    alarm_text,counter,cities_alarm_list = eastern_launch(e_launches_short,e_launches_medium,e_launches_long,dir_e)
    alarm_text2,counter2,cities_alarm_list2 = northern_launch(n_launches_short,n_launches_medium,n_launches_long,dir_n)
    
    text, counters = list_creator(alarm_text,alarm_text2,counter,counter2)
    correct_alarm_counter(counters)
    story()
    for enum,count_num in enumerate(counters):
        alarm_or_safe(count_num,text[enum])
        print(f"{count_num} alarms have been raised")
        print_space()
    all_alarms(cities_alarm_list,cities_alarm_list2)
main()
