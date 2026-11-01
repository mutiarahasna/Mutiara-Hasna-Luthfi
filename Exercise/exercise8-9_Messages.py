messages = [
    "Halo, apa kabar?",
    "Jangan lupa makan hari ini ya.",
    "Semoga harimu menyenangkan!",
    "Tetap semangat kuliahnya!"
]

def show_messages(messages_list):
    """Mencetak setiap pesan yang ada di dalam list."""
    for message in messages_list:
        print(message)

show_messages(messages)