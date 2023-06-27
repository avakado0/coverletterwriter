from src import main
from inputs import skillss
import time
from plyer import notification
cover_letter_tasks = [
    "Step 1: Analyze job requirements",
    "Step 2: Highlight relevant skills and experience",
    "Step 3: Craft an engaging introduction",
    # Add more steps as needed
]

softs = skillss.soft_skills
codes = skillss.coding_skills
#from ..constants.personal_info import soft_skills, coding_skills, name, address
print("Has the job description been added to the inputs/job_desc.txt ? (y/n) => ", end = "");  file_inplace = input() 
if file_inplace.lower() == 'y':
    with open("inputs/job_desc.txt") as f:
        job_desc = f.read()
elif file_inplace.lower() == 'n':
    pass
else:
    raise Exception
output = main.generate_cover_letter(job_description=job_desc, complete_times=1)
print(output)
#temperature 'ile oyna ilerde