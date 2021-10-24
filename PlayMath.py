#Write a program to ask user for sum of two random numbers and check if their answer is correct
# TODO 
# 1. Generate two random numbers in a given range 
# 2. Get user input 
# 3. Calculate the actual sum 
# 4. Check if user input matches sum 
# 5. If it does say "Good Job!" else "Say the correct answer and 'Learn Addition!'"

import random

def generate_random_numbers():
  a=random.choice([0,1,2,3,4,5,6,7,8,9])
  b=random.choice([0,1,2,3,4,5,6,7,8,9])
  return a,b

def play_addition():
  a,b=generate_random_numbers()
  sum_of_nos = int(input(f"Enter sum {a}+{b} = "))
  actual_sum = a+b
  if sum_of_nos==actual_sum:
    print("cool")
  else:
    print("Learn Addition you monkey")
    
def play_sub():
  a,b=generate_random_numbers()
  if b>a:
    x=b
    b=a
    a=x
  sum_of_nos = int(input(f"Enter answer {a}-{b} = "))
  actual_sum = a-b
  if sum_of_nos==actual_sum:
    print("cool")
  else:
    print("Learn Addition you monkey")
    
    
play_addition()
play_sub()

