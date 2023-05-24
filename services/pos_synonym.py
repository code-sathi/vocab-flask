import nltk
from nltk.corpus import wordnet
from helper.helper import remove_duplicate_from_list, get_top_n_from_list

POS_MAP = {
    'CC': 'n',   # coordinating conjunction
    'CD': 'n',   # cardinal number
    'DT': 'n',   # determiner
    'EX': 'n',   # existential there
    'FW': 'n',   # foreign word
    'IN': 'n',   # preposition or subordinating conjunction
    'JJ': 'a',   # adjective
    'JJR': 'a',  # adjective, comparative
    'JJS': 'a',  # adjective, superlative
    'LS': 'n',   # list item marker
    'MD': 'v',   # modal
    'NN': 'n',   # noun, singular or mass
    'NNS': 'n',  # noun, plural
    'NNP': 'n',  # proper noun, singular
    'NNPS': 'n',  # proper noun, plural
    'PDT': 'n',  # predeterminer
    'POS': 'n',  # possessive ending
    'PRP': 'n',  # personal pronoun
    'PRP$': 'n',  # possessive pronoun
    'RB': 'r',   # adverb
    'RBR': 'r',  # adverb, comparative
    'RBS': 'r',  # adverb, superlative
    'RP': 'n',   # particle
    'SYM': 'n',  # symbol
    'TO': 'n',   # to
    'UH': 'n',   # interjection
    'VB': 'v',   # verb, base form
    'VBD': 'v',  # verb, past tense
    'VBG': 'v',  # verb, gerund or present participle
    'VBN': 'v',  # verb, past participle
    'VBP': 'v',  # verb, non-3rd person singular present
    'VBZ': 'v',  # verb, 3rd person singular present
    'WDT': 'n',  # wh-determiner
    'WP': 'n',   # wh-pronoun
    'WP$': 'n',  # possessive wh-pronoun
    'WRB': 'r',  # wh-adverb
}


# def is_plural(synset):
#     hypernyms = synset.hypernyms()
#     for hypernym in hypernyms:
#         if hypernym.name() == 'entity.n.01':
#             # Singular form
#             return False
#         elif hypernym.name() == 'physical_entity.n.01':
#             # Plural form
#             return True
#     return False


def get_synonym_for_word_in_sentence(sentence, index):
    # Tokenize the sentence into individual words
    words_list = nltk.word_tokenize(sentence)

    word = words_list[index]

    # Use part-of-speech tagging to identify the parts of speech for each word
    pos_tags = nltk.pos_tag(words_list)

    syn_list = []

    # Iterate over each word in the sentence and check if it can be replaced with any of the words in the list
    if pos_tags[index][0] == word and POS_MAP[pos_tags[index][1]]:
        word_synsets = wordnet.synsets(
            pos_tags[index][0], POS_MAP[pos_tags[index][1]])
        for syn in word_synsets:
            for lemma in syn.lemmas():
                syn_list.append((lemma.name(), syn))
    print(syn_list)
    if len(syn_list) > 1:
        syn_list = remove_duplicate_from_list(syn_list, word)
        syn_list = get_top_n_from_list(syn_list, 3)
    return syn_list


def check_adverb(sentence, index):
    # Tokenize the sentence into individual words
    words_list = nltk.word_tokenize(sentence)

    # Use part-of-speech tagging to identify the parts of speech for each word
    pos_tags = nltk.pos_tag(words_list)

    if pos_tags[index][1] in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
        if index > 0 and pos_tags[index-1][1].startswith('RB'):
            words_list[index-1:index+1] = [pos_tags[index][0]]
        else:
            words_list[index] = pos_tags[index][0]

    # Iterate over each word in the sentence and check if it can be replaced with any of the words in the list
    for i in range(len(pos_tags)):
        if pos_tags[i][1] in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            # If the current word is an adjective, adverb or verb, check if it can be replaced
            word_synsets = wordnet.synsets(pos_tags[i][0])
            for word in words:
                for synset in word_synsets:
                    if word in synset.lemma_names():
                        if i > 0 and pos_tags[i-1][1].startswith('RB'):
                            # If the word before the adjective is an adverb, replace both the adverb and the adjective
                            words_list[i-1:i+1] = [word]
                            i -= 1
                        else:
                            words_list[i] = word
                    break
        i += 1
    # Join the list of words back into a sentence
    new_sentence = ' '.join(words_list)

    return new_sentence
