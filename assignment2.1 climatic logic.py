"""
------------------------------------------------------------
Assignment 2.1 - Climatic Risk Intelligence Module
Course : Programming for Artificial Intelligence
Author : Punit Kumar

Description:
This program simulates an AI-based climatic risk intelligence
system. It accepts environmental telemetry such as temperature,
humidity, and wind speed to calculate the Heat Stress Index (HSI)
and classify the environment into one of four safety tiers.

Order of Evaluation:
1. Freeze Alert
2. Critical
3. Cautionary
4. Operational

Freeze Alert is checked first because even if humidity makes the
HSI numerically large, freezing conditions should always take
priority.

The walrus operator is used to validate empty input before
conversion. The try-except block handles invalid numeric input,
while assert ensures physically impossible humidity values are
not accepted.
------------------------------------------------------------
"""

print("========== Climatic Risk Intelligence Module ==========\n")

# -----------------------------
# Optional User Name
# -----------------------------
user_name = input("Enter User Name : ").strip() or "Guest User"

# -----------------------------
# Temperature Input
# -----------------------------
if not (temp_str := input("Temperature (°C): ").strip()):
    print("\nSafety Level : Unknown")
    exit()

try:
    temperature = float(temp_str)
except ValueError:
    print("\nSafety Level : Unknown")
    exit()

# -----------------------------
# Humidity Input
# -----------------------------
if not (humidity_str := input("Humidity (%): ").strip()):
    print("\nSafety Level : Unknown")
    exit()

try:
    humidity = float(humidity_str)
except ValueError:
    print("\nSafety Level : Unknown")
    exit()

# Assertion for humidity
assert humidity >= 0, "Telemetry Error: Negative Humidity"

# -----------------------------
# Wind Speed Input
# -----------------------------
if not (wind_str := input("Wind Speed (km/h): ").strip()):
    print("\nSafety Level : Unknown")
    exit()

try:
    wind_speed = float(wind_str)
except ValueError:
    print("\nSafety Level : Unknown")
    exit()

# -----------------------------
# Heat Stress Index
# -----------------------------
hsi = temperature + (0.5 * humidity)

# Ternary Operator
risk_label = "Safe" if hsi < 30 else "Unsafe"

# -----------------------------
# Decision Logic
# -----------------------------
if temperature <= 0:
    safety_level = "FREEZE ALERT"

elif hsi > 45 or (temperature > 38 and humidity > 70):
    safety_level = "CRITICAL"

elif 30 <= hsi <= 45 and wind_speed < 5:
    safety_level = "CAUTIONARY"

    # -----------------------------
    # Bonus Task
    # -----------------------------
    if not (battery_str := input("Battery Level (%): ").strip()):
        print("\nSafety Level : Unknown")
        exit()

    try:
        battery = float(battery_str)
    except ValueError:
        print("\nSafety Level : Unknown")
        exit()

    if battery < 20:
        safety_level = "CRITICAL"

    elif battery > 80:
        safety_level = "OPERATIONAL"

else:
    safety_level = "OPERATIONAL"

# -----------------------------
# Final Output
# -----------------------------
print("\n========== RESULT ==========")
print("User           :", user_name)
print("Temperature    :", temperature, "°C")
print("Humidity       :", humidity, "%")
print("Wind Speed     :", wind_speed, "km/h")
print("HSI            :", round(hsi, 2))
print("Risk Label     :", risk_label)
print("Safety Level   :", safety_level)
print("============================")