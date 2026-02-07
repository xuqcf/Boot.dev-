def word_count_aggregator():
    count = 0
    def calculate(doc):

        nonlocal count
        words = doc.split()
        count += len(words)

        return count


    return calculate

