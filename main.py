def greet_by_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    print("Hope you are well.")
greet_by_name("Ryan")

# Functions with input
def life_in_weeks(age):
    total_weeks = 90 * 50
    current_weeks = age * 50
    remaining_weeks = total_weeks - current_weeks
    print(f"You have {remaining_weeks} weeks left.")
life_in_weeks(22)