def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_lenght(doc):
            count = 0
            split = doc.split("\n")
            for lines in split:
                if lines.__contains__(sequence):
                    count += 1
            return count
        return with_lenght

    return with_char
