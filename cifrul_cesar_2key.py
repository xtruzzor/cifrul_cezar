import tkinter as tk
from tkinter import messagebox

def apply_key_permutation(alphabet, key):
    key_set = set(key)
    permuted_alphabet = key
    for letter in alphabet:
        if letter not in key_set:
            permuted_alphabet += letter
    return permuted_alphabet

def remove_duplicates(string):
    seen = set()
    result = ""
    for char in string:
        if char not in seen:
            result += char
            seen.add(char)
    return result

def caesar_cipher(text, key1, key2, mode):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_alphabet = apply_key_permutation(alphabet, key2.upper())
    permuted_alphabet = remove_duplicates(new_alphabet)

    if mode == "encrypt":
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift = permuted_alphabet.index(char.upper())
                encrypted_text += permuted_alphabet[(shift + key1) % 26]
            else:
                encrypted_text += char
        return encrypted_text
    elif mode == "decrypt":
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shift = permuted_alphabet.index(char.upper())
                decrypted_text += permuted_alphabet[(shift - key1) % 26]
            else:
                decrypted_text += char
        return decrypted_text


def encrypt_decrypt():
    mode = mode_var.get()
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    message = message_entry.get().replace(" ", "").upper()

    if not key1.isdigit() or int(key1) < 1 or int(key1) > 25:
        messagebox.showerror("Erreur", "Clé invalide. Veuillez saisir un nombre entier compris entre 1 et 25.")
        return

    if len(key2) < 7 or not key2.isalpha():
        messagebox.showerror("Erreur", "Deuxième clé invalide. Veuillez saisir un mot contenant au moins 7 caractères alphabétiques.")
        return

    key1 = int(key1)

    if mode == "encrypt":
        encrypted_message = caesar_cipher(message, key1, key2, mode)
        result_label.config(text="Message crypté: " + encrypted_message)
    else:
        decrypted_message = caesar_cipher(message, key1, key2, mode)
        result_label.config(text="Message décrypté: " + decrypted_message)

root = tk.Tk()
root.title("Caesar Cipher")

mode_label = tk.Label(root, text="Sélectionnez le mode:")
mode_label.grid(row=0, column=0, padx=5, pady=5)

mode_var = tk.StringVar(value="encrypt")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt")
encrypt_radio.grid(row=0, column=1, padx=5, pady=5)

decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt")
decrypt_radio.grid(row=0, column=2, padx=5, pady=5)

key1_label = tk.Label(root, text="Entrez la première clé(1-25):")
key1_label.grid(row=1, column=0, padx=5, pady=5)

key1_entry = tk.Entry(root)
key1_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

key2_label = tk.Label(root, text="Entrez la deuxième clé(at least 7 letters):")
key2_label.grid(row=2, column=0, padx=5, pady=5)

key2_entry = tk.Entry(root)
key2_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

message_label = tk.Label(root, text="Entrez le message:")
message_label.grid(row=3, column=0, padx=5, pady=5)

message_entry = tk.Entry(root)
message_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

encrypt_decrypt_button = tk.Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt)
encrypt_decrypt_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
