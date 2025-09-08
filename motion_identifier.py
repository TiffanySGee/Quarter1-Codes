# Motion Type Identifier Program

# Function 1: Convert velocity to m/s
def convert_velocity(value, unit):
    """
    Convert velocity to meters per second (m/s)
    Supported units: m/s, ft/s, km/s, mi/s
    """
    unit = unit.lower()
    if unit == "m/s":
        return value
    elif unit == "ft/s":
        return value * 0.3048   # 1 ft = 0.3048 m
    elif unit == "km/s":
        return value * 1000     # 1 km = 1000 m
    elif unit == "mi/s":
        return value * 1609.34  # 1 mile = 1609.34 m
    else:
        print("Invalid velocity unit. Returning 0.")
        return 0.0

# Function 2: Convert acceleration to m/s²
def convert_acceleration(value, unit):
    """
    Convert acceleration to meters per second squared (m/s²)
    Supported units: m/s², ft/s², km/s², mi/s²
    """
    unit = unit.lower()
    if unit in ["m/s²", "m/s^2", "m/s'"]:
        return value
    elif unit in ["ft/s²", "ft/s^2", "ft/s'"]:
        return value * 0.3048   # ft → m
    elif unit in ["km/s²", "km/s^2", "km/s'"]:
        return value * 1000     # km → m
    elif unit in ["mi/s²", "mi/s^2", "mi/s'"]:
        return value * 1609.34  # mile → m
    else:
        print("Invalid acceleration unit. Returning 0.")
        return 0.0

# Function 3: Determine motion type
def motion_type(v, a):
    """
    Determine the type of motion based on velocity and acceleration
    Rules:
    - v > 0 and a = 0 → "Uniform Motion"
    - v > 0 and a > 0 → "Accelerated Motion"
    - v > 0 and a < 0 → "Decelerated Motion"
    - v = 0 → "At Rest"
    """
    if v == 0:
        return "At Rest"
    elif v > 0 and a == 0:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    else:
        return "Unknown Motion"

# --- Main Program ---

# Step 1: Input velocity
v_value = float(input("Enter velocity value: "))
v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

# Step 2: Input acceleration
a_value = float(input("Enter acceleration value: "))
a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")

# Step 3: Convert to SI units
v_si = convert_velocity(v_value, v_unit)
a_si = convert_acceleration(a_value, a_unit)

# Step 4: Determine motion type
motion = motion_type(v_si, a_si)

# Step 5: Display results
print("\n--- Results ---")
print(f"Velocity = {v_si:.3f} m/s")
print(f"Acceleration = {a_si:.3f} m/s²")
print(f"Motion Type = {motion}")