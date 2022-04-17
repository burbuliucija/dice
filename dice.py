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
