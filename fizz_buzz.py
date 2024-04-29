"#fizzbuzz 3% == 0 , 5 %==0  && both , first 100 numbers"
for numb in range(1,101):
  if numb % 3 == 0 and numb % 5 == 0:
    print("FizzBuzz")
  elif numb % 3 == 0:
    print("Fizz")
  elif numb % 5 == 0:
    print("Buzz")
  else:
    print(numb)
