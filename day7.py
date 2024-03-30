import random

#word_list=["Ardvark","Baboon","Camel"]
from hangman_words import word_list

chosen_word=random.choice(word_list)
word_length=len(chosen_word)
print(chosen_word)
from hangman_art import logo
print(logo)
display=[]
for letter in range(len(chosen_word)):
    display+="_"
lives=6
end_of_game=False
while end_of_game==False and lives>0:
    guess=input("Guess a letter present in the word").lower()
    for positon in range(0,len(chosen_word)):
        letter = chosen_word[positon].lower()
        if guess == letter:
            display[positon] = letter
    if guess in display:
        print(f"You've already guessed {guess}")
        continue


    from hangman_art import stages

    if guess not in display:
        print("You lose a life")
        lives -= 1
        if lives==0:
            print("You lose")
            print(display)
        print(stages[6-lives])
        if "_" not in display:
            end_of_game=True
            print("You Win")
            print(stages[lives])

