import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, key, mode):
    if mode == "encrypt":
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                encrypted_text += chr((ord(char) - shift + key) % 26 + shift)
            else:
                encrypted_text += char
        return encrypted_text
    elif mode == "decrypt":
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - shift - key) % 26 + shift)
            else:
                decrypted_text += char
        return decrypted_text


def encrypt_decrypt():
    mode = mode_var.get()
    key = key_entry.get()
    message = message_entry.get().replace(" ", "").upper()

    if not key.isdigit() or int(key) < 1 or int(key) > 25:
        messagebox.showerror("Erreur", "Clé invalide. Veuillez saisir un nombre entier compris entre 1 et 25.")
        return

    key = int(key)

    if mode == "encrypt":
        encrypted_message = caesar_cipher(message, key, mode)
        result_label.config(text="Message crypté: " + encrypted_message)
    else:
        decrypted_message = caesar_cipher(message, key, mode)
        result_label.config(text="Message décrypté : " + decrypted_message)


root = tk.Tk()
root.title("Caesar Cipher")


mode_label = tk.Label(root, text="Sélectionnez le mode:")
mode_label.grid(row=0, column=0, padx=5, pady=5)

mode_var = tk.StringVar(value="encrypt")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt")
encrypt_radio.grid(row=0, column=1, padx=5, pady=5)

decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt")
decrypt_radio.grid(row=0, column=2, padx=5, pady=5)


key_label = tk.Label(root, text="La touche Entrée (1-25):")
key_label.grid(row=1, column=0, padx=5, pady=5)

key_entry = tk.Entry(root)
key_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)


message_label = tk.Label(root, text="Entrez le message :")
message_label.grid(row=2, column=0, padx=5, pady=5)

message_entry = tk.Entry(root)
message_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)


encrypt_decrypt_button = tk.Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt)
encrypt_decrypt_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)


result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
