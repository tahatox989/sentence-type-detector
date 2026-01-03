def split(text):
    l1 = text.split()
    return l1

def last_points(text):

    verbs_for_imprative = ["can", "go", "come", "take", "put", "eat", "drink", "sit", "stand",
         "close", "open", "look", "listen", "wait", "stop", "run", "write",
         "study", "play", "please"]
    
    verbs_for_emitional = ["love", "hate", "happy", "sad", "angry", "excited", "scare",
        "scared", "tired", "bored", "boring", "beautiful"]

    assert type(text) == list, "the input must be a list not another type !"

    n = len(text)

    if "hello" in text or "hello!" in text or "hello !"in text or "hello  !" in text:

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

            if "your" in text or "he" in text or "she" in text or "my" in text or "it" in text or "they" in text or "we" in text or "our" in text or "their" in text:
            
                return "declarative(خبري)"

            elif verbs_for_emitional in text:

                return "Emotional(عاطفي)"

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
        
        if "your" in text or "he" in text or "she" in text or "my" in text or "it" in text or "they" in text or "we" in text or "our" in text or "their" in text:
            
            return "declarative(خبري)"

        elif "love" in text or "hate" in text or "happy" in text or "sad" in text or "angry" in text or "excited" in text or "scare" in text or "scared" in text or "tired" in text or "bored" in text or "beautiful" in text:

            return "Emotional(عاطفي)"

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
    return last_points(split(text))


