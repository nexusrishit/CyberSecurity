import re

# Function to assess password strength
def assess_password_strength(password):
    strength_criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special_char': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }

    # Count how many criteria are met
    score = sum(strength_criteria.values())

    # Feedback and strength assessment
    if score == 5:
        strength = "Strong"
        feedback = "Your password is strong."
    elif 3 <= score < 5:
        strength = "Moderate"
        feedback = "Your password is moderate. Try adding more variety: uppercase letters, numbers, or special characters."
    else:
        strength = "Weak"
        feedback = "Your password is weak. Consider making it longer and adding uppercase letters, numbers, or special characters."

    # Detailed feedback
    improvement_suggestions = []
    if not strength_criteria['length']:
        improvement_suggestions.append("Make your password at least 8 characters long.")
    if not strength_criteria['uppercase']:
        improvement_suggestions.append("Add some uppercase letters (A-Z).")
    if not strength_criteria['lowercase']:
        improvement_suggestions.append("Include lowercase letters (a-z).")
    if not strength_criteria['digit']:
        improvement_suggestions.append("Add numbers (0-9).")
    if not strength_criteria['special_char']:
        improvement_suggestions.append("Include special characters like !@#$%^&*().")
    
    return strength, feedback, improvement_suggestions

# Main program to take input from the user
def password_strength_tool():
    password = input("Enter your password to assess its strength: ")
    
    strength, feedback, improvement_suggestions = assess_password_strength(password)
    
    print(f"\nPassword Strength: {strength}")
    print(f"Feedback: {feedback}")
    
    if improvement_suggestions:
        print("\nSuggestions for improvement:")
        for suggestion in improvement_suggestions:
            print(f"- {suggestion}")

# Run the program
password_strength_tool()
