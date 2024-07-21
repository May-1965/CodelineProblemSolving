import re

def validate_username(username):
    if not username:
        return False, "Username should not be empty."
    if len(username) > 50:
        return False, "Username is invalid! it should not exceed 50 characters."
    return True, "Username is valid."
##################################################
def validate_password(password):
    if len(password) < 8:
        return False, "Password is invalid! it must be at least 8 characters long."
    if not re.search(r'[()*&^%$#@!,.?":{}|<>]', password):
        return False, "Password is invalid! it should contain at least one special symbol."
    ##############################################
    if not re.search(r'[0-9]', password):
        return False, "Password is invalid! it should have one or more numbers."
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False, "Password is invalid! it must have one or more uppercase and lowercase characters."
    return True, "Password is valid."
###################################################
def validate_email(email):
    if "@" not in email:
        return False, "Email is invalid! it should have the '@' symbol."
    local, domain = email.split("@", 1)
    if not local or not domain:
        return False, "Email is invalid! it should have alphanumeric characters before and after the '@' symbol."######################
    domain_parts = domain.split(".")
    if len(domain_parts) < 2 or not all(part.isalpha() for part in domain_parts):
        return False, " Email is invalid! After the '@' symbol, it should have letters having . character in between."
    return True, "Email is valid."
####################################################
def main():
    print("Kindly enter your username, password and email:")

    while True:
        username = input("Username: ")
        valid, message = validate_username(username)
        print(message)
        if valid:
            break
################################################## 
    while True:
        password = input("Password: ")
        valid, message = validate_password(password)
        print(message)
        if valid:
            break
###################################################
    while True:
        email = input("Email: ")
        valid, message = validate_email(email)
        print(message)
        if valid:
            break

    print("Thank you, all inputs are valid")

if __name__ == "__main__":
    main()
