def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    status = "Standard user"

    if premium == True:
        status = "Premium user"

    return f"{username} age: {age} - {status}"

print(create_user_profile("Boonchoo", 40))
print(create_user_profile("Manee"))
print(create_user_profile("Piti", 23, True))
