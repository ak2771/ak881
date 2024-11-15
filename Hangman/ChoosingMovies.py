import csv
import random


def movie_Selection(name: str) -> str:

    columnDisney = []
    columnIMDB = []
    columnOscars = []
    columnNolan = []

    with open('/Users/huntar/Desktop/Coding/Python Projects/Hangman/Datafiles/Nolan.csv', mode='r') as Nolan_file:
        Nolan_csv = csv.reader(Nolan_file)
        
        next(Nolan_csv)

        for row in Nolan_csv:
            columnNolan.append(row[1])



    with open('/Users/huntar/Desktop/Coding/Python Projects/Hangman/Datafiles/disney_movies.csv', mode='r') as disney_file:
        disney_csv = csv.reader(disney_file)
        
        next(disney_csv)

        for row in disney_csv:
            columnDisney.append(row[0])

    #print(columnDisney)

    with open('/Users/huntar/Desktop/Coding/Python Projects/Hangman/Datafiles/IMDB Top 250 Movies.csv', mode='r') as imdb_file:
        imdb_csv = csv.reader(imdb_file)
        
        next(imdb_csv)

        for row in imdb_csv:
            columnIMDB.append(row[1])

    #print(columnDisney)

    with open('/Users/huntar/Desktop/Coding/Python Projects/Hangman/Datafiles/oscars best movie selections.csv', mode='r') as oscars_file:
        oscars_csv = csv.reader(oscars_file)
        
        next(oscars_csv)

        for row in oscars_csv:
            columnOscars.append(row[1])

    #print(columnOscars)
    

    print("There are four categories of movies to choose from:")
    print("1. Christopher Nolan Movies (Easiest)")
    print("2. Disney movies (Misleadingly Easy)")
    print("3. IMDB Top 250 Movies (Challenging at times)")
    print("4. Oscars Best Movie Selections (A good challenge for movie buffs)")
    choice = input("choose a movie from the list above (1., 2., 3., or 4.): ")

    if choice == '1':
        name = random.choice(columnNolan)
    elif choice == '2':
        name = random.choice(columnDisney)
    elif choice == '3':
        name = random.choice(columnIMDB)
    elif choice == '4':
        name = random.choice(columnOscars)

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

    return name 

