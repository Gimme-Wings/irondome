#check if even or odd by %
#get number
def main():
    x = int(input("which number? "))
#check if divisible by 2 fold all into z
    if is_even(x):
#check if remainder is 0
     print("even")
    else:
      print("odd")
      
def is_even(q):
   if q % 2 == 0:
        return True
   else:
        return False
main()
