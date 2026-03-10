#!/user/bin/env python3

from random import randint


def roll_dice():
     return randint(1,6)


def generate_target_number(lower_limit=17, upper_limit=29):
    return randint(lower_limit, upper_limit)


if __name__ == "__main__":
   target_number = generate_target_number()

   print(f'The target number is {target_number}')
   print()

    #set total to zero

#FOREEVER

   # Roll the dice

    #add the roll to total

    #tell the user what the total is.

     #As the user if they want to stop

     #if the user want to stop EXIT

     # display the final scores -
#     Differnce if within 5 , or you lose

