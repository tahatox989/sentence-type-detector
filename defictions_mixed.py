def split(text):
    text = text.lower()
    output_text1 = text.split()
    return output_text1

def find(text):

    global txt

    verbs_for_imprative = ["can", "go", "come", "take", "put", "eat", "drink", "sit", "stand",
         "close", "open", "look", "listen", "wait", "stop", "run", "write",
         "study", "play", "please","برو", "بیا", "بخور", "بنشین", "بایست", "ببند", "بازکن", 
                           "نگاه", "گوش کن", "صبرکن", "ایست", "بنویس", "مطالعه کن", 
                           "بازی کن", "لطفا", "بردار", "بگذار", "بیاور", "ببر",
                           "بکن", "نکن", "لطفا", "بشین", "بزار", "نزار", "بخون",    
                           "نخون", "بیار", "نیار"]
    
    verbs_for_emitional = ["love", "hate", "happy", "sad", "angry", "excited", "scare",
        "scared", "tired", "bored", "boring", "beautiful""دوست دارم", "دوست داری", "عاشق", "متنفر", "خوشحال", 
                           "غمگین", "عصبانی", "هیجان زده", "میترسم", "ترسیده", 
                           "خسته", "کسل", "کسالت بار", "زیبا", "قشنگ", "عالی", 
                           "وحشتناک", "عاشق", "دوست ", "دوستت"]

    assert type(text) == list, "the input must be a list not another type !"

    n = len(text)

    if "hello" in text or "hello!" in text or "hello !"in text or "hello  !" in text:

        if txt.lower() == "hello" or txt.lower() == "hello!" or txt.lower() == "hello !" or txt.lower() == "hello  !" or txt.lower() == " hello " or txt.lower() == " hello!":

            return "simple(ساده)"

        if "?" in text[n - 1]:

            if text[0] == "is" or text[0] == "are" or text[0] == "am":
            
                return "asking(پرسشي)"
            
            elif "what" in text or "why" in text:

                return "asking(پرسشی)"
            
            elif text[0] in verbs_for_imprative:
                
                return "imperative(امري)"
            
            else:
                return "asking(پرسشي)"
        
        elif "!" in text[n - 1]:

            for i in verbs_for_emitional:

                if i in text:
                    
                    return "emitional(عاطفی)"
                #
        
            if "your" in text or "he" in text or "she" in text or "my" in text or "it" in text or "they" in text or "we" in text or "our" in text or "their" in text:
                
                return "declarative(خبري)"
            
            elif "yours" in text or "mine" in text or "his" in text or "hers" in text or "its" in text:

                return "declarative(خبری)"

            else:

                return "exclamatory(تعجبي)"
        
                
        else:

            return "simple(ساده)"

    elif "?" in text[n - 1]:   # when question mark in sentence(text):
        
        if text[0] == "is" or text[0] == "are" or text[0] == "am":
            
            return "asking(پرسشي)"
        elif "what" in text or "why" in text:

            return "asking(پرسشی)"
        
        elif text[0] in verbs_for_imprative:
            
            return "imperative(امري)"
        
        else:
            return "asking(پرسشي)"
        
    elif "!" in text[n - 1]:   # when Exclamation mark in sentence(text):
        
        for i in verbs_for_emitional:

            if i in text:

                return "emitional(عاطفی)"
            #
        
        if "your" in text or "he" in text or "she" in text or "my" in text or "it" in text or "they" in text or "we" in text or "our" in text or "their" in text:
            
            return "declarative(خبري)"


        else:
            return "exclamatory(تعجبي)"
        
    elif "." in text[n - 1]:
        
        if "your" in text or "he" in text or "she" in text or "my" in text or "it" in text or "they" in text or "we" in text or "our" in text or "their" in text:
            
            return "declarative(خبري)"
        
    elif text[0] == "can" or text[0] == "is" or text[0] == "are" or text[0] == "am":

        return "asking(پرسشی)"
    
    elif text[0] == "he" or text[0] == "she" or text[0] == "i" or text[0] == "i'm" or text[0] == "you" or text[0] == "you're" or text[0] == "he's" or text[0] == "she's":

        return "declarative(خبری)"
    
    else:
        
        return "please add a mark(?, !, .)"
    
        
def starting(text):
    global txt
    txt = text
    return find(split(text))


