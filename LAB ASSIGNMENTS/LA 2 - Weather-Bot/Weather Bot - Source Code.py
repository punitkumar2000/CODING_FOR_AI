"""
Program : Weather-Bot 3000
Purpose : Gives simple lifestyle advice based on temperature and rain
Author  : Punit Kumar
Date    : 08 August 2026
"""

print("Welcome to your AI Climate Assistant.")
temp_input = input("What is the current temperature in Celsius?: ").strip()

if temp_input.isdigit():
    temperature = int(temp_input)

    if temperature > 30:
        print("AI Alert: It's hot! AI suggests turning on the AC.")
    elif temperature < 15:
        print("AI Alert: Chilly! AI suggests a jacket.")
    else:
        print("AI Analysis: Temperature is optimal. Enjoy your day!")

    rain_check = input("Is it raining outside? (yes/no): ")

    if "yes" in rain_check.lower() and temperature < 15:
        print("AI Recommendation: Stay indoors today, and carry an umbrella.")
    elif "yes" in rain_check.lower():
        print("AI Recommendation: Carry an umbrella.")
    else:
        print("AI Recommendation: No umbrella needed.")
else:
    print("Please enter the temperature as a valid number (digits only).")