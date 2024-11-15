def GameAglo(name:str):
    
    counter = 7
    nameLower = name.lower()
    mainarray = [] 
    for i in nameLower:
      mainarray.append(i)
      
    hidden = []
    for i in range(len(mainarray)):
      if mainarray[i] == " ":
        hidden.append(" ")
      else:
        hidden.append("_")
    
    while counter > 0:
        
      print("Your word is:", " ".join(hidden))
      print("You have", str(counter), "chances")
      
#      update_hidden = ''.join(hidden) 
      guess = input("Guess a letter, digit or the whole name:").lower()

      if guess == nameLower:
        print("Congratulations! You guessed the name of the word correctly.")
        print("The word was:", name)
        return counter
      
      elif guess not in "abcdefghijklmnopqrstuvwxyz1234567890":
        print("Wrong input :(")
        counter -= 1

      else:
        if guess in mainarray:
          for i in range(len(mainarray)):
            if mainarray[i] == guess:
              hidden[i] = guess
#              update_hidden = ''.join(hidden)  
          print("Your Guess is correct")
      
        else:
          print("The letter", guess, "is not in the name of the word.")
          counter -= 1
                
        if "_" not in hidden:
          print("Congratulations! You guessed the name of the word correctly.")
          print("The word was:", name)
          return counter
                
        if counter == 0:
          print("You have run out of chances. The name of the word was:", name)
          return counter