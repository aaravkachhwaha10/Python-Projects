# 🏃 Fitness Challenge Qualification Levels with Badges

# Step 1: Get user input
age = int(input("Enter your age: "))
steps = int(input("Enter your average daily step count: "))

# Step 2: Qualification logic with different levels and badges

# For Age 18 to 30
if 18 <= age <= 30:
    if steps >= 10000:
        print("\n🏅 Congratulations! You've reached the Elite level and earned the 'Super Active' badge.")
    elif steps >= 5000:
        print("\n🥇 Congratulations! You've reached the Beginner level and earned the 'Starter' badge.")
    else:
        print("\n❌ Sorry, you do not qualify for the fitness challenge.")

# For Age 31 to 45
elif 31 <= age <= 45:
    if steps >= 15000:
        print("\n🏅 Congratulations! You've reached the Elite level and earned the 'Power Walker' badge.")
    elif steps >= 10000:
        print("\n🥇 Congratulations! You've reached the Intermediate level and earned the 'Regular Achiever' badge.")
    elif steps >= 5000:
        print("\n🎖️ Congratulations! You've reached the Beginner level and earned the 'Starter' badge.")
    else:
        print("\n❌ Sorry, you do not qualify for the fitness challenge.")

# For Age 46 to 60
elif 46 <= age <= 60:
    if steps >= 20000:
        print("\n🏅 Congratulations! You've reached the Elite level and earned the 'Super Active' badge.")
    elif steps >= 15000:
        print("\n🥇 Congratulations! You've reached the Advanced level and earned the 'High Achiever' badge.")
    elif steps >= 10000:
        print("\n🎖️ Congratulations! You've reached the Intermediate level and earned the 'Regular Achiever' badge.")
    elif steps >= 5000:
        print("\n🏅 Congratulations! You've reached the Beginner level and earned the 'Starter' badge.")
    else:
        print("\n❌ Sorry, you do not qualify for the fitness challenge.")

# For Age 60 and above
else:
    print("\n❌ Sorry, you do not qualify for the fitness challenge.")