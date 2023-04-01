import random

class ResponseGenerator:
    def __init__(self):
        self.greetings = ["Hello!", "Hi there!", "Greetings!", "Hey, how can I help you today?"]
        self.small_talk = ["How's your day going?", "Have you heard any good news lately?", "Did you see the latest sports results?"]
        self.services = ["We offer a variety of services, including ride sharing and grocery delivery. Which service can I help you with?", "How can I assist you with your order today?"]
        self.product_info = ["Sure, I'd be happy to provide more information. What product are you interested in?", "Let me check our database. What specific information do you need about the product?"]
        self.ordering = ["Great, let's get started. What would you like to order?", "Sure thing! Can you tell me more about what you're looking for?"]
        self.payment = ["We accept all major credit cards and PayPal. Which payment method would you prefer?", "We have a variety of payment options, including Apple Pay and Google Wallet. Which one would you like to use?"]
        self.customer_support = ["I'm sorry to hear that you're experiencing an issue. Can you tell me more about the problem?", "I'd be happy to assist you with any questions or concerns you have. What's on your mind?"]
        self.multi_language = ["Hola, ¿cómo puedo ayudarte hoy?", "Bonjour, comment puis-je vous aider aujourd'hui?", "こんにちは、今日はどうしたいですか？"]
        self.complex_scenarios = ["That's a great question. Let me look into it and get back to you shortly.", "I'm not sure about that, but I'll do my best to find out. Can you give me some more details?"]

    def generate_response(self, input_text):
        # Process the input text
        processed_text = process_text(input_text)

        # Check for keywords in input text and generate appropriate response
        if any(word in processed_text for word in ['hello', 'hi', 'hey']):
            response = random.choice(self.greetings)
        elif any(word in processed_text for word in ['how are you', 'how\'s it going']):
            response = random.choice(self.small_talk)
        elif any(word in processed_text for word in ['order', 'ride', 'delivery']):
            response = random.choice(self.services)
        elif any(word in processed_text for word in ['product', 'information']):
            response = random.choice(self.product_info)
        elif any(word in processed_text for word in ['order', 'buy']):
            response = random.choice(self.ordering)
        elif any(word in processed_text for word in ['payment', 'pay']):
            response = random.choice(self.payment)
        elif any(word in processed_text for word in ['complaint', 'issue', 'problem', 'question']):
            response = random.choice(self.customer_support)
        elif any(word in processed_text for word in ['hola', 'bonjour', 'こんにちは','صباح الخير']):
            response = random.choice(self.multi_language)
        else:
            response = random.choice(self.complex_scenarios)

        return response

response_generator = ResponseGenerator()

# Test response generator
print(response_generator.generate_response("Hello"))
print(response_generator.generate_response("How can I order a ride?"))
print(response_generator.generate_response("Can you tell me more about the product?"))
