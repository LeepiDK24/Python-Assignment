import re

def validate_password(password, username=None, previous_passwords=None):
    # Check minimum length
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."

    # Check character variety
    if not re.search(r"[A-Z].*[A-Z]", password):
        return False, "Password must contain at least two uppercase letters."
    if not re.search(r"[a-z].*[a-z]", password):
        return False, "Password must contain at least two lowercase letters."
    if not re.search(r"\d.*\d", password):
        return False, "Password must contain at least two digits."
    if not re.search(r"[!@#$%&*].*[!@#$%&*]", password):
        return False, "Password must contain at least two special characters."

    # Check sequence and repetition restrictions
    for i in range(len(password) - 2):
        # Check for sequence of three or more consecutive characters from the username
        if username and password[i:i+3] in username:
            return False, "Password should not contain any sequence of three or more consecutive characters from the username."
        # Check for any character repeating more than three times in a row
        if password[i] == password[i+1] == password[i+2] == password[i+3]:
            return False, "No character should repeat more than three times in a row."

    # Check historical password check
    if previous_passwords:
        for prev_password in previous_passwords[-3:]:
            if password == prev_password:
                return False, "New password must not be the same as the last three passwords used by the user."

    return True, "Password is valid."

# Example usage
username = "john_doe"
previous_passwords = ["password1", "password2", "password3", "password4"]
password = "Passw0rd@123"
result, message = validate_password(password, username, previous_passwords)
print(message)
