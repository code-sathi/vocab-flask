import nltk

nltk.download('averaged_perceptron_tagger')


from nltk.corpus import wordnet

def replace_with_hyponym(sentence):
    # Tokenize the sentence and tag each token with its part of speech
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)

    # Loop through each tagged token and replace nouns with one of their hyponyms
    for i in range(len(pos_tags)):
        word, pos = pos_tags[i]
        if pos.startswith('NN'): # Check if the word is a noun
            synsets = wordnet.synsets(word, pos='n')
            if synsets: # Check if the word has any synsets
                hyponyms = synsets[0].hyponyms()
                if hyponyms: # Check if the word has any hyponyms
                    # Replace the word with one of its hyponyms
                    new_word = hyponyms[0].lemmas()[0].name()
                    tokens[i] = new_word

    # Join the tokens back into a sentence
    new_sentence = ' '.join(tokens)
    return new_sentence[:-2] + '.'
