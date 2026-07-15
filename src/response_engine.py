import random

responses = {
    "greeting": [
        "Hello! How can I help you?",
        "Hi! What can I do for you today?",
        "Welcome! How may I assist you?"
    ],

    "goodbye": [
        "Goodbye! See you soon.",
        "Take care! Have a great day.",
        "See you next time!"
    ],

    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "Anytime!"
    ],

    "aws": [
        "AWS is Amazon Web Services.",
        "AWS is Amazon's cloud computing platform.",
        "AWS provides services like EC2, S3, IAM, Lambda, and RDS."
    ],

    "devops": [
        "DevOps combines development and operations.",
        "DevOps focuses on automation and continuous delivery.",
        "DevOps helps teams build and deploy software efficiently."
    ],

    "sports": [
        "Sports include Football, Cricket, Tennis, Basketball and many more.",
        "Sports are physical activities played individually or in teams.",
        "Popular sports include Cricket, Football, Basketball and Tennis."
    ]
}

def get_response(intent):
    if intent in responses:
        return random.choice(responses[intent])

    return "Sorry, I need more learning."