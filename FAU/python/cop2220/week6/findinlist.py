list1 = [2,4,"wr",10.5,"%"]
if 10.5 in list1:
    print("10.5 in it")
if "@" not in list1:
    print("9 not in it")
cap = 0
text = "I lOve napkins and noone can stop me"
for i in text:
    if ("o" in i) or ("O" in i):
        cap = cap + 1
print(cap)
