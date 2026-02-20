def show_messages(affirmations):
    """Display affirmations for individuals."""
    for affirmation in affirmations:
        msg = f"{affirmation}"
        print(msg)

motivations = ['You can do it!', 'You got it.']
show_messages(motivations)