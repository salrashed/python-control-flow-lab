# EX 1
def check_letter():
    letter = input("Enter a letter: ")
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single letter.")
        return
    vowels = "aeiou"
    if letter.lower() in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")

check_letter()

# EX 2
def check_voting_eligibility():
   voting_age = 18
   age = int(input("Enter your age: "))
   if age >= voting_age:
       print("You are eligible to vote.")
   else:
       print("You are not eligible to vote.")

check_voting_eligibility()

# EX 3
def calculate_dog_years():
    
    dog_age_input = input("Input a dog's age: ")
    dog_age = float(dog_age_input)  

    if dog_age < 0:
        print("Age cannot be negative. Please enter a valid age.")
        return
    if dog_age <= 2:
        dog_years = dog_age * 10 
    else:
        dog_years = (2 * 10) + ((dog_age - 2) * 7)  

    print(f"The dog's age in dog years is {dog_years:.1f}.")
    

calculate_dog_years()

# EX 4
def weather_advice():
    cold_input = input("Is it cold outside? (yes/no): ")
    rain_input = input("Is it raining? (yes/no): ")

    if cold_input not in ["yes", "no"] or rain_input not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no' ")
        return
    is_cold = cold_input == "yes"
    is_raining = rain_input == "yes"

    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    if is_cold and not is_raining:
        print("Wear a warm coat.")
    if  not is_cold and is_raining:
        print("Carry an umbrella.") 
    if not is_cold and not is_raining:
        print("Wear light clothing.")

weather_advice() 

# EX 5
def determine_season():
    month_input = input("Enter the month of the year (Jan - Dec):")
    day = int(input("Enter the day of the month:"))

    if month_input not in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
        print("Invalid input. Please enter a valid month.")
        return
    if day <= 1 or day >= 31:
        print("Invalid input. Please enter a valid day.")
        return
    if month_input (month_input == "Dec" and day >= 21) or (month_input == "Mar" and day <= 19):
        season = "Winter"
    if month_input (month_input == "Mar" and day >= 20) or (month_input == "Jun" and day <= 20):
        season = "Spring"
    if month_input in (month_input == "Jun" and day >= 21) or (month_input == "Sep" and day <= 21):
        season = "Summer"
    if month_input in (month_input == "Sep" and day >= 22) or (month_input == "Dec" and day <= 20):
        season = "Fall"
    print(f"{month_input} {day} is in {season}.")

determine_season()