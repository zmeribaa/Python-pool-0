import time
from datetime import datetime

seconds = time.time()

formatted_seconds = "{:,.4f}".format(seconds)

scientific = "{:.2e}".format(seconds)

date = datetime.fromtimestamp(seconds)
date_str = date.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific} in scientific notation")
print(date_str)
