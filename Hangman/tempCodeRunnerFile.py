    while p1counter > 0:
        
      print("Player1 word choice is:", " ".join(hidden2))
      print("You have", str(p1counter), "chances")
      

      guess2 = input("Guess a letter, digit or word name:").lower()

      if guess2 == p2Lower:
        print("Congratulations! You guessed the word correctly.")
        return
      
      elif guess2 not in "abcdefghijklmnopqrstuvwxyz1234567890":
        print("Wrong input :(")
        p1counter -= 1

      else:
        if guess2 in p2:
          for i in range(len(p2)):
            if p2[i] == guess2:
              hidden2[i] = guess2
#              update_hidden = ''.join(hidden)  
          print("Your Guess is correct")
      
        else:
          print("The letter", guess2, "is not in the word.")
          p1counter -= 1
                
        if "_" not in hidden2:
          print("Congratulations! You guessed the word correctly.")
          return
                
        if p1counter == 0:
          print("You have run out of chances. The word was:", player1)
          return

      if p1counter > p2counter:
        print("Player 1 wins!")
      
      elif p2counter > p1counter:
        print("Player 2 wins!")

      else:
        print("It's a tie!")