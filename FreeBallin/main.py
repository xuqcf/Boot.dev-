def file_to_prompt(file, to_string):
    convert = to_string(file)
    return f"```\n{convert}\n```"