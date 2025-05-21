from datetime import date, timedelta
import random
import os

# Ensure the 'data' folder exists
os.makedirs("data", exist_ok=True)

# Date range
start_date = date(1960, 1, 1)
end_date = date(2020, 12, 31)

# Function to generate all formats for a given date
def date_formats(d):
    mm = d.strftime("%m")
    dd = d.strftime("%d")
    yyyy = d.strftime("%Y")
    yy = d.strftime("%y")

    return [
        mm + dd + yyyy,  # MMDDYYYY
        dd + mm + yyyy,  # DDMMYYYY
        yyyy + mm + dd,  # YYYYMMDD
        yyyy + dd + mm,  # YYYYDDMM
        yy + mm + dd,    # YYMMDD
        yy + dd + mm,    # YYDDMM
        dd + mm + yy,    # DDMMYY
        mm + dd + yy     # MMDDYY
    ]

# Generate all passwords
passwords = []
current = start_date
while current <= end_date:
    passwords.extend(date_formats(current))
    current += timedelta(days=1)

# Shuffle the list
random.shuffle(passwords)

# Save to data folder
output_path = "data/password_dictionary.txt"
with open(output_path, "w") as f:
    for password in passwords:
        f.write(password + "\n")

print(f"Generated {len(passwords)} passwords and saved to '{output_path}'.")
