def is_spam_words(text, spam_words, space_around=False):
    
    letter_case = True
    new_text = text.split(" ")
    spam_words_str = ', '.join(spam_words)
    spam_word = spam_words_str.split(" ")

    if space_around == False : 
        
        if letter_case == True:
            
            for word in new_text:
                print("first if")
                for spam in spam_word:
                    
                    if word == spam.casefold() :
                        return True 
            return False     
        for word in new_text:
            print("first if first")
            for spam in spam_word:
                if word == spam :
                    return True 
        return False   
    else:
        if letter_case == False:
            
            for word in new_text:
                print("second if")
                for spam in spam_word:
                    if word == spam or (word.find(spam) == 0 and spam != ""):
                        return True 
            return False   
        for word in new_text:
            print("second if second")
            for spam in spam_word:
            
                if word == spam.casefold() or (word.find(spam.casefold()) == 0 and spam != ""):
                    return True 
        return False     
     
        
    
print(is_spam_words("hello mather facker", ["Facker off", "coco"]))            