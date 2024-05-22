#!/usr/bin/env python3

def happy_new_year():
      # code goes here!
      counter = 10
      while (counter > 0):
          print(counter)
          counter-=1
          print("Happy New Year!")

  
def square_integers(int_list):
    # code goes here!
    return [num ** 2 for num in int_list]
    pass

def fizzbuzz(num=None):
    # code goes here!
    if num is None:
        for num in range(1, 101):
            print(fizzbuzz(num))
    else:
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return str(num)
