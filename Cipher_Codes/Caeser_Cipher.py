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
root.geometry("400x300")

# Add widgets
instruction_label = tk.Label(root, text="Enter the encoded text and shift value:")
instruction_label.pack(pady=10)

encoded_text_label = tk.Label(root, text="Encoded Text:")
encoded_text_label.pack()
encoded_text_entry = tk.Entry(root, width=40)
encoded_text_entry.pack(pady=5)

shift_label = tk.Label(root, text="Shift Value:")
shift_label.pack()
shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)

decode_button = tk.Button(root, text="Decode", command=decode_message)
decode_button.pack(pady=10)

result_label = tk.Label(root, text="Decoded Message: ", fg="blue")
result_label.pack(pady=10)

# Run the application
root.mainloop()
