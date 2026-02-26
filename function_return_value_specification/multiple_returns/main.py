# using miltiple return values
def validate_registration(username, email, password):
    errors = []
# test username length
    if len(username) < 3:
        errors.append("Username must be at least 3 characters long.")
# test for @ in email
    if ("@" in email) == False:
        errors.append("Invalid email format.")
# test for password length
    if len(password) < 6:
        errors.append("Password must be at least 6 characters long.")

    return (len(errors) == 0, errors)

# Testing the result
is_valid, errors = validate_registration("js", "userexample.com", "123")
print("Validation successful:", is_valid)
print("Errors:", errors)