class ConversationMemory:

    def __init__(self):
        self.last_intent = None
        self.last_user_message = None
        self.last_bot_response = None

    def update(self, intent, user_message, bot_response):
        self.last_intent = intent
        self.last_user_message = user_message
        self.last_bot_response = bot_response

    def clear(self):
        self.last_intent = None
        self.last_user_message = None
        self.last_bot_response = None