import os
import openai
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAPI_API_KEY")

def chart(user):
    content = "My name is "+user.name+", I was born on "+user.date_of_birth+" in "+user.place_of_birth+". Today is the "+datetime.today().strftime('%Y-%m-%d')+"Write a message in the format of. “Hi Ben, what a beautiful day today to be a Sagittarius! <a short message about the zodiac sign>!”"
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an astrologer and have a long trajectory analizing birth chats. You sound professional and confident."},
        {"role": "user", "content": content}
    ]
    )
    return response['choices'][0]['message']['content']
