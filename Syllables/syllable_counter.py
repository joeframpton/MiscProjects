def openfile():
    with open('cmudict-07b.txt') as fin:
        input = fin.read()
    return input

def word_collector(letter):
    text = openfile().split('\n')
    words_syllables = {}
    for line in text:
        syllables = 0
        word_split = line.split(' ', 1)
        syllables = word_split[1].count('0') + word_split[1].count('1') + word_split[1].count('2')
        if letter in word_split[0]:
            words_syllables[word_split[0]] = syllables
    return words_syllables

def histogram_maker(letter):
    syllable_dict = word_collector(letter)
    syllables_histogram = {}
    for word, syllables in syllable_dict.items():
        if syllables in syllables_histogram:
            syllables_histogram[syllables] += 1
        else:
            syllables_histogram[syllables] = 1
    return syllables_histogram

def histogram_printer(letter):
    syllables_histogram = histogram_maker(letter)
    for i in sorted(syllables_histogram):
        print((i, syllables_histogram[i]))
    total_words = sum(syllables_histogram.values())
    for syllable in syllables_histogram:
        syllables_histogram[syllable] = round((syllables_histogram[syllable]/total_words) * 100, 2)
    for i in sorted(syllables_histogram):
        print((i, syllables_histogram[i]))

histogram_printer('W')