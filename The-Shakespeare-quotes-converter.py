def Shakespeare_translator(text):
    #dictionary mapping Elizabeth terms to modern slang 
    modern_map = {
        "thou": "you",
        "thee": "you",
        "thy": "your",
        "art": "are",
        "wherefore": "why",
        "hark": "listen",
        "fair": "beautiful",
        "plague": "disease",
        "doth": "does",
        "shalt": "will",
        "morrow": "morning",
        "hie": "hurry",
        "ay": "yes",
        "nay": "no"
    }


    words = text.lower().split()
    translated  = [modern_map.get(word, word)for word in words]

    return " ".join(translated).capitalize()

user_input = input("Enter a Shakespearean Line: ")
print(f"modern remix : {Shakespeare_translator(user_input)}")