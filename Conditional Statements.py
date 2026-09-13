print("=== Daily Activity Planner ===")


temperature = int(input("Enter the temperature (°C): "))
is_raining = input("Is it raining? (yes/no): ").strip().lower()
homework_time = int(input("How many hours of homework do you have today? "))
free_time = int(input("How many hours of free time do you have today? "))

print("\n--- Activity Recommendation ---")


if temperature >= 25 and is_raining == "no":
    print("It's warm and sunny. Great day for outdoor activities!")
elif temperature >= 15 and is_raining == "no":
    print("Nice weather. You could go for a walk or play outside.")
elif is_raining == "yes":
    print("It's raining. Indoor activities might be better.")
else:
    print("It's cold outside. Stay warm and consider indoor activities.")

if homework_time > 3:
    print("You have a lot of homework. Start with that first.")
elif homework_time > 0:
    print("You have some homework. Try finishing it early.")
else:
    print("No homework today. Enjoy your free time!")


if free_time >= 3:
    print("You have plenty of free time. Maybe try a hobby or play a game.")
elif free_time >= 1:
    print("You have a bit of free time. Relax or do something small.")
else:
    print("Not much free time today. Make the most of short breaks.")

print("\nPlan generated successfully!")