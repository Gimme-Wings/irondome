tran_dict = {"cat":"gatto", "dog":"perro", "bird":"pajaro"}
for key,value in tran_dict.items():#retrieve the tuple with key and value
    print("key", key)
    print("value",value)

staff ={"alan":"lecturer","emily":"prof","david":"teacher"}
del staff["alan"]
print(staff)
#good to check if the key is there
if "emily" in staff:
    del staff["emily"]
    print("deleted")
else:
    print("not a member")