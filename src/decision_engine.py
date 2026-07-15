def is_contextual_followup(user_input, memory):
    """
    Determines whether the user's message is a
    contextual follow-up to the previous conversation.
    """

    if memory.last_intent is None:
        return False

    word_count = len(user_input.split())

    if word_count <= 4:
        return True

    return False