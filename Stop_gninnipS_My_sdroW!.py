def spin_words(sentence):
    # Your code goes here
    split_sentence = sentence.split(sep=" ")
    newSentence = ""
    for a in split_sentence:
        print(a)
        if len(a) > 4:
            a = a[::-1]
        if not newSentence == "":
            newSentence = newSentence + " "
        newSentence = newSentence + a
    print(newSentence)
    return newSentence
