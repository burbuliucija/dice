import sys
import random

def user_input():
   action = sys.stdin.readline().strip()
   if action == "q":
      exit()
   elif action == "?help":
      print(f'''To roll a dice type xdy where
x - number of dice to roll
y - number of sides on the dice
Example: 1d20 rolls 1 dice with 20 sides.''')
      return user_input()
   else:
      try:
         if action[0] == "d":
            dice_amount = 1
            dice_sides = int(action[1:])
         else:
            action = action.split("d")
            dice_amount = int(action[0])
            dice_sides = int(action[1])
         assert dice_amount > 0
         assert dice_sides > 1
      except:
         print("Invalid syntax. Please try again.")
         return user_input()
      roll(dice_amount, dice_sides)

def roll(amount, sides):
   print(f'Rolling {amount}d{sides}...')
   if amount == 1:
      print(f'{random.randint(1, sides)}')
   else:
      rolls = []
      sum = 0
      for i in range(0, amount):
         roll = random.randint(1, sides)
         sum += roll
         rolls.append(str(roll))
      output = " + ".join(rolls)
      print(f'{output} = {sum}')
   return user_input
      

print(f''' 
      Welcome to
      _ ___         
   __| |_ _|___ ___ 
  / _` || |/ __/ _ \ 
 | (_| || | (_|  __/
  \__,_|___\___\___|
                    
  type ?help for help
  q to exit
''')

user_input()
