import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def generate_password():
    try:
        length = int(length_input.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        # Characters to use in the password
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation
