def split(text):
    text = text.lower()
    output_text1 = text.split()
    return output_text1


def find(text):

    global txt

    
    verbs_for_imprative = ["برو", "بیا", "بخور", "بنشین", "بایست", "ببند", "بازکن", 
                           "نگاه", "گوش کن", "صبرکن", "ایست", "بنویس", "مطالعه کن", 
                           "بازی کن", "لطفا", "بردار", "بگذار", "بیاور", "ببر",
                           "بکن", "نکن", "لطفا", "بشین", "بزار", "نزار", "بخون",    
                           "نخون", "بیار", "نیار"]
    
    verbs_for_emitional = ["دوست دارم", "دوست داری", "عاشق", "متنفر", "خوشحال", 
                           "غمگین", "عصبانی", "هیجان زده", "میترسم", "ترسیده", 
                           "خسته", "کسل", "کسالت بار", "زیبا", "قشنگ", "عالی", 
                           "وحشتناک", "عاشق", "دوست ", "دوستت"]

    persian_question_words = ["آیا", "چیست", "کیست", "کجاست", "چرا", "چطور", 
                              "چگونه", "کدام", "آیا", "مگر", "چه", "مگه", "کدوم", "چطور"]
    
    persian_pronouns = ["من", "تو", "او", "ما", "شما", "ایشان", "آنها", "این", 
                        "آن", "اینجا", "آنجا", "ان", "اون"]

    assert type(text) == list, "the input must be a list not another type !"

    n = len(text)

    
    if "سلام" in text:

        if "سلام" in txt:

            return "simple(ساده)"

        if "?" in text[n - 1] or "؟" in text[n - 1]:

            if any(word in text for word in persian_question_words):
            
                return "asking(پرسشي)"
            
            elif "میتونی" in text[0]:

                return "imprative(امری)"
            
            elif "چی" in text or "چرا" in text or "چه" in text:

                return "asking(پرسشی)"
            
            elif text[0] in verbs_for_imprative:
                
                return "imprative(امري)"
            
            else:
                return "asking(پرسشي)"
        
        elif "!" in text[n - 1] or "!" in txt:

            for i in verbs_for_emitional:

                if i in text:
                    
                    return "emitional(عاطفی)"
            
            if any(word in text for word in persian_pronouns):
                
                return "declarative(خبري)"

            else:

                return "exclamatory(تعجبي)"
        
                
        else:

            return "simple(ساده)"
    
    
    elif "?" in text[n - 1] or "؟" in text[n - 1]:
        
        if any(word in text for word in persian_question_words):
            
            return "asking(پرسشي)"
        elif "چی" in text or "چرا" in text or "چه" in text:

            return "asking(پرسشی)"
        
        elif text[0] in verbs_for_imprative:
            
            return "imperative(امري)"
        
        else:
            return "asking(پرسشي)"
        
    elif "!" in text[n - 1] or "!" in txt:
        
        for i in verbs_for_emitional:

            if i in text:

                return "emitional(عاطفی)"
        
        if any(word in text for word in persian_pronouns):
            
            return "declarative(خبري)"

        elif text[0] in verbs_for_imprative:

            return "imprative(امری)"
        
        else:
            return "exclamatory(تعجبي)"
    
    
    elif "." in text[n - 1] or "۔" in text[n - 1]:
        
        if any(word in text for word in persian_pronouns):
            
            return "declarative(خبري)"
        
    elif any(word in text for word in persian_question_words):

        return "asking(پرسشی)"
    
    elif any(word in text for word in persian_pronouns):

        return "declarative(خبری)"
    
    else:
        
        return "please add a mark(?, !, .)"


def starting(text):
    global txt
    txt = text
    return find(split(text))
