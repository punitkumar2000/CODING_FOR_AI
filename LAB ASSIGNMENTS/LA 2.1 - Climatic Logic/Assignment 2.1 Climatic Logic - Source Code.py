"""
------------------------------------------------------------
Assignment 2.1 - Climatic Risk Intelligence Module
Course : Programming for Artificial Intelligence
Author : Punit Kumar
Date   : August 2026

Description:
This program simulates an AI-based climatic risk intelligence
system. It accepts temperature, humidity, and wind speed
telemetry and calculates the Heat Stress Index (HSI).

The environment is classified into four safety tiers:

1. FREEZE ALERT
2. CRITICAL
3. CAUTIONARY
4. OPERATIONAL

The tiers are evaluated in this exact order because Freeze Alert
must always take priority over heat-related conditions.

The walrus operator (:=) is used to capture and validate empty
input before conversion. The try-except block handles invalid
numeric input, while an assertion prevents negative humidity.

The bonus feature asks for battery level only when the initial
classification is CAUTIONARY.
------------------------------------------------------------
"""

print("========== Climatic Risk Intelligence Module ==========\n")


# -----------------------------
# Optional User Name
# -----------------------------
user_name = input("Name : ").strip() or "Guest User"


# -----------------------------
# Temperature Input
# -----------------------------
if not (temp_str := input("Temperature (C) : ").strip()):
    print("Safety Level : Unknown")
    exit()

try:
    temperature = float(temp_str)
except ValueError:
    print("Safety Level : Unknown")
    exit()


# -----------------------------
# Humidity Input
# -----------------------------
if not (humidity_str := input("Humidity (%) : ").strip()):
    print("Safety Level : Unknown")
    exit()

try:
    humidity = float(humidity_str)
except ValueError:
    print("Safety Level : Unknown")
    exit()


# Negative humidity is physically impossible
assert humidity >= 0, "Telemetry Error: Negative Humidity"


# -----------------------------
# Wind Speed Input
# -----------------------------
wind_str = input("Wind Speed (km/h) : ").strip()

if wind_str:
    try:
        wind_speed = float(wind_str)
    except ValueError:
        print("\nSafety Level : Unknown")
        exit()
else:
    wind_speed = 0.0

# -----------------------------
# Heat Stress Index
# -----------------------------
hsi = temperature + (0.5 * humidity)


# Ternary expression required by assignment
risk_label = "Safe" if hsi < 30 else "Unsafe"


# -----------------------------
# Decision Logic
# -----------------------------

# 1. Freeze Alert
if temperature <= 0:
    safety_level = "FREEZE ALERT"


# 2. Critical
elif hsi > 45 or (temperature > 38 and humidity > 70):
    safety_level = "CRITICAL"


# 3. Cautionary
elif 30 <= hsi <= 45 and wind_speed < 5:
    safety_level = "CAUTIONARY"

    # -----------------------------
    # Bonus: Battery-Level Check
    # -----------------------------
    if not (battery_str := input("Battery Level (%) : ").strip()):
        print("Safety Level : Unknown")
        exit()

    try:
        battery = float(battery_str)
    except ValueError:
        print("Safety Level : Unknown")
        exit()

    if battery < 20:
        safety_level = "CRITICAL"

    elif battery > 80:
        safety_level = "OPERATIONAL"


# 4. Operational
else:
    safety_level = "OPERATIONAL"


# -----------------------------
# Final Output
# -----------------------------
print("\n========== RESULT ==========")
print("Name           :", user_name)
print("Temperature    :", temperature, "C")
print("Humidity       :", humidity, "%")
print("Wind Speed     :", wind_speed, "km/h")
print("HSI            :", round(hsi, 2))
print("Risk Label     :", risk_label)
print("Safety Level   :", safety_level)
print("============================")