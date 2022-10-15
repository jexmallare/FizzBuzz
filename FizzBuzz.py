#Loop up to a hundred
for i in range(1,101):
#if divisible by 3 and 5, return FizzBuzz
    if i%15 == 0:
        print("FizzBuzz")

#if divisible by 3, return Fizz
    elif i%3 == 0:
        print("Fizz")

#if divisible by 5, return Buzz
    elif i%5 == 0:
        print("Buzz")

#else, print only the number
    else:
        print(i)
#end
