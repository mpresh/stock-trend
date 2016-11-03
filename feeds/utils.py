import re


def remove_white_space(input):
    sentence = re.sub(r"\s+", "", input, flags=re.UNICODE)
    return sentence


def cleanup_int(input):
    input = input.replace(",", "")
    return input
