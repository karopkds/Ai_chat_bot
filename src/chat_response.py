def build_response(
    reply,
    intent,
    confidence,
    source,
    success=True,
):
    """
    Build a standard chatbot response.

    Every response returned by the chatbot
    follows the same structure.
    """

    return {
        "reply": reply,
        "intent": intent,
        "confidence": confidence,
        "source": source,
        "success": success,
    }