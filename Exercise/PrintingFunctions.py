def print_models(unprinted_designs, completed_models):
    """Mensimulasikan pencetakan setiap desain hingga habis."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Menampilkan semua model yang telah dicetak."""
    print("\nModel berikut telah dicetak:")
    for completed_model in completed_models:
        print(completed_model)