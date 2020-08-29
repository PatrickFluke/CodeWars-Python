#I'm very well aware how much longer this is than it had to be. This was just the first method that came to mind. I'm continually practicing
#to reduce the number of lines of code I require.

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
