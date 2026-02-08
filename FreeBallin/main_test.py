from main import *


def remove_spaces(text):
    return text.replace(" ", "")


def to_upper(text):
    return text.upper()


run_cases = [
    (
        "hello world",
        "--one",
        "helloworld",
    ),
    (
        "hello world",
        "--two",
        "HELLO WORLD",
    ),
    (
        "hello world",
        "--both",
        "HELLOWORLD",
    ),
]

submit_cases = run_cases + [
    (
        "boot dev",
        None,
        "BOOTDEV",
    ),
]


def test(input_text, option, expected_output):
    print("---------------------------------")
    print("Input:", input_text)
    print("Option:", option)
    print("Expected:", expected_output)

    pipeline = create_pipeline(remove_spaces)(to_upper)
    result = pipeline(option)(input_text)

    print("Actual:  ", result)
    if result == expected_output:
        print("Pass")
        return True

    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
