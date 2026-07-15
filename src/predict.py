from chat_engine import process_message


while True:

    user_input = input("YOU: ")

    if user_input.lower() == "exit":
        print("GOODBYE! See you Soon :)")
        break

    result = process_message(user_input)

    print("\n" + "=" * 60)
    print(f"Intent      : {result['intent']}")
    print(f"Confidence  : {result['confidence']:.2%}")
    print(f"Source      : {result['source']}")
    print("=" * 60)

    print("KDS_BOT:", result["reply"])
    print()