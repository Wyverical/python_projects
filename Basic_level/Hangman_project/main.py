import random 
from word_list import word_list
from game_art import stages
from game_art import logo
#list_of_words = ['apple', 'tomato', 'grapes']

chose_word = random.choice(word_list)
wordlength = len(chose_word)
end_game = False
no_of_lives = 6
display = []

for _ in range(wordlength):
    display +="_"

while not end_game:
    guess_letter = input("Select a letter of your choice: ").lower()

    if guess_letter in display:
        print(f"You have selected Correct letter {guess_letter}")
    for position in range(wordlength):
        letter = chose_word[position]

        if letter == guess_letter:
            display[position]=letter
    if guess_letter not in chose_word:
        print(f"The selected letter {guess_letter} is not in the word. You have lost a life!")
        no_of_lives-=1
        if no_of_lives ==0:
            end_game=True
            print("You Lose!!! Please try again!")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game= True
        print("Congratulations!!! You Win!!")
    print(stages[no_of_lives])

    































