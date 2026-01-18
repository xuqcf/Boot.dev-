def filter_messages(messages):
    filtered = []
    counts = []

    for message in messages:
        words = message.split()
        good_words = []
        dang_words = []

        for word in words:
            if word == "dang":
                dang_words.append(word)
            else:
                good_words.append(word)

        sentence = " ".join(good_words)
        filtered.append(sentence)
        counts.append(len(dang_words))

    return filtered, counts
