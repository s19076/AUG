def reverse_sentence(sentence: str) -> str:
    """
    """
    reversed_sentence = ""
    for i in range(len(sentence)):
        reversed_sentence += sentence[len(sentence) - 1 - i]

    return reversed_sentence
