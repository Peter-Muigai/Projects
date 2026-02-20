# Start with a list of messages to text.
un_sent_messages = ['You can do it!', 'You got it.']
sent_messages = []

# Show the sending of the messages.
while un_sent_messages:
    current_messages = un_sent_messages.pop()
    print(f"\nThe following messages are being sent: {current_messages}")
    sent_messages.append(current_messages)

# Show the done messages.
print("\nThe following messages have been sent:")
for sent_message in sent_messages:
    print(sent_message)

