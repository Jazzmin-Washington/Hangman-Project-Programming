#%%
# Hangman Project
from random import choice
word_list = ['cultured','lively','finish','separate','aspiring','nostalgic','determined','announce','depressed','unwieldy','nonchalant','makeshift','vivacious','hideous','precious','mysterious','classy','filthy','name','stingy','questionable','dispensable','astonishing','volleyball','lunchroom','organic','recognize','garrulous','glistening','sweltering','suggestion','determine','handsomely','treatment','mountain','eminent','numerous','cemetery','grandiose','understand','incredible','cumbersome','damaging','numerous','threatening','rhetorical','endurable','disturbed','coordinated','broadcast']

def welcome():
      print("Welcome to my game of Hangman. This is a game where a random word is generated and you will have 8 tries to guess the letters. Good luck")

def hangman_picture(x):
      if x < 0:
            print("You have no parts yet")
      elif x == 0: 
            print(
   '''
  +---+
  |
  |
  |
  ===''')
      elif x == 1:
            print(               
  '''
  +---+
  O   |   
      |
      |
  ===
  ''')
      elif x == 2:
            print('''
+---+
O   |
|   |
    |
===''')
      elif x == 3:
            print('''
  +---+
  O   |
 /|   |
      |
 ====''')
      elif x == 4:
            print('''
  +---+
  O   |
 /|\  |
      |
====''')
      elif x == 5:
            print('''
  +---+
  O   |
 /|\  |
 /    |
 ===''')
      elif x == 6:
            print('''
  +---+
  O   |
 /|\  |
 / \  |
 ===''')
      else:
            print("You Lose")
            play_again()

def play_hangman():
      print("Let me think of a word")
      chosen_word = choice(word_list)    
      word_for_game = list(chosen_word)
      word_completed = ("_""") * len(word_for_game)
      guessed = False
      guessed_characters = []
      guessed_words = []
      incorrect_characters = []
      turns = 8
      x = -2
      print(word_completed)
      while not guessed and turns > 0:
            print(f'You have {turns} tries left')
            guess = input('Please guess a letter for the game')
            if len(guess) == 1 and guess.isalpha():
                  if guess in guessed_characters:
                        print(f'You have already tried that letter. Your previous guesses include {guessed_characters}')
                  elif guess not in chosen_word:
                            print(guess, "is not in the word")
                            guessed_characters.append(guess)
                            incorrect_characters.append(guess)
                            turns -= 1
                            x += 1
                            print(hangman_picture(x))  
                  else:
                        print("Good job", guess, "is in the word")
                        guessed_characters.append(guess)
                        word_as_list = list(word_completed)
                        indices = [i for i, letter in enumerate(chosen_word) if letter == guess]
                        for index in indices:
                              word_as_list[index] = guess
                        word_completed = "".join(word_as_list)
                        if " __ " not in word_completed:
                              guessed = False
                              if word_completed == chosen_word:
                                    print("Congrats, you guessed the word! You Win!")
                                    play_again()
                        
                                    
            elif len(guess) == len(chosen_word) and guess.isalpha():
                  if guess in guessed_words:
                        print(f'You have already tried that word. Your previous guesses include {guessed_words}')
                  elif guess != chosen_word:
                        print(guess, "is not the word.")
                        guessed_words.append(guess)
                        turns -= 1
                        x += 1
                        print(hangman_picture(x))  
                  else:
                        guessed = True
                        
                        
            else:
                  print("Not a valid guess")
          
            print(f' \n You have guessed the following characters {guessed_characters} \n') 
            print(word_completed)
            print('\n')
            
    
      if guessed == True:
            print("Congrats, you guessed the word! You Win!")
            play_again()
      else:
            print("Sorry you ran out of tries. The word was", chosen_word, ". Maybe next time")
            play_again()
            
                  
def play_again():
      again = input('Would you like to play again? Enter y/n')
      if again == 'y':
           lets_play()
      else:
            return 'Thanks for playing!'

def lets_play():
      welcome(),
      play_hangman()
      return
      
              
            
lets_play()
# %%
