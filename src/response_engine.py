response = {
    "greeting" : "Hello! How Can I Help You?",
    "goodbye": "Goodbye!, See You Soon :)",
    "thanks": "You're welcome!",
    "aws": "AWS is Amazon Web Services.",
    "devops": "DevOps combines development and operations.",
    "sports" : "Sports contains FoodBall, Cricket and many more"
}

def get_response(intent):
    return response.get(intent, "Sorry i need more Learning.")