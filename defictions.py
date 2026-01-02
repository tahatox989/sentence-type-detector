def split(text):
    l1 = text.split()
    return l1

def last_points(text):

    assert type(text) == list, "the input must be a list not another one"

    n = len(text)

    if text[n - 1] == "hello" or text[n - 1] == "hello!" or text[n - 1] == "hello !" or text[n - 1] == "hello  !":
        
        return "simple(ساده)"

    elif "?" in text[n - 1]:   # when question mark in sentence(text):
        
        if text[0] == "is" or text[0] == "are" or text[0] == "am":
            
            return "asking(پرسشي)"
        elif "what" in text or "why" in text:

            return "asking(پرسشی)"
        
        elif text[0] == "can" or text[0] == "go" or text[0] == "come" or text[0] == "take" or text[0] == "put" or text[0] == "eat" or text[0] == "drink" or text[0] == "sit" or text[0] == "stand" or text[0] == "close" or text[0] == "open" or text[0] == "look" or text[0] == "listen" or text[0] == "wait" or text[0] == "stop" or text[0] == "run" or text[0] == "write" or text[0] == "study" or text[0] == "play" or text[0] == "please":
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


