import openai
from constants.personal_info import name

from os import listdir
print(listdir())


path = "constants/keys/key.key"
with open(path) as f:
    key = f.read()
    
openai.api_key = key

def generate_cover_letter(job_description, complete_times, temp = 0.5, resume = False):
    if resume:
        with open("inputs/resume.txt") as f:
            resume = f.load()    
    with open("inputs/bitze.txt") as f:
        bitze = f.read()
    prompt = f"""Person A has the resume below:
    {resume}
    He is applying to the job with the job description below:
    {job_description}

    Here is the draft cover letter for him which shows him has a free spirited and experienced journalist who became a self-thaught coder 
    
    Cover letter for him will be prepared. So that he will be free of Turkey which is a risky place for him as he wants to do real journalism uncovering unseen truths.
     
    What is the proof of this? Here is the project which he was inspired from his current job as the Trial Observer in Amnesty International Turkey Section:
    {bitze} 
    
    Here is the draft cover letter which will make him get the job above and will set him free: """
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        #max_tokens=1000,
        temperature=temp,
        n=complete_times,
        stop=None,
    )
    cover_letter_draft = response.choices[0].text.strip()

    # Replace placeholders with user-specific information
    cover_letter_draft = cover_letter_draft.replace("{{NAME}}", name)
    cover_letter_draft = cover_letter_draft.replace("{{ADDRESS}}", address)
    cover_letter_draft = cover_letter_draft.replace("{{SKILLS}}", skills)

    return cover_letter_draft
