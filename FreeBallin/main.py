def new_collection(initial_docs):
    copy = initial_docs.copy()

    def add_doc(doc):

        nonlocal copy
        copy.append(doc)
        return copy

    return add_doc