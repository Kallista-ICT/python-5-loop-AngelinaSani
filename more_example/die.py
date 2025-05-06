import random

score = 0
roll = []

print("welcome to your eternal doom of gambling")
print("you need to get 50 points to escape")

while score < 50:
    input(" roll or die, roll or die rolling")
    die = random.randint(1, 6)
    score += die

    print(f"you rolled a {die}")
    print(f"now your score is {score}")

    if score >= 50:
        print("have u truly escaped? No, you're here forever")
        show_history = input("Do you want to see your history? (yes or no): ").strip().lower()
        
        if show_history == "yes":
            print("Your history of rolls:")
            roll_number = 1
            for roll in roll:
                print(f"Roll {roll_number}: {roll}")
                roll_number += 1
            
