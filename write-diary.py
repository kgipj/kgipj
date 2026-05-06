import datetime
import os

date = datetime.date.today()
date_str = f"{date.year}-{date.month}-{date.day}"

os.system(f"hugo new diaries/{date_str}.md")
