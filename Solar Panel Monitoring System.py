# Solar Panel Monitoring System
# Easy Python Code

voltage = float(input("Enter solar panel voltage (V): "))
current = float(input("Enter solar panel current (A): "))

# Calculate power
power = voltage * current

print("\n--- SOLAR PANEL MONITOR ---")
print("Voltage :", voltage, "V")
print("Current :", current, "A")
print("Power   :", round(power, 2), "W")

# Panel status
if power >= 100:
    print("Status  : GOOD")
elif power >= 50:
    print("Status  : NORMAL")
else:
    print("Status  : LOW POWER")
