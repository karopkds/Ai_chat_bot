def is_contextual_followup(user_input, memory):

    if memory.last_intent is None:
        return False

    text = user_input.strip().lower()

    # Clearly a new question
    question_starters = (
        "what",
        "who",
        "where",
        "when",
        "why is",
        "how do",
        "how can",
        "which",
    )

    if text.startswith(question_starters):
        return False

    # Short contextual messages
    return len(text.split()) <= 4