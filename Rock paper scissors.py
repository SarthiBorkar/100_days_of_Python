import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Type 1 , 2 or 3 for Rock , Paper and Scissors respectively" ) 
val = int(input("type a no."))
if val == 1:
    print(rock)
elif val == 2:
    print(paper)
elif val == 3:
    print(scissors)
else:
    print("try again with 1,2,3")    

valout = random.randint(1,3)            

if valout == 1:
    print(rock)
elif valout == 2:
    print(paper)
elif valout == 3:
    print(scissors)

w = "You Win"
l = "You lose"
d = "Its a Draw"

if val == 1:
   if valout == 1:
    print(d)
   elif valout==2:
    print(l)
   elif valout==3:
    print(w)
 
if val == 2:
   if valout == 1:
    print(w)
   elif valout==2:
    print(d)
   elif valout==3:
    print(l)

if val == 3:
   if valout == 1:
    print(l)
   elif valout==2:
    print(w)
   elif valout==3:
    print(d)     

   
   