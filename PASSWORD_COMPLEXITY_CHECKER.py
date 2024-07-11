import re

def evaluate_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = {
        "length": "8 or more characters" if length_criteria else "Less than 8 characters",
        "uppercase": "Contains uppercase letters" if uppercase_criteria else "No uppercase letters",
        "lowercase": "Contains lowercase letters" if lowercase_criteria else "No lowercase letters",
        "number": "Contains numbers" if number_criteria else "No numbers",
        "special_char": "Contains special characters" if special_char_criteria else "No special characters"
    }

    return strength, feedback

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ").strip()
    
    strength, feedback = evaluate_password_strength(password)
    
    print(f"Password Strength: {strength}")
    print("Feedback:")
    for criterion, message in feedback.items():
        print(f"- {message}")


main()
