import random

print("Welcome to BullsEye : Guess The Number Game")
print("\nLet's Get Started, Here are the rules:")
print("\t1. You have to guess the number from given range")
print("\t2. You can have total 5 chances")
print("\t3. You can select the difficulty level")
print("\t4. Levels:  1. Easy Level (1-25)  2. Medium Level (1-50)  3. Hard Level (1-100)\n")

rNum = None
uNum = None

n = int(input("Select your level: "))

while(n>3):
  n = int(input("Please enter valid level: "))

if(n==1):
  print("\nGuess the number between range 1 to 25\n")
  rNum = random.randrange(1,25)
elif(n==2):
  print("\nGuess the number between range 1 to 50\n")
  rNum = random.randrange(1,50)
elif(n==3):
  print("\nGuess the number between range 1 to 100\n")
  rNum = random.randrange(1,100)

flag = 0
attempts = 5

while(flag==0):
  if(attempts==0):
    print(f"Game Over!!! Correct answer is: {rNum}")
    flag=1
    break

  uNum = int(input("Enter your guess num: "))

  if(attempts>0):
    if(uNum==rNum):
      print("Yay! Your guess is Correct. You're awesome!!!\n")
      flag=1
      break
    else:
      attempts -= 1
      print(f"Incorrect Guess. Please try again. Remaining attempts: {attempts}") 
      diff = abs(rNum-uNum)

      if(diff>0 and diff<=5):
        print("Hint: You're very close\n")
      elif(diff>5 and diff<=15):
        print("Hint: You are quite near\n")  
      elif(diff>15):
        print("Hint: You're too far\n")

        
      

    




