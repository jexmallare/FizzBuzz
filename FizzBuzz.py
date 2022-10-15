#loop to a hundred
for i in range(1,101):

#if divisible by 3 and 5, print FizzBuzz
    if i%15 == 0:
        print("FizzBuzz")

#if divisible  by only 3, print Fizz
    elif i%3 == 0:
        print("Fizz")

#if divisible by only 5, print Buzz
    elif i%5 == 0:
        print("Buzz")

#else, just print the number
    else:
        print(i)
