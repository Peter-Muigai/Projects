# Start with sandwiches to be made.
# and an empty list to hold the made ones.
sandwich_orders = ['french toast', 'toasted bread', 'breadsticks', 'cheese sandwich']
finished_sandwiches = []

while sandwich_orders:
    done_sandwiches = sandwich_orders.pop()

    print(f"I made you a {done_sandwiches}.")
    finished_sandwiches.append(done_sandwiches)

# Display all the sandwiches made.
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
