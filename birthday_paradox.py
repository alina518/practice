import random
import datetime
TRIALS=100000

while True:
  startofYear=datetime.date(2001,1,1)
  match_count=0
  number=int(input('Enter the number of b\'days to generate: '))
  step=10000 if TRIALS>=100000 else 1000 if TRIALS>=10000 else 100
  for trial in range(1,TRIALS+1):
    birthday=[]
    for i in range(number):
      random_num_of_days=datetime.timedelta(random.randint(0,364))
      bdayYear=startofYear+random_num_of_days
      birthday.append(bdayYear.strftime('%b %d'))
    
    if len(birthday)!=len(set(birthday)):
        match_count+=1
    if trial%step==0:
        print(f'{trial} simulations run')
  percent=(match_count/TRIALS)*100
  print(f"Out of {TRIALS} simulations of {number} people, match happened {match_count} times.")
  print(f"Percentage: {percent:.2f}%")
  ch=input('Do you want to try again? y/n: ')
  if ch!='y':
    break
