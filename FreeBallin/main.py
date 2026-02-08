def args_logger(*args, **kwargs):
    for i, arg in enumerate(args, start=1):
        print(f"{i}. {arg}")

    k_tuple = kwargs.items()
    k_sorted = sorted(k_tuple)

    for key, value in k_sorted:
        print(f"* {key}: {value}")

    return args_logger