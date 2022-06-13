def reverse_sentence(sentence: str) -> str:
    """
    """
    reversed_sentence = ""
    for i in range(len(sentence)):
        reversed_sentence += sentence[len(sentence) - 1 - i]

    return reversed_sentence


def get_max_pref_suff(sentence: str) -> str:
    """
    """
    max_pref_suff = ""
    if len(sentence) == 1:
        return sentence
    else:
        for i in range(len(sentence)):
            if sentence[i] == sentence[-1 - i]:
                max_pref_suff += sentence[i]
            else:
                break
    return max_pref_suff


if __name__ == "__main__":
    print(get_max_pref_suff("abaa"))
