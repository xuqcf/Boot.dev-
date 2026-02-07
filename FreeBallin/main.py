def doc_format_checker_and_converter(conversion_function, valid_formats):
    def new(filename, content):
        split = filename.split(".")
        ext = split[-1]


        if ext in valid_formats:
            conversion_function(content) 
        else:
            raise ValueError("Invalid file format")
    
    return new

# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
