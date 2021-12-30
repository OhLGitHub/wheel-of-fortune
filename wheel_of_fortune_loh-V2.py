# Wheel of Fortune
# Lindsey Oh

# Set up word bank
import random # Python's built-in module for all things random
f = open('words_alpha.txt','r') # open and read from the text file
word_list = f.readlines() # read the file line by line into a list
f.close() # close the text file

# spin_the_wheel function
def spin_the_wheel():
    wheel_segments = [800, 500, 650, 500, 900, 'BANKRUPT', 5000, 500, 900, 700, 600, 800, 500, 700, 500, 600, 550, 500, 900, 'BANKRUPT', 650, 900, 700, 'LOSE A TURN']
    landed_on = random.choice(wheel_segments)
    print('')
    print('The wheel is spinning...')
    return landed_on

# money_update function
def money_update(pnum):
    if pnum == 1:
        global player1_temp, player1_total
        print(f'Player {pnum} balance: ${player1_temp}. Player {pnum} overall winnings: ${player1_total}.\n')
    elif pnum == 2:
        global player2_temp, player2_total
        print(f'Player {pnum} balance: ${player2_temp}. Player {pnum} overall winnings: ${player2_total}.\n')
    elif pnum == 3:
        global player3_temp, player3_total
        print(f'Player {pnum} balance: ${player3_temp}. Player {pnum} overall winnings: ${player3_total}.\n')
    else:
        print('Error: argument must be a valid player number.')

# consonant? or vowel? or word? (cvw) function
def cvw():
    global player1_temp, player2_temp, player3_temp
    global spin_result, onscreen, letter_list, guess
    global consonant_list, correct_letter_count, winnings, purchase
    global vowel_list, correct_vowel_count, full_guess, is_guessed
    is_guessed = False
    while not is_guessed:
        choice = str(input('Spin for a (C)onsonant? Type "C". Buy a (V)owel? Type "V". Guess the (W)ord? Type "W": ')).upper().strip() # turn the input into an uppercase string
        if choice == 'C':
            spin_result = spin_the_wheel()
            if spin_result == 'BANKRUPT':
                bankrupt(p)
                break
            elif spin_result == 'LOSE A TURN':
                print(f'Sorry, Player {p}, you landed on LOSE A TURN.\n')
                break
            else:
                print(f'Player {p}, you landed on ${spin_result}!\n')
                print(''.join(onscreen)) # display the number of letters in the word as dashes
                print('')
                print(''.join(consonant_list)) # display which consonants have not yet been guessed
                guess = str(input('Guess a consonant from the list above: ')).upper().strip() # turn the input into an uppercase string
                if guess.isalpha() == True and guess in consonant_list and guess in letter_list and len(guess) == 1: # guess is a correct letter
                    consonant_list.remove(guess) # remove guess from list to prevent reuse
                    correct_letter_count = 0
                    for i in range(0,len(word)): # for the entire length of the word
                        if guess == letter_list[i]: # guessed letter matches a letter in the word
                            correct_letter_count += 1 # keep track of how many correct letters are in the word
                            onscreen[i] = guess # updates 'onscreen' to display correctly guessed letters
                    print('')
                    print(''.join(onscreen)) # display updated word
                    print('')
                    winnings = spin_result * correct_letter_count
                    print(f'{guess} appears {correct_letter_count} times. You win ${winnings}.')
                    add_winnings(p) # add winnings to Player balance
                    if onscreen == letter_list:
                        round_winner(p)
                        is_guessed = True
                elif guess.isalpha() == True and guess in consonant_list and guess not in letter_list and len(guess) == 1: # guess is an incorrect letter
                    print(''.join(onscreen))
                    print(f'{guess} is not in the word. Your turn is over.\n')
                    break
                else: # guess is invalid
                    print('Error: you did not follow directions. Try again.')
        elif choice == 'V':
            if player1_temp >= 250 or player2_temp >= 250 or player3_temp >= 250:
                print('')
                print(''.join(onscreen)) # display the number of letters in the word as dashes
                print('')
                print(''.join(vowel_list)) # display which vowels have not yet been purchased
                purchase = str(input('Purchase a vowel from the list above for $250: ')).upper().strip() # turn the input into an uppercase string
                if purchase.isalpha() == True and purchase in vowel_list and purchase in letter_list and len(purchase) == 1: # purchase is a correct letter
                    vowel_list.remove(purchase) # remove purchase from list to prevent reuse
                    correct_vowel_count = 0
                    for i in range(0,len(word)): # for the entire length of the word
                        if purchase == letter_list[i]: # guessed letter matches a letter in the word
                            correct_vowel_count += 1 # keep track of how many correct letters are in the word
                            onscreen[i] = purchase # updates 'onscreen' to display correctly purchased letters
                    print('')
                    print(''.join(onscreen)) # display updated word
                    vowel_purchase(p)
                    if onscreen == letter_list:
                        round_winner(p)
                        is_guessed = True
                elif purchase.isalpha() == True and purchase in vowel_list and purchase not in letter_list and len(purchase) == 1: # purchase is an incorrect letter
                    vowel_list.remove(purchase) # remove purchase from list to prevent reuse
                    print(f'{purchase} is not in the word. Your turn is over.\n')
                    break
                else: # guess is invalid
                    print('Error: you did not follow directions. Try again.')
            else:
                print('You do not have enough money to purchase a vowel.\n')
        elif choice == 'W':
            print('')
            print(''.join(onscreen)) # display the number of letters in the word as dashes
            print('')
            full_guess = str(input('Guess the entire word: ')).upper().strip() # turn the input into an uppercase string
            if list(full_guess) == letter_list:
                onscreen = list(full_guess)
                round_winner(p)
                is_guessed = True
            else:
                print('{full_guess} is incorrect. Your turn is over.\n')
                break
        else:
            print('Error: you did not follow directions.')

# bankrupt function
def bankrupt(pnum):
    if pnum == 1:
        global player1_temp
        player1_temp = 0
        print(f'Sorry, Player {pnum}, you landed on BANKRUPT. Player {pnum} balance: ${player1_temp}.\n')
        return player1_temp
    elif pnum == 2:
        global player2_temp
        player2_temp = 0
        print(f'Sorry, Player {pnum}, you landed on BANKRUPT. Player {pnum} balance: ${player2_temp}.\n')
        return player2_temp
    elif pnum == 3:
        global player3_temp
        player3_temp = 0
        print(f'Sorry, Player {pnum}, you landed on BANKRUPT. Player {pnum} balance: ${player3_temp}.\n')
        return player3_temp
    else:
        print('Error: argument must be a valid player number.')

# add_winnings function
def add_winnings(pnum):
    global spin_result, correct_letter_count, winnings
    winnings = spin_result * correct_letter_count
    if pnum == 1:
        global player1_temp
        player1_temp = player1_temp + winnings
        print(f'Player {pnum} balance: ${player1_temp}.')
    elif pnum == 2:
        global player2_temp
        player2_temp = player2_temp + winnings
        print(f'Player {pnum} balance: ${player2_temp}.')
    elif pnum == 3:
        global player3_temp
        player3_temp = player3_temp + winnings
        print(f'Player {pnum} balance: ${player3_temp}.')
    else:
        print('Error: argument must be a valid player number.')

# vowel_purchase function
def vowel_purchase(pnum):
    global purchase, correct_vowel_count
    global player1_temp, player2_temp, player3_temp
    if pnum == 1:
        player1_temp = player1_temp - 250
        print(f'{purchase} appears {correct_vowel_count} times. You lost $250. Player {pnum} balance: ${player1_temp}.')
    elif pnum == 2:
        player2_temp = player2_temp - 250
        print(f'{purchase} appears {correct_vowel_count} times. You lost $250. Player {pnum} balance: ${player2_temp}.')
    elif pnum == 3:
        player3_temp = player3_temp - 250
        print(f'{purchase} appears {correct_vowel_count} times. You lost $250. Player {pnum} balance: ${player3_temp}.')
    else:
        print('Error: argument must be a valid player number.')

# round_winner function
def round_winner(pnum):
    global onscreen
    global player1_temp, player2_temp, player3_temp
    global player1_total, player2_total, player3_total
    if pnum == 1:
        print('')
        print(''.join(onscreen)) # display the number of letters in the word as dashes
        print(f'Player {pnum} wins ${player1_temp} this round!')
        player1_total = player1_total + player1_temp
        player1_temp = 0
        player2_temp = 0
        player3_temp = 0
    elif pnum == 2:
        print('')
        print(''.join(onscreen)) # display the number of letters in the word as dashes
        print(f'Player {pnum} wins ${player2_temp} this round!')
        player2_total = player2_total + player2_temp
        player1_temp = 0
        player2_temp = 0
        player3_temp = 0
    elif pnum == 3:
        print('')
        print(''.join(onscreen)) # display the number of letters in the word as dashes
        print(f'Player {pnum} wins ${player3_temp} this round!')
        player3_total = player3_total + player3_temp
        player1_temp = 0
        player2_temp = 0
        player3_temp = 0
    else:
        print('Error: argument must be a valid player number.')

# final_consonants function
def final_consonants(num_cons_left):
    global game_is_played, word
    global consonant_list, letter_list, onscreen, guess
    if num_cons_left >= 3:
        for cons in range(1,4): # for each of the 3 guesses
            print(''.join(consonant_list)) # display which consonants have not yet been guessed
            guess = str(input('Guess a consonant from the list above: ')).upper().strip() # turn the input into an uppercase string
            if guess.isalpha() == True and guess in consonant_list and guess in letter_list and len(guess) == 1: # guess is a correct letter
                consonant_list.remove(guess) # remove guess from list to prevent reuse
                for i in range(0,len(word)): # for the entire length of the word
                    if guess == letter_list[i]: # guessed letter matches a letter in the word
                        onscreen[i] = guess # updates 'onscreen' to display correctly guessed letters
            elif guess.isalpha() == True and guess in consonant_list and guess not in letter_list and len(guess) == 1: # guess is an incorrect letter
                consonant_list.remove(guess) # remove guess from list to prevent reuse
            else: # guess is invalid
                print(f'Error: you did not follow directions. You wasted guess {cons}/3.')
                if cons < 3:
                    continue
                else:
                    pass
    elif num_cons_left == 2 or num_cons_left == 1:
        for cons in range(1,(num_cons_left+1)): # for each of the remaining guesses
            print(''.join(consonant_list)) # display which consonants have not yet been guessed
            guess = str(input('Guess a consonant from the list above: ')).upper().strip() # turn the input into an uppercase string
            if guess.isalpha() == True and guess in consonant_list and guess in letter_list and len(guess) == 1: # guess is a correct letter
                consonant_list.remove(guess) # remove guess from list to prevent reuse
                for i in range(0,len(word)): # for the entire length of the word
                    if guess == letter_list[i]: # guessed letter matches a letter in the word
                        onscreen[i] = guess # updates 'onscreen' to display correctly guessed letters
            elif guess.isalpha() == True and guess in consonant_list and guess not in letter_list and len(guess) == 1: # guess is an incorrect letter
                consonant_list.remove(guess) # remove guess from list to prevent reuse
            else: # guess is invalid
                print(f'Error: you did not follow directions. You wasted guess {cons}/{num_cons_left}.')
                if cons < num_cons_left:
                    continue
                else:
                    pass
    else:
        pass

# final_vowels function
def final_vowels(num_vow_left):
    global game_is_played, word
    global vowel_list, letter_list, onscreen, guess
    if num_vow_left >= 1:
        print(''.join(vowel_list)) # display which vowels have not yet been guessed
        guess = str(input('Guess a vowel from the list above: ')).upper().strip() # turn the input into an uppercase string
        if guess.isalpha() == True and guess in vowel_list and guess in letter_list and len(guess) == 1: # guess is a correct letter
            vowel_list.remove(guess) # remove guess from list to prevent reuse
            for i in range(0,len(word)): # for the entire length of the word
                if guess == letter_list[i]: # guessed letter matches a letter in the word
                    onscreen[i] = guess # updates 'onscreen' to display correctly guessed letters
            print('')
            print(''.join(onscreen)) # display the number of letters in the word as dashes
            print('')
        elif guess.isalpha() == True and guess in vowel_list and guess not in letter_list and len(guess) == 1: # guess is an incorrect letter
            vowel_list.remove(guess) # remove guess from list to prevent reuse
            print(''.join(onscreen))
        else: # guess is invalid
            print(f'Error: you did not follow directions. You wasted your guess.')
            print(''.join(onscreen))
    else:
        pass

# Set up each player's temporary bank (bank for each round)
player1_temp = 0
player2_temp = 0
player3_temp = 0

# Set up each player's total bank (bank for entire game)
player1_total = 0
player2_total = 0
player3_total = 0

# Begin the game
game_is_played = True

while game_is_played == True:
    print('')
    print('/' * 27 + '\\' * 27)
    print('  W e l c o m e  t o  W H E E L  O F  F O R T U N E ! ')
    print('\\' * 27 + '/' * 27)
    print('')
    for r in range(1,3): # Rounds 1 and 2
        print(f'Now beginning Round {r} of 3!\n')
        consonant_list = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
        vowel_list = ['A','E','I','O','U']
        # Obtain random word
        raw_word = random.choice(word_list) # return a random element from word_list
        word_list.remove(raw_word) # remove the chosen word from the list to ensure it is not used again
        word = raw_word.rstrip('\n').upper() # remove "\n" characters from the right side of the word (aka from the end) and capitalize
        #print(word) # FOR CODE TESTING
        letter_list = list(word) # this will be used to check the variable 'onscreen'
        onscreen = list('-' * len(word)) # variable that keeps track of players' correct guesses
        #print(''.join(onscreen)) # FOR CODE TESTING
        #print('') # FOR CODE TESTING
        # Randomly decide who goes first
        players = [1,2,3]
        random.shuffle(players) # takes players and returns the sequence in a random order
        for p in players:
            while onscreen != letter_list:
                print(f'Your turn, Player {p}!')
                money_update(p) # displays both temporary and total banks for current Player
                spin_result = spin_the_wheel()
                if spin_result == 'BANKRUPT':
                    bankrupt(p)
                    if p == 1:
                        p = 2
                    elif p == 2:
                        p = 3
                    else:
                        p = 1
                elif spin_result == 'LOSE A TURN':
                    print(f'Sorry, Player {p}, you landed on LOSE A TURN.\n')
                    if p == 1:
                        p = 2
                    elif p == 2:
                        p = 3
                    else:
                        p = 1
                else:
                    print(f'Player {p}, you landed on ${spin_result}!\n')
                    print(''.join(onscreen)) # display the number of letters in the word as dashes
                    print('')
                    print(''.join(consonant_list)) # display which consonants have not yet been guessed
                    guess = str(input('Guess a consonant from the list above: ')).upper().strip() # turn the input into an uppercase string
                    if guess.isalpha() == True and guess in consonant_list and guess in letter_list and len(guess) == 1: # guess is a correct letter
                        consonant_list.remove(guess) # remove guess from list to prevent reuse
                        correct_letter_count = 0
                        for i in range(0,len(word)): # for the entire length of the word
                            if guess == letter_list[i]: # guessed letter matches a letter in the word
                                correct_letter_count += 1 # keep track of how many correct letters are in the word
                                onscreen[i] = guess # updates 'onscreen' to display correctly guessed letters
                        print('')
                        print(''.join(onscreen)) # display updated word
                        winnings = spin_result * correct_letter_count
                        print(f'{guess} appears {correct_letter_count} times. You win ${winnings}.')
                        add_winnings(p) # add winnings to Player balance
                        cvw()
                        break
                    elif guess.isalpha() == True and guess in consonant_list and guess not in letter_list and len(guess) == 1: # guess is an incorrect letter
                        consonant_list.remove(guess) # remove guess from list to prevent reuse
                        print(''.join(onscreen))
                        print(f'{guess} is not in the word. Your turn is over.\n')
                        if p == 1: #testing how this works
                            p = 2
                        elif p == 2:
                            p = 3
                        else:
                            p = 1
                    else: # guess is invalid
                        print('Error: you did not follow directions. Try again.')
        print(f'This concludes Round {r} of 3!\n')
        continue
    # Round 3
    print(f'Player 1 Total Bank: ${player1_total}')
    print(f'Player 2 Total Bank: ${player2_total}')
    print(f'Player 3 Total Bank: ${player3_total}')
    finalplayer_total = max(player1_total, player2_total, player3_total)
    if player1_total == player2_total and player1_total == player3_total:
        print('Three-way tie! Randomly choosing a winner...')
        flip_list = ['Player 1','Player 2','Player 3']
        flip = random.choice(flip_list)
        print(f'Congratulations, {flip}! You have made it to the Final Round!\n')
    elif player1_total > player3_total and player1_total == player2_total:
        print('Two-way tie! Randomly choosing a winner...')
        flip_list = ['Player 1','Player 2']
        flip = random.choice(flip_list)
        print(f'Congratulations, {flip}! You have made it to the Final Round!\n')
    elif player1_total > player2_total and player1_total == player3_total:
        print('Two-way tie! Randomly choosing a winner...')
        flip_list = ['Player 1','Player 3']
        flip = random.choice(flip_list)
        print(f'Congratulations, {flip}! You have made it to the Final Round!\n')
    elif player2_total > player1_total and player2_total == player3_total:
        print('Two-way tie! Randomly choosing a winner...')
        flip_list = ['Player 2','Player 3']
        flip = random.choice(flip_list)
        print(f'Congratulations, {flip}! You have made it to the Final Round!\n')
    else:
        if finalplayer_total == player1_total:
            print(f'Congratulations, Player 1! You have made it to the Final Round!\n')
        elif finalplayer_total == player2_total:
            print(f'Congratulations, Player 2! You have made it to the Final Round!\n')
        else:
            print(f'Congratulations, Player 3! You have made it to the Final Round!\n')
    print(f'Now beginning Round 3 of 3!\n')
    consonant_list = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    vowel_list = ['A','E','I','O','U']
    # Obtain random word
    raw_word = random.choice(word_list) # return a random element from word_list
    word_list.remove(raw_word) # remove the chosen word from the list to ensure it is not used again
    word = raw_word.rstrip('\n').upper() # remove "\n" characters from the right side of the word (aka from the end) and capitalize
    #print(word) # FOR CODE TESTING
    letter_list = list(word) # this will be used to check the variable 'onscreen'
    onscreen = list('-' * len(word)) # variable that keeps track of players' correct guesses
    #print(''.join(onscreen)) # FOR CODE TESTING
    #print('') # FOR CODE TESTING
    # Use set comparison for final_consonants and final_vowels functions
    consonant_set = set(consonant_list)
    vowel_set = set(vowel_list)
    word_set = set(word)
    rstln_set = {'R','S','T','L','N'}
    e_set = {'E'}
    num_cons_word = len(consonant_set & word_set) # number of unique consonants in the word
    num_vow_word = len(vowel_set & word_set) # number of unique vowels in word
    num_rstln_word = len(rstln_set & word_set) # intersection of rstln_set and word_set
    num_e_word = len(e_set & word_set) # intersection of e_set and word_set
    num_cons_unguessed = num_cons_word - num_rstln_word # number of unique consonants left to guess
    num_vow_unguessed = num_vow_word - num_e_word # number of unique vowels left to guess
    # Reveal RSTLNE
    for x in ['R','S','T','L','N']:
        consonant_list.remove(x) # remove guess from list to prevent reuse
        for i in range(0,len(word)): # for the entire length of the word
            if x == letter_list[i]: # guessed letter matches a letter in the word
                onscreen[i] = x # updates 'onscreen' to display correctly guessed letters
    for y in ['E']:
        vowel_list.remove(y) # remove guess from list to prevent reuse
        for i in range(0,len(word)): # for the entire length of the word
            if y == letter_list[i]: # guessed letter matches a letter in the word
                onscreen[i] = y # updates 'onscreen' to display correctly guessed letters
    print('')
    print(''.join(onscreen)) # display updated word
    print('')
    # Guess (at most) 3 more consonants
    #print(num_cons_unguessed) # FOR TESTING PURPOSES
    final_consonants(num_cons_unguessed)
    # Guess 1 more vowel at no cost
    #print(num_vow_unguessed) # FOR TESTING PURPOSES
    final_vowels(num_vow_unguessed)
    # Guess the word and Display prize if final player guesses correctly
    full_guess = str(input('Guess the entire word: ')).upper().strip() # turn the input into an uppercase string
    if list(full_guess) == letter_list:
        onscreen = list(full_guess)
        print('')
        print(''.join(onscreen)) # display the number of letters in the word as dashes
        print('')
        print(f'C o n g r a t u l a t i o n s! You just won ${finalplayer_total}!\n')
    else:
        print('')
        print(f'{full_guess} is incorrect.\n')
        print(f'The word was {word}\n')
    print('This concludes Round 3 of 3! Game over.\n')
    game_is_played = False