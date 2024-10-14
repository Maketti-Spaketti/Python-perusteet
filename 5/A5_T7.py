DELIMITER = ","


def analyseWords(WordString: str) -> None:
    WordCount = WordString.count(DELIMITER)+1
    Characters = len(WordString)-WordCount
    # WordList = WordString.split(DELIMITER)
    # WordCount = len(WordList)
    # Characters = len(WordString) - WordCount
    print(f"- {WordCount} Words")
    print(f"- {Characters} Characters")
    print(
        f"-{Characters / WordCount: .2f} Average word length"
    )  # Buginen flake8 versio


def collectWords() -> str:
    return input("Insert word(empty stops): ")


def main() -> None:
    print("Program starting.")
    collectedWords = []
    while word := collectWords():
        collectedWords.append(word)
    analyseWords(DELIMITER.join(collectedWords))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
