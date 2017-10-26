def collatz(number):
    if number % 2 == 0:
        num1 = number // 2
        print(num1)
        return num1
    elif number % 2 == 1:
        num2 = 3 * number + 1
        print(num2)
        return num2

def returner(num):
    while num != 1:
        num = collatz(num)

while True:
  try:
      myNum = int(input("Enter a number: "))
      returner(myNum)
      break
  except ValueError:
      print('You must enter an integer.')
