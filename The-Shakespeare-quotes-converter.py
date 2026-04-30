import csv 
def Shakespeare_translator(text):
 modern_map = {}
 with open('dictionary.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skips the header row (e.g., "old, modern")
    for row in reader:
                # row[0] is the old word, row[1] is the modern word
                if len(row) >= 2:
                         modern_map[row[0].strip().lower()] = row[1].strip()


    words = text.lower().split()
    translated  = [modern_map.get(word, word)for word in words]
    return " ".join(translated).capitalize()
 
while True:
    user_input = input("Enter a Shakespearean Line (or 'Q' for quit): ")
    if user_input == 'Q' or user_input == 'q':
        break
    print(f"modern remix : {Shakespeare_translator(user_input)}")
print('Thank you for using the Shakespeare Quote Converter!')