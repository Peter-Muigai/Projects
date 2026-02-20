def send_messages(unsent_messages, sent_messages):
    """Simulate the sending of messages until none is left."""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending the following texts: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    """Show all the sent texts."""
    print("\nThe following texts have been sent: ")
    for sent_message in sent_messages:
        print(sent_message)

unsent_messages = ['You can do it!', 'You got it.']
sent_messages = []

# Call the function to send messages
send_messages(unsent_messages, sent_messages)
show_sent_messages(sent_messages)
