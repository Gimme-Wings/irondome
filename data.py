person1 = {"name": "alice", "height": 165,"weight": 68,"age":29}
person2 = {"name": "bob", "height": 150,"weight": 75,"age":35}
person3 = {"name": "jon", "height": 175,"weight": 58,"age":45}

people = [person1,person2,person3]

for person in people:
    print(person["name"])

height = 0
for person in people:
    height += person["height"]

print("average is ", height/len(people))