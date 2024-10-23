staff ={"alan":"lecturer","emily":"prof","david":"teacher"}

removed = staff.pop("alan",None)#return None
if removed is None:
    print("this person is a staff member")
else:
    print(removed, "removed")