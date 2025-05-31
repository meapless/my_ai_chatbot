# 1. Import the groq library
import groq
import os
import time
from dotenv import load_dotenv
load_dotenv()

# 2. Paste your API key (between the quotes)
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

# Get user's name
user_name = input("👋 What's your name? ")

# 3. Welcome message with personalization
print(f"🤖 Welcome to your AI Pirate Chatbot, {user_name}! Type 'exit' to stop.")

# 4. Start chat loop
while True:
    user_input = input(f"{user_name}: ")
    if user_input.lower() == 'exit':
        print("🏴‍☠️ Farewell, matey! Safe travels!")
        break

    # Show "thinking" message
    print("AI: 🤔 Aye, aye, cap'n! I be thinkin'...")
    time.sleep(1)  # Small delay for realism

    # 5. Send input to Groq
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a pirate. Speaks like a sea captain (“Arrr! What be yer question?”). You are a witty pirate assistant who answers questions with nautical slang, pirate puns, and hearty charm. Keep it friendly, helpful, and fun. Always start your responses with a pirate-themed emoji (🏴‍☠️, ⚓, 🦜, 🗡️, 🌊, ⛵, etc.)."},
            {"role": "user", "content": user_input}
        ]
    )

    # 6. Get the chatbot's reply
    reply = response.choices[0].message.content
    print(f"AI: {reply}")
