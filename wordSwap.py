import random

def create_swap_dict(words):

    unique_words= set(words)
    word_list = list(unique_words)
    swap_dict = {}

    for word in unique_words:
        swap_dict[word] = random.choice(word_list)

    return swap_dict

def replace_words(words, swap_dict):
    return [swap_dict[word] for word in words]

def main():
    sentence = input("enter a sentence: ")
    words = sentence.split()

    swap_dict = create_swap_dict(words)

    print("\nSwap Dictionary: ")
    print(swap_dict)

    new_sentence_words = replace_words(words, swap_dict)
    new_sentence = ' '.join(new_sentence_words)

    print("\nNew Sentence: ")
    print(new_sentence)

if __name__ == "__main__":
    main()

