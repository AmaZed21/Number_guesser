import random
import time

#player set-up
points = 0

#Instructions
print("There are 3 levels")
time.sleep(1)
print('''You will start with 0 poitns''')
time.sleep(1)
print("You will have 3 tries and your points will be shown after the 3 levels")

#Level 1
print("The number I'm thinking is between 1 and 10")
answer = random.randint(1, 10)
player_old = input("Your guess:")
player = int(player_old)
if player == answer:
    print("Correct!")
    points += 3
else:
    print("Wrong!")
    hint = answer/2
    if hint.is_integer():
       print("Hint: The number is divisible by 2")
    else:
        print("Hint: The number is not divisible by 2")
    player_2_old = input("Your guess:")
    player_2 = int(player_2_old)
    if player_2 == answer:
        print("Correct!")
        points += 2
    else:
        print("Wrong!")
        if player_2 < answer:
            print("Hint: Your guess was too low")
        else:
            print("Hint: Your guess was too high")
        player_3_old = input("Your guess:")
        player_3 = int(player_3_old)
        if player_3 == answer:
            print("Correct!")
            points += 1
        else:
            print("Wrong! The number was {}".format(answer))
print("Your points at the end of level 1 are {}".format(points))

#level 2
print("The number I'm thinking is between 1 and 50")
value = random.randint(1, 50)
gamer_old = input("Your guess:")
gamer = int(gamer_old)
if gamer == value:
    print("Correct!")
    points += 4
else:
    print("Wrong!")
    hint_2 = value/5
    if hint_2.is_integer():
        print("The number is divisible by 5")
    else:
        print("The number is not divisible by 5")
    gamer_2_old = input("Your guess:")
    gamer_2 = int(gamer_2_old)
    if gamer_2 == value:
        print("Correct")
        points += 3
    else:
        print("Wrong!")
        if gamer_2 < value:
            print("Hint: Your guess was too low")
        else:
            print("Hint: Your guess was too high")
        hitn_old = input("Do you want to use a bonus hint CHOOSE y/n?")
        hitn = hitn_old.lower()
        if 'y' in hitn:
            if value < 25:
                print('The number is smaller than 25!')
            elif value > 25:
                print('The number is bigger than 25!')
            elif value == 25:
                print("Lucky you! The number is 25!")
            points -= 0.5
            print("Since you chose the hint, you lost 0.5 points!")
        elif 'n' in hitn:
            print("Alright! Good luck!")
        gamer_3_old = input("Your guess:")
        gamer_3 = int(gamer_3_old)
        if gamer_3 == value:
            print("Correct!")
            points += 2
        else:
            print("Wrong! The number was {}".format(value))
print("Your points at the end of level 2 are {}".format(points))

#level 3
print("The number I'm thinking is between 1 and 100")
last = random.randint(1,100)
dream_old = input("Your guess:")
dream = int(dream_old)
if dream == last:
    print("Correct!")
    points += 5
else:
    print("Wrong!")
    hint_3 = last/10
    if hint_3.is_integer():
        print("Hint: The number is divisible by 10")
    else:
        print("Hint: The number is not divisible by 10")
    dream_2_old = input("Your guess:")
    dream_2 = int(dream_2_old)
    if dream_2 == last:
        print("Correct!")
        points += 4
    else:
        print("Wrong!")
        if dream_2 < last:
            print("Your guess was too low")
        else:
            print("Your guess was too high")
        thin_old = input('Do you want to use a bonus hint CHOOSE y/n?')
        thin = thin_old.lower()
        if 'y' in thin:
            if last < 50:
                print('The number is smaller than 50!')
            elif last > 50:
                print('The number is bigger than 50!')
            elif last == 50:
                print('Lucky you! The number is 50!')
            points -= 0.25
            print("Since you chose the hint, you lost 0.25 points!")
        elif 'n' in thin:
            print("Alright! Good luck!")
        dream_3_old = input("Your guess:")
        dream_3 = int(dream_3_old)
        if dream_3 == last:
            print("Correct!")
            points += 3
        else:
            print("Wrong! The number was {}".format(last))
print("Your points at the end of level 3 are {}".format(points))
john = random.randint(1,4)
print("For a chance to get extra points, answer this question!")
ben = input('What is 10 + 10 - 40:')
ben_new = int(ben)
if ben_new == -20:
    print("You got an extra {} points!".format(john))
points += john

print("Your final points are {}".format(points))

#ranking
if points == 13:
    print("Excellent!")
elif points <= 12 and points >= 7:
    print("Very good!")
elif points <= 6 and points >= 3:
    print("Good!")
elif points == 0:
    print("Aim higher!")
elif points < 0:
    print("Terrible!")
else: 
    print("Nice try!")
