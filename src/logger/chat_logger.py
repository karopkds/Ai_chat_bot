import csv
from datetime import datetime
from pathlib import Path

class ChatLogger:
    """
    Handles chatbot conversation logging.
    """

    def __init__(self):
        self.log_file = Path("logs/chat_history.csv")

        if not self.log_file.exists():
            with open(self.log_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerow([
                    "timestamp",
                    "user_input",
                    "predicted_intent",
                    "confidence",
                    "response_source",
                    "bot_response"
                ])
    def log_chat(
    self,
    *,
    user_input: str,
    predicted_intent: str,
    confidence: float,
    response_source: str,
    bot_response: str,
    ) -> None:
        """
        Logs a chatbot conversation.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.log_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                timestamp,
                user_input,
                predicted_intent,
                confidence,
                response_source,
                bot_response
            ])