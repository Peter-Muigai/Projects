# Start with some designs that need to be printed.
un_printed_designs = ['phone case', 'bluetooth', 'RAM module']
completed_models = []
# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while un_printed_designs:
    current_designs = un_printed_designs.pop()
    print(f"Printing model: {current_designs}.")
    completed_models.append(current_designs)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
