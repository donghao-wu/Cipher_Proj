import tkinter as tk
from tkinter import messagebox, ttk

# Function to decode a Caesar Cipher encoded string
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
            decoded_char = chr((ord(char) - start + shift) % 26 + start)
            decoded_text += decoded_char
        else:
            decoded_text += char  # Non-alphabet characters remain unchanged
    return decoded_text

#example use: the text you want to transform to caesar cipher is 'dog', the shift you want to make is 1
#print(caesar_code("dog", 1))  the result will be cnf

# Function for the error message
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
root.configure(bg="black")

# Styling
label_font = ("Fixedsys", 12, "bold")
entry_font = ("Fixedsys", 12)
button_font = ("Fixedsys", 12, "bold")

# Create instruction widgets
instruction_label = tk.Label(root, text="Enter the encoded text and shift value:", font=label_font, bg="black", fg="white")
instruction_label.pack(pady=10) #pady is space between the widgets

# Create input widgets (frame for the input)
frame = tk.Frame(root, bg="black")
frame.pack(pady=5)

#Create input fields for encoded text and shift value
encoded_text_label = tk.Label(frame, text="Encoded Text:", font=label_font, bg="black", fg="#ECF0F1")
encoded_text_label.grid(row=0, column=0, padx=5, pady=5)
encoded_text_entry = tk.Entry(frame, width=30, font=entry_font)
encoded_text_entry.grid(row=0, column=1, padx=5, pady=5)

shift_label = tk.Label(frame, text="Shift Value:", font=label_font, bg="black", fg="#ECF0F1")
shift_label.grid(row=1, column=0, padx=5, pady=5)
shift_entry = tk.Entry(frame, width=10, font=entry_font)
shift_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the decode button
style = ttk.Style()
style.configure("Rounded.TButton", font=button_font, padding=10, relief="flat", background="#1ABC9C")
style.map("Rounded.TButton", background=[("active", "#16A085"), ("!active", "#1ABC9C")])

decode_button = tk.Button(root, text="Decode", font=button_font, bg="#1ABC9C", fg="white", command=decode_message, padx=10, pady=5)
decode_button.pack(pady=15)

result_label = tk.Label(root, text="Decoded Message:", font=label_font, bg="black", fg="#1ABC9C")
result_label.pack(pady=10)

# Run the application
root.mainloop()

