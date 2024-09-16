year = int(input("what year is it? "))

if (year % 4 == 0) and (year % 100 == 0 and year %400 != 0):
    print("leap")
else:
    print("not a leap year")


birth_year = 1770
leap_years_lived = 0
reg_years_lived = 0
for i in range(birth_year,2024):
    if (i % 4 == 0) and (i % 100 != 0 or i %400 == 0):
        leap_years_lived = leap_years_lived +1
    else:
        reg_years_lived = reg_years_lived +1

print(leap_years_lived)
print(reg_years_lived)
