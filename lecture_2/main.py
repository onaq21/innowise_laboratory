def  main():
    """Print user information and profile summary"""

    user_name = input("Hello, enter your full name: ")
    while True:
        try:
            current_age = 2025 - int(input("Enter your birth year: "))
            break
        except ValueError:
            print("Please enter a valid year")
    life_stage = generate_profile(current_age)
    hobbies = []
    print("Enter your favorite hobby (type 'stop' to finish): ")
    while True:
        if (hobby := input().lower()) == "stop":
            break
        hobbies.append(hobby)

    user_profile = {
        "Name": user_name,
        "Age": current_age,
        "Stage": life_stage,
        "hobbies": hobbies
    }

    print("--------\nProfile Summary:")
    for key, value in user_profile.items():
        if key == "hobbies":
            if not value:
                print("You didn't mention any hobbies")
            else :
                print(f"Favorite hobbies ({len(value)}):")
                for hobby in value:
                    print(f"- {hobby}")
            continue
        print(f"{key}: {value}")
    print("--------")



def generate_profile(age):
    """Return life stage"""
    if age < 0:
        return "Incorrect age"
    elif 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

if __name__ == "__main__":
    main()