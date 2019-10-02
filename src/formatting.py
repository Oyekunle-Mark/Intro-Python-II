formatting = {
    "blue": '\033[94m',
    "green": '\033[92m',
    "red": '\033[91m',
    "yellow": '\033[93m',
    "bold": '\033[1m',
    "underline": '\033[4m',
    "end": '\033[0m'
}


def headline(text):
    print("\n\n" + formatting["blue"] + formatting["bold"] +
          formatting["underline"] + text + formatting["end"] + "\n")


def details(text):
    print(formatting["green"] +
          formatting["bold"] + text + formatting["end"])


def message(text):
    print(formatting["yellow"] + text + formatting["end"])


def error(text):
    print("\n" + formatting["red"] + text + formatting["end"] + "\n")
