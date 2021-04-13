def madlib():
    body_part = input("Body Part: ")
    verb = input("Verb: ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun_plural_1 = input("Noun (plural): ")
    noun_plural_2 = input("Noun (plural): ")

    madlib = f"I love boxing because it's {adj1}! The journey to becoming a \
great boxer starts with hope in your mind and a dream in your {body_part}. Through blood, \
sweat, and {noun_plural_1}, hopefully it never ends. Yes, once you learn to {verb}, it becomes \
a part of your life identity and you can become a super {adj2} face-destroyer. Knowledge of the techniques \
lets you take control of your {noun1}. You can become a {noun_plural_2}, \
a literal {adj3} boxer, somebody who can win a lots of tournament and win a {noun2}. You can \
maybe even become the next Muhammad Ali {adj4}."
    
    print(madlib)