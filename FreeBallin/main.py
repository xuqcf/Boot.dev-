def find_longest_word(document, longest_word=""):
    if not document or not document.strip():
        return longest_word

    parts = document.split(maxsplit=1)
    first_word = parts[0]

    if len(parts) > 1:
        rest = parts[1]
    else:
        rest = ""

    if len(first_word) > len(longest_word):
        longest_word = first_word

    if rest:
        return find_longest_word(rest, longest_word)
    else:
        return longest_word
