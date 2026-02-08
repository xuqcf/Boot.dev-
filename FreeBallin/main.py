def create_markdown_image(alt_text):

    def inner(url):

        url = url.replace("(", "%28")
        url = url.replace(")", "%29")
        base = f"![{alt_text}]({url})"

        def inner_most(title=None):
            if title:
                return base[:-1] + f' "{title}" )'
            return base
        return inner_most
    return inner
    
