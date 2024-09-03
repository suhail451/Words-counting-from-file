import tkinter as tk
from tkinter import filedialog

def amount(count):
    amount_per_word = int(input("Enter the amount per word: "))
    result = amount_per_word * count
    print(f"Total file amount: {result}")

def count_words_in_file():
    # Setting up the GUI
    root = tk.Tk()
    root.withdraw()  # Hides the root window
    

    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])
    
    if not file_path:
        print("No file selected. Exiting.")
        return
    
    # Reading the file content
    with open(file_path, "r") as f:
        data = f.read()

    # converting string into list of words
    word_list = data.split()

    # Counting the words in the list
    count = len(word_list)
    print(f"{count} words in file {file_path}")

    choice = input(f"Do you want to calculate the price for the file (Y) or press Enter to exit\n")
    if choice.upper() == "Y":
        amount(count)


count_words_in_file()
