def choose_parser(file_extension):
    if file_extension.lower() in ("markdown", "md"):
        return "markdown"
    else:
        return "plaintext"
