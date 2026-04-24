Def shakespeare_translator(text): 
    #dictionary mapping Elizabeth terms to modern slang 
    slang_map = { 
        "thou" : "You"
        "art" : "are"
        "wherefore" : "why"
        "hark": "listen"
        "fair" : "aesthetic"
        "plague" : "sickness"
    }

    Words = text.lower().spilt()
    translated  = [slang_map.get(Word, Word)for word in Words]

    return " ".join(translated).capitalize()

user_input = input("Enter a Shakespearean Line: ")
print(f"modern remix : {Shakespeare_translator(user_input)}")