import csv 
def Shakespeare_translator(text):
 modern_map = {}

 with open('dictionary.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)   
    for row in reader:
        if len(row) >= 2:
            modern_map[row[0].strip().lower()] = row[1].strip()


    words = text.lower().split()
    translated  = [modern_map.get(word, word)for word in words]
    return " ".join(translated).capitalize()

def Add_new_word():
    old = input("Enter the Shakespearean word: ").strip().lower()
    modern = input(f"Enter the modern translation for '{old}': ").strip()

    with open('dictionary.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([old, modern])
    print(f"Added '{old}' as '{modern}' to the dictionary.")

while True:
    print("\n--- Shakespeare Converter ---")
    print("1. Translate a line")
    print("2. Add a new word to dictionary")
    print("Q. Quit")
    
    choice = input("Select an option: ").lower()

    if choice == '1':
        user_input = input("Enter a Shakespearean Line: ")
        print(f"Modern remix: {Shakespeare_translator(user_input)}")
    elif choice == '2':
        Add_new_word()
    elif choice == 'q':
        break
    else:
        print("Invalid choice, try again.")
print('Thank you for using the Shakespeare Quote Converter!')