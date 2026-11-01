messages = [
    "Halo, apa kabar?",
    "Jangan lupa belajar Python hari ini ya.",
    "Semoga harimu menyenangkan!"
]
sent_messages = []

def send_messages(unsent_messages, sent_messages_list):
    """Mencetak pesan dan memindahkannya ke list sent_messages."""
    while unsent_messages:
        current_message = unsent_messages.pop(0)
        print(f"Mengirim pesan: '{current_message}'")
        sent_messages_list.append(current_message)

send_messages(messages[:], sent_messages)

print("\n--- List Asli (Tetap Utuh) ---")
print(messages)

print("\n--- List Pesan Terkirim (Sent Messages) ---")
print(sent_messages)