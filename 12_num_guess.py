import random
random_num=random.randint(0,10)
guess=int(input("Guess a num btw 0-10:-"))
          while(guess!=random_num):
            print("your guess is wrong")
            guess=int(input("Guess again:- "))
          print("Wel Guess")            
