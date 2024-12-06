import random

def roll_dice(sides=6, rolls=1):
    results = []
    for _ in range(rolls):
        results.append(random.randint(1, sides))
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice (e.g., 6): "))
            rolls = int(input("Enter the number of dice rolls: "))
            
            if sides < 1 or rolls < 1:
                print("Please enter positive numbers for sides and rolls.")
                continue
            
            results = roll_dice(sides, rolls)
            print(f"Results of {rolls} rolls with a {sides}-sided dice: {results}")
            
            play_again = input("Do you want to roll again? (yes/no): ").strip().lower()
            if play_again not in ['yes', 'y']:
                print("Thank you for using the Dice Rolling Simulator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
