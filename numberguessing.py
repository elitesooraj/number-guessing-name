import random
print("hello this is sa number guessing game/n you have 7 tries. good luck!")
low=int(input("Enter the lower guess"))
high=int(input("Enter the higher guess"))
print(f"\n you have 7 chances to guess number between {low} nad {high}.Lets start!")
num = random.randint(low,high)
ch=7
gc=0

while gc<ch:
    gc +=1
    guess = int(input("Enter your guess"))

    if guess==num:
        print("correct! The number {num} is guessed corrrectly in {gc} attempts ")
        break
    
    elif gc>=ch and guess!=num:
        print("sorry the number was {num}")
        
    elif guess > num:
        print("Too high!  try a lower number")

    elif guess < num:
        print(" too low! try ahigher number")