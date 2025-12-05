from langchain_google_genai import ChatGoogleGenerativeAI
import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash',
                             google_api_key=os.getenv('GOOGLE_API_KEY'))

def generate_content():
    """AI generates content about crypto"""
    prompt = """Create an X post about using PyCharm for beginners.
    Requirements:
    - Less than 280 characters
    - Provide a daily documentationtip
    - Introduce a new concept with a short example
    - Make it unique and fresh
    - No emojis. Keep it professional.
    """
    response = llm.invoke(prompt)
    content = response.content

    if len(content) > 280:
        content = content[:277] + "..."
    return content

def x_api_setup():
    client = tweepy.Client(
        bearer_token=os.getenv('X_BEARER_TOKEN'),
        consumer_key=os.getenv('X_API_KEY'),
        consumer_secret=os.getenv('X_API_SECRET'),
        access_token=os.getenv('X_ACCESS_TOKEN'),
        access_token_secret=os.getenv('X_ACCESS_SECRET')
    )
    return client

def post_on_x(client, content):
    client.create_tweet(text=content)
    print("Posted to X successfully!")
    return True

x_client = x_api_setup()
x_content = generate_content()
post_on_x(x_client, content=x_content)