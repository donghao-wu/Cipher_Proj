import tkinter as tk
from tkinter import messagebox
def caesar_code(encoded_text, shift):
    """
    Decodes a Caesar Cipher encoded string.

    :param encoded_text: The encoded string to decode.
    :param shift: The number of positions each letter was shifted in the cipher.
    :return: The decoded string.
    """
    decoded_text = ""

    for char in encoded_text:
        if char.isalpha():  # Check if character is a letter
            start = ord('A') if char.isupper() else ord('a')
            decoded_char = chr((ord(char) - start - shift) % 26 + start)
            decoded_text += decoded_char
        else:
            decoded_text += char  # Non-alphabet characters remain unchanged
    return decoded_text

#example use: the text you want to transform to caesar cipher is 'dog', the shift you want to make is 1
#print(caesar_code("dog", 1))  the result will be cnf

def decode_message():
    encoded_text = encoded_text_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    decoded_message = caesar_code(encoded_text, shift)
    result_label.config(text=f"Decoded Message: {decoded_message}")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Decoder")
root.geometry("450x350")
root.configure(bg="#2C3E50")

# Styling
label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

instruction_label = tk.Label(root, text="Enter the encoded text and shift value:", font=label_font, bg="#2C3E50", fg="#ECF0F1")
instruction_label.pack(pady=10)

frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=5)

encoded_text_label = tk.Label(frame, text="Encoded Text:", font=label_font, bg="#2C3E50", fg="#ECF0F1")
encoded_text_label.grid(row=0, column=0, padx=5, pady=5)
encoded_text_entry = tk.Entry(frame, width=30, font=entry_font)
encoded_text_entry.grid(row=0, column=1, padx=5, pady=5)

shift_label = tk.Label(frame, text="Shift Value:", font=label_font, bg="#2C3E50", fg="#ECF0F1")
shift_label.grid(row=1, column=0, padx=5, pady=5)
shift_entry = tk.Entry(frame, width=10, font=entry_font)
shift_entry.grid(row=1, column=1, padx=5, pady=5)

decode_button = tk.Button(root, text="Decode", font=button_font, bg="#1ABC9C", fg="white", command=decode_message, padx=10, pady=5)
decode_button.pack(pady=15)

result_label = tk.Label(root, text="Decoded Message:", font=label_font, bg="#2C3E50", fg="#F39C12")
result_label.pack(pady=10)

# Run the application
root.mainloop()

