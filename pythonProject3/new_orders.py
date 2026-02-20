# Start with sandwiches to be made.
# and an empty list to hold the made ones.

sandwich_orders = ['french toast', 'pastrami sandwich', 'toasted bread', 'pastrami sandwich', 'breadsticks',
                   'pastrami sandwich', 'cheese sandwich']
finished_sandwiches = []

# Remove pastrami sandwich from the list
print("We have run out of pastrami sandwiches.")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders .remove('pastrami sandwich')
print(sandwich_orders)

while sandwich_orders:
    done_sandwiches = sandwich_orders.pop()

    print(f"I made you a {done_sandwiches}.")
    finished_sandwiches.append(done_sandwiches)

# Display all the sandwiches made.
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
