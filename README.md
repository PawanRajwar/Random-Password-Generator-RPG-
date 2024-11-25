# Random Password Generator ( RPG )

## Overview

This application is a Random Password Generator built using Python with a graphical user interface (GUI) created using the tkinter library. The program allows users to generate secure passwords of customizable length. It guarantees at least one character from each category (uppercase letters, lowercase letters, digits, and special characters) for robust password security. Additionally, users can copy the generated password to the clipboard.

## Features
1. Random Password Generation:
   - Customizable password length (minimum of 4 characters).

   - Includes at least one of each: uppercase letter, lowercase letter, digit, and special character.

   - Shuffles characters to ensure randomness.

2. User-Friendly Interface:
   - Input field to specify password length.

   - Button to generate passwords with instant display.

   - Button to copy the password to the clipboard for easy use.

3. Error Handling:
   - Alerts users if the password length is invalid (e.g., less than 4 or non-numeric).


## How It Works

### Components:

1. Password Length Input:
   - An input field where users specify the desired length of the password.

   - Ensures that the length is a valid number and is at least 4.

2. Generate Password Button:
   - Validates the length entered by the user.

   - Generates a password by:
     - Ensuring at least one uppercase letter, lowercase letter, digit, and special character.

     - Filling the remaining characters with a random selection from all categories.

     - Shuffling the final password to maximize randomness.

    - Displays the generated password in the output field.

3. Password Output Field:
   - A text field where the generated password is displayed.

4. Copy to Clipboard Button:
   - Copies the displayed password to the clipboard for use elsewhere.

   - Displays a confirmation message when successful.

5. Error and Warning Messages:
   - Alerts users if they input an invalid length or try to copy a password when none has been generated.