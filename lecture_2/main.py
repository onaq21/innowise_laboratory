def  main():
    """Print user information and profile summary"""
    while True:
        user_name = input("Hello, enter your full name: ")
        if not valid_string(user_name):
            continue
        break
    while True:
        try:
            current_age = 2025 - int(input("Enter your birth year: "))
            if not valid_age(current_age):
                continue
            break
        except ValueError:
            print("Invalid input, please try again")
    life_stage = generate_profile(current_age)
    hobbies = []
    print("Enter your favorite hobby (type 'stop' to finish): ")
    while True:
        hobby = input().lower()
        if hobby == "stop":
            break
        elif not valid_string(hobby):
            continue
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



def generate_profile(age: int) -> str:
    """Return life stage"""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

def valid_string(s: str) -> bool:
    """Check if string is valid"""
    s = s.strip()
    if not s or s.isdigit():
        print("Invalid input, please try again")
        return False
    return True

def valid_age(age: int) -> bool:
    """Check if age is valid"""
    if age < 0 or age > 150:
        print("Invalid input, please try again")
        return False
    return True

if __name__ == "__main__":
    main()