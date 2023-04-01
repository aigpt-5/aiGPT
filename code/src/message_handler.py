import random

def process_message(message):
    """Process and handle incoming message from user."""
    # Replace this with your custom message processing logic
    if message.lower() == 'hello':
        response = 'Hi there!'
    elif message.lower() == 'how are you?':
        response = random.choice(['I am doing well, thank you.', 'I am feeling great today!', 'I am a chatbot, I don\'t have emotions.'])
    else:
        response = 'I am sorry, I didn\'t understand your message.'

    return response