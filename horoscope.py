import os
import openai
from datetime import date
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAPI_API_KEY")

def chart(name, day, month, year, place, current_date):
    content = "My name is "+name+", I was born on "+month+"/"+str(day)+"/"+str(year)+" in "+place+". Today is the "+current_date+"Write a message in the format of. “Hi Ben, what a beautiful day today to be a Sagittarius! <a short message about the zodiac sign>!”"
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an astrologer and have a long trajectory analizing birth chats. You sound professional and confident."},
        {"role": "user", "content": content}
    ]
    )
    return response['choices'][0]['message']['content']

print(chart("Steve", "13", "2", "2002", "russia", "20/06/2023"))