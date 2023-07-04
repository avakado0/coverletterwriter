import openai
import json
from os import listdir
print(listdir('constants/keys'))


path = "constants/keys/key.key"
with open(path) as f:
    key = f.read()
    
openai.api_key = key

def generate_cover_letter(job_description, complete_times, temp = 0.5, resume = False, max_tokens = 300):
    if resume:
        with open("inputs/resume.txt") as f:
            resume = f.load()    
    with open("inputs/bitze.txt") as f:
        bitze = f.read()
    imported = get_personal_info_from_file()
    name, address, skills = imported['name'], imported['address'],imported['skills']
    prompt = f"""Person with the name {name}, and address "{address}" has the resume below:
    {resume}
    His skills are: {skills}

    He is applying to the job with the job description below:
    {job_description}

    Here is the draft cover letter for him which shows him has a free spirited and experienced journalist who became a self-thaught coder 
    
    Chat gpt will prepare him a striking letter for him will be prepared. So that he will be free of Turkey which is a risky place for him as he wants to do real journalism uncovering unseen truths.
     
    What is the proof of this? Here is the project which he was inspired from his current job as the Trial Observer in Amnesty International Turkey Section:
    {bitze} 
    
    Here is the draft cover letter which will make him get the job above and will set him free: """
    print(f'Input prompt:\n{prompt}')
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        #max_tokens=1000,
        temperature=temp,
        n=complete_times,
        stop=None,
        max_tokens=max_tokens,
    )
    responses = dict(response)
    responses['response_prompt_text'] = response.text
    responses = json.dumps(responses)
    write_to_file(responses)    
    # Replace placeholders with user-specific information
    #cover_letter_draft = cover_letter_draft.replace("{{NAME}}", name)
    #cover_letter_draft = cover_letter_draft.replace("{{ADDRESS}}", address)
    #cover_letter_draft = cover_letter_draft.replace("{{SKILLS}}", skills)

    return responses

def write_to_file(obj):
    with open('outputs/output.json', 'w') as f:
        text = json.dumps(obj)
        f.write(text)
def get_personal_info_from_file():
    with open('constants/personal.info', 'r') as personal:
        taken_from_file = [x for x in personal.readlines() if x.strip()]
        name, address = taken_from_file
    with open('constants/skills.json', 'r') as skills:
        text = skills.read()
        skills = json.loads(text)
    return {
        'name': name,
        'address': address,
        'skills': skills
    }
