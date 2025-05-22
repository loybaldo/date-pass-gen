import os
import random
from datetime import date, datetime, timedelta

# Ensure the "data" folder exists
os.makedirs("data", exist_ok=True)

# Date range
start_date = date(1960, 1, 1)
end_date = datetime.today().date()

# Settings
separators = ["", "-", "_", ".", "/", " "]  # Allowed separators
casing_funcs = [str.lower, str.upper, str.title]  # lowercase, UPPERCASE, Title
month_formats = ["%B", "%b"]  # Full and abbreviated month
day_formats = [
	lambda d: d.strftime("%d"),               # Leading zero (e.g. 01)
	lambda d: str(int(d.strftime("%d")))      # No leading zero (e.g. 1)
]
date_orders = [
	("month", "day", "year"),
	("day", "month", "year"),
	("year", "month", "day"),
	("year", "day", "month"),
]

# Function to generate all variations for a single date
def date_formats(d):
	yyyy = d.strftime("%Y")
	formats = []

	for m_fmt in month_formats:
		month_str = d.strftime(m_fmt)

		for day_fmt in day_formats:
			dd_str = day_fmt(d)

			for case_func in casing_funcs:
				month_cased = case_func(month_str)

				for sep in separators:
					for order in date_orders:
						parts = []
						for part in order:
							if part == "year":
								parts.append(yyyy)
							elif part == "month":
								parts.append(month_cased)
							elif part == "day":
								parts.append(dd_str)
						formats.append(sep.join(parts))

	# Add numeric-only formats
	mm = d.strftime("%m")
	dd = d.strftime("%d")
	d_no_zero = str(int(dd))

	formats.extend([
		mm + dd + yyyy,             # MMDDYYYY
		dd + mm + yyyy,             # DDMMYYYY
		yyyy + mm + dd,             # YYYYMMDD
		yyyy + dd + mm,             # YYYYDDMM
		d_no_zero + mm + yyyy,
		mm + d_no_zero + yyyy,
		yyyy + mm + d_no_zero,
		yyyy + d_no_zero + mm,
	])

	return formats

# Generate all passwords
passwords = set()
current = start_date
while current <= end_date:
	passwords.update(date_formats(current))
	current += timedelta(days=1)

# Shuffle and save
passwords = list(passwords)
random.shuffle(passwords)

output_path = "data/date_dictionary.txt"
with open(output_path, "w", encoding="utf-8") as f:
	for password in passwords:
		f.write(password + "\n")

print(f'Generated {len(passwords)} unique passwords and saved to "{output_path}".')
