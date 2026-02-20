def print_models(un_printed_designs, completed_designs):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = un_printed_designs.pop()
        print(f"Printing model: {current_design}")
        completed_designs.append(current_design)
def show_completed_models(completed_designs):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_design in completed_designs:
        print(completed_design)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)