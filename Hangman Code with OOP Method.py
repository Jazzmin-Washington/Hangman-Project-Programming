#%%
# Hangman Project
from random import choice
from re import X
word_list = ['cultured','lively','finish','embezzling','separate','aspiring','nostalgic','determined','announce','depressed','unwieldy','nonchalant','makeshift','vivacious','hideous','precious','mysterious','classy','filthy','name','stingy','questionable','dispensable','astonishing','volleyball','lunchroom','organic','recognize','garrulous','glistening','sweltering','suggestion','determine','handsomely','treatment','mountain','eminent','numerous','cemetery','grandiose','understand','incredible','cumbersome','damaging','numerous','threatening','rhetorical','endurable','disturbed','coordinated','broadcast']
class Hangman:
      def __init__(self):
            self.word_list = word_list

      def welcome(self):
            print("Welcome to my game of Hangman. This is a game where a random word is generated and you will have 8 tries to guess the letters. Good luck")

      def hangman_picture(self, x):
            self.x = x
            if x < 0:
                  print("You have gained no parts")
                  print('\n')
                  
            elif x == 0: 
                  print(
      '''
      +---+
          |
          |
          |
      ===''')
                  print('\n')
                  
            elif x == 1:
                  print(               
      '''
      +---+
      O   |   
          |
          |
      ===
      ''')
                  print('\n')
                  
            elif x == 2:
                  print('''
      +---+
      O   |
      |   |
          |
      ===''')
                  print('\n')
                  
            elif x == 3:
                  print('''
      +---+
      O   |
     /|   |
          |
      ====''')
                  print('\n')
                  
            elif x == 4:
                  print('''
       +---+
       O    |
      /|\   |
            |
      ====''')
                  print('\n')
                  
            elif x == 5:
                  print('''
      +---+
       O   |
      /|\  |
      /    |
      ===''')
                  print('\n')
                  
            elif x == 6:
                  print('''
      +---+
       O   |
      /|\  |
      / \  |
      ===''')
                  print('\n')
                  
            else:
                  print("You Lose")
                  
      def playing_hangman(self, turns = 8, x = -2):
            self.turns = turns
            self.x = x
            self.guessed_characters = []
            self.guessed_word = []
            guessed = False
            print("Let me think of a word")
            self.chosen_word = choice(self.word_list)
            self.word_for_game = list(self.chosen_word)
            self.word_completed = (" _ ") * len(self.word_for_game)
            while not guessed and self.turns > 0:
                  print(f'You have {self.turns} tries left')
                  print('\n')
                  guess = input('Please guess a letter or word for the game')
                  if len(guess) == 1 and guess.isalpha():
                        
                        if guess in self.guessed_characters:
                              print(f'You have already tried that letter.')
                              
                        elif guess not in self.chosen_word:
                              self.guessed_characters.append(guess)
                              print(guess, "is not in the word")
                              self.turns -= 1
                              self.x += 1
                                        
                        else:
                              print("Good job", guess, "is in the word")
                              self.guessed_characters.append(guess)
                              word_as_list = list(self.word_completed)
                              indices = [i for i, letter in enumerate(self.chosen_word) if letter == guess]
                              for index in indices:
                                    word_as_list[index] = guess
                                    self.word_completed = "".join(word_as_list)
                                    if " __ " not in self.word_completed:
                                          guessed = False
                                          if self.word_completed == self.chosen_word:
                                                guessed = True
                                   
                  elif len(guess) == len(self.chosen_word) and guess.isalpha():
                        if guess in self.guessed_word:
                              print('You have already guessed that word.')
                              
                        elif guess != self.chosen_word:
                              self.guessed_word.append(guess)
                              print(guess, "is not the word")
                              self.turns -= 1
                              self.x += 1
                             
                        else:
                              guessed = True
                              self.play_again()
                  else:
                        print('Not a valid guess. Please enter a letter or word to guess.')
                        
                  print(self.hangman_picture(self.x))            
                  print(f' \n You have guessed the following characters {self.guessed_characters} and the following words {self.guessed_word} \n') 
                  print(self.word_completed)
                  print('\n')
                        
            if guessed == True :
                  print(f'Congrats! You guessed the word: {self.chosen_word}. You win!')
                  print('\n')
                  self.play_again()      
            elif guessed == False:
                  print('Sorry you ran out of tries. The word was', self.chosen_word, '. Maybe next time')
                  print('\n')
                  self.play_again() 
            else:
                  print('\n')  
      
      def lets_play(self):
            self.welcome(), self.playing_hangman()     
                        
      def play_again(self):
            again = input('Would you like to play again? Enter y/n')
            if again == 'y':
                  self.lets_play()
            elif again =='n':
                  print('Thanks for playing!')
            else:
                  print('Please enter y or n for yes and no, respectively')
                  return self.play_again()
                           
new_hangman_game = Hangman()
new_hangman_game.lets_play()       
# %%
