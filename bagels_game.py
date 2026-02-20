import random
max_digit=3

while True:
  secret_num=''
  numbers=list('0123456789')
  random.shuffle(numbers)
  for i in range(max_digit):
    secret_num+=numbers[i]
  # print(secret_num)

  for no_of_guess in range(1,11):
    while True:
      guess=input('guess: ')
      if guess==secret_num:
        print('You got it')
        break
      clues=[]
      for i in range(len(guess)):
        if guess[i]==secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
          clues.append('Pico')
      if len(clues)==0:
          print('Bagels')
      else:
        print(' '.join(clues))
    if guess==secret_num:
      break
  else:
      print(f'You are out of guesses. The number was {secret_num}')
  ch=input('wanna play again? y/n: ')
  if not ch.startswith('y'):
      break
