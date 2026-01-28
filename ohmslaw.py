# Input voltage and resistance
V = float(input("Enter voltage (V): "))
R = float(input("Enter resistance (R): "))

# Calculate current using Ohm's Law
I = V / R

# Display current
print("Current (I) =", I, "A")

# Determine nature of current
if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")
