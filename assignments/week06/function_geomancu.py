def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    if premium == True:
        status = "Premium User"
    else:
        status = "Standard User"
    input(print("Enter username: "))
    input(int("Enter age: "))
    input(bool("Enter premium status: "))
    print(f"{username} age: {age} - {status}")

print("User Profile")
print(create_user_profile("Boonchoo", 40))
print(create_user_profile("Manee"))
print(create_user_profile("Piti", 23, True))