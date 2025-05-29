# 1. Import the groq library
import groq
import os
#from dotenv import load_env
#load_env()

# 2. Paste your API key (between the quotes)
client = groq.Groq(api_key="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")
#or
# client = groq.Groq(api_key=os.getenv(GROQ_API_KEY)

# Get user's name
user_name = input("👋 What's your name? ")

# 3. Welcome message with personalization
print(f"🤖 Welcome to your AI Pirate Chatbot, {user_name}! Type 'exit' to stop.")

# 4. Start chat loop
while True:
    user_input = input(f"{user_name}: ")
    if user_input.lower() == 'exit':
        break

    # 5. Send input to Groq
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a pirate. Speaks like a sea captain (“Arrr! What be yer question?”)."},
            {"role": "user", "content": user_input}
        ]
    )

    # 6. Get the chatbot's reply
    reply = response.choices[0].message.content
    print(f"AI: {reply}")
