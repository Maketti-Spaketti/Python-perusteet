def frameWord(PWord: str) -> None:
    decorator = "*" * (len(PWord) + 4)
    print(decorator)
    print(f"* {PWord} *")
    print(decorator)
    return None


def main() -> None:
    print("Program starting.")
    string = input("Insert word: ")
    print("")
    frameWord(string)
    print("")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
