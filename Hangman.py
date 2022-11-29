# Problem Set 2, hangman.py
# Name: Fedorenko Elizaveta
# Collaborators:
# Time spent: nobody knows

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = set(secret_word)
    l_g_s = set(letters_guessed)
    s_w_set = set(secret_word)
    if ((l_g_s.intersection(letters)) == s_w_set): 
      return True
    else: 
      return False  
     


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = set(secret_word)
    l_g_s = set(letters_guessed)
    m = letters.difference(l_g_s)
    s1 = secret_word
    for el in m:
      s1 = s1.replace(el, '_ ')
    return s1


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    dostypni = alphabet
    for l in letters_guessed:
      dostypni = dostypni.replace(l, '')
    return dostypni


 
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guess = 6
    end = False
    glasni = ['a', 'i', 'e', 'o', 'u']
    w = 3
    print ('Welcome to the game Hangman!')
    print ('I am thinking of the word', len(secret_word), 'letters long')
    print(f'{"-"*13}')
    while end != True:
      print('You have', guess, 'guesses left')
      print('Available letters left:', get_available_letters(letters_guessed))
      l = str.lower(input('Please guess a letter: '))
      if l.isalpha() and len(l) == 1:
        if l in secret_word and l not in letters_guessed:          
           letters_guessed.append(l)
           print('Good guess:', get_guessed_word(secret_word, letters_guessed)) 
           print(f'{"-"*13}')
           win = is_word_guessed(secret_word, letters_guessed)
           if win is True:
            print('Congratulations! You won! Your word: ', secret_word)
            print('Your total score: ', guess * len((list(set(secret_word)))))
            end = True
        elif l in secret_word and l not in letters_guessed:
            w -= 1
            print("Oops! You've already guessed that letter. You nave have", w, "warnings")
            letters_guessed.append(l)
            print(f'{"-"*13}')
            if guess <= 0:
              print('Sorry, you lost, your word: ', secret_word)
              end = True
            letters_guessed.append(l)
        elif l in letters_guessed:
            w -= 1
            print("Oops! You've already guessed that letter. You nave have", w, "warnings")
            print(f'{"-"*13}')
            if w <= 0:
              print('No more warnings has left')
              w += 3
              guess -= 1
              if guess <= 0:
               print('Sorry, you lost, your word: ', secret_word)
               end = True
        else:
          if l in glasni:
            guess -= 2
            letters_guessed.append(l)
            if guess <= 0:
              print('Sorry, you lost, your word: ', secret_word)
              end = True            
            print('Oops! That letter not in my word: ', get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*13}')
          else:
            guess -= 1
            print('Oops! That letter not in my word: ', get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*13}')
            letters_guessed.append(l)
            if guess <= 0: 
              print('Sorry, you lost, your word: ', secret_word)
              end = True

      else:
          w -= 1
          print('Oops! Not a valid letter input. You nave have', w, 'warnings')
          if w <= 0:
              print('No more warnings has left')
              w += 3
              guess -= 1












# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", '')
    if len(my_word) != len(other_word): return False
    list = []
    int = 0
    for i in my_word:
        
        if i != "_":
            list.append(other_word[int])
        else:
            list.append("_")
        int += 1
    list = "".join(list)
    if my_word == list: return True
    else: return False
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Possible matches are: ")
    for word in wordlist:
            word1 = match_with_gaps(my_word, word)
            if word1 is True:
              print(word, end = ",")
def hangman_with_hints(secret_word):
      # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guess = 6
    end = False
    glasni = ['a', 'i', 'e', 'o', 'u']
    w = 3
    print ('Welcome to the game Hangman!')
    print ('I am thinking of the word', len(secret_word), 'letters long')
    print(f'{"-"*13}')
    while end != True:
      print('You have', guess, 'guesses left')
      print('Available letters left:', get_available_letters(letters_guessed))
      l = str.lower(input('Please guess a letter: '))
      if l.isalpha() and len(l) == 1:
        if l in secret_word and l not in letters_guessed:          
          letters_guessed.append(l)
          print('Good guess:', get_guessed_word(secret_word, letters_guessed))
          print(f'{"-"*13}')
          win = is_word_guessed(secret_word, letters_guessed)
          if win is True:
            print('Congratulations! You won! Your word: ', secret_word)
            print('Your total score: ', guess * len((list(set(secret_word)))))
            end = True
        elif l in secret_word and l not in letters_guessed:
            w -= 1
            print("Oops! You've already guessed that letter. You nave have", w, "warnings")
            letters_guessed.append(l)
            print(f'{"-"*13}')
            if guess <= 0:
              print('Sorry, you lost, your word: ', secret_word)
              end = True
            letters_guessed.append(l)
        elif l in letters_guessed:
            w -= 1
            print("Oops! You've already guessed that letter. You nave have", w, "warnings")
            print(f'{"-"*13}')
            if w <= 0:
              print('No more warnings has left')
              w += 3
              guess -= 1
              if guess <= 0:
               print('Sorry, you lost, your word: ', secret_word)
               end = True
        else:
          if l in glasni:
            guess -= 2
            letters_guessed.append(l)
            if guess <= 0:
              print('Sorry, you lost, your word: ', secret_word)
              end = True            
            print('Oops! That letter not in my word: ', get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*13}')
          else:
            guess -= 1
            print('Oops! That letter not in my word: ', get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*13}')
            letters_guessed.append(l) 
            if guess <= 0:            
               print('Sorry, you lost, your word: ', secret_word)
               end = True

      elif l == '*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        print('')
      else:
          w -= 1
          print('Oops! Not a valid letter input. You nave have', w, 'warnings')
          print(f'{"-"*13}')
          if w <= 0:
              print('No more warnings has left')
              w += 3
              guess -= 1












# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------




if __name__ == "__main__": 
    secret_word =choose_word(wordlist) 
    hangman_with_hints(secret_word)
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines.