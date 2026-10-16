def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    text = input("What do you want to say? ")
    print(convert(text))


main()