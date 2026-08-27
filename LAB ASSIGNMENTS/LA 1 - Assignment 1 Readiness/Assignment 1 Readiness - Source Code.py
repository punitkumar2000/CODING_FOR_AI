"""
Program : Temporal Profile Analyzer
Purpose : Computes an AI Era Readiness Score from user metadata.
Author : Punit Kumar
Date : 08 August 2026
"""

from datetime import date


def numeric_age(age):
    return age.isdigit()


def temporal_profile_analyzer():

    """ Here user have to write their full name """
    full_name = input("Enter Your Full Name: ").strip()

    if not full_name:
        print("Please Enter Your Full Name")
        return

    # Age Input as numeric
    current_age = input("Enter Your Current Age: ")

    if not numeric_age(current_age):
        print("Please Enter a Valid Numeric Age")
        return

    # converting from str to int (as in the input the variable value is str)
    current_age = int(current_age)

    # Name Analysis
    formatted_name = full_name.title()
    name_length = len(full_name)

    # Finding current year using datetime libra 
    current_year = date.today().year

    # Projected Age in 2045
    age_in_2045 = current_age + (2045 - current_year)

    # AI Readiness Score
    ai_readiness_score = ((name_length * 10) + age_in_2045) / 2

    # Bonus - repeating the name based on first digit of age
    # age // 10 gives first digit for two digit age, but for single
    # digit age like 7, 7 // 10 = 0, so we need to treat that as 1 time
    first_digit = current_age // 10
    if first_digit == 0:
        first_digit = 1

    repeated_name = formatted_name * first_digit

    # Output
    print("\n========== Temporal Profile Analyzer ==========")
    print(f"Formatted Name        : {formatted_name}")
    print(f"Identifier Byte-Count : {name_length}")
    print(f"Current Age           : {current_age}")
    print(f"Current Year          : {current_year}")
    print(f"Projected Age (2045)  : {age_in_2045}")
    print(f"AI Readiness Score    : {ai_readiness_score:.2f}")
    print(f"Repeated Name (Bonus) : {repeated_name}")
    print("===============================================")


temporal_profile_analyzer()