# turkish-autocomplete
A tool for typing Turkish while using English keyboard. Ex: hic -> hiç, kucuk -> küçük

Works in python 3.7 and uses pynput

Sorry for the messy code you will see :P

## How to use
Just clone the repo and run the file in terminal
>python3 autocomplete.py

You can press ESC key to stop the program


Note: You might need to start it with sudo because in the end it listens and controls your keyboard.
>sudo python3 autocomplete.py

This code is only tested in Mac OS 10.14

## Technical Issue
This code can't autocomplete 'ş' and 'ğ' characters since there is no combination to make them in english keyboard.
