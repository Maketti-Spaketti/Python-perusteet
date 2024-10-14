optionsMenu: dict[str, str] = {
    "1": "Insert word",
    "2": "Show current word",
    "3": "Show current word in reverse",
    "0": "Exit",
}


def printOptions() -> None:
    print("Options:")
    for opt in optionsMenu:
        print(opt, "-", optionsMenu[opt])
    return None


def main() -> None:
    Word: str = ""
    print("Program starting.")
    while True:
        printOptions()
        match (input("Your choice: ")):
            case "1":
                Word = input("Insert word: ")
                print("")
            case "2":
                print(f'Current word - "{Word}"\n')
            case "3":
                print(f'Word reversed - "{Word[::-1]}"\n')
            case "0":
                print("Exiting program.\n")
                break
            case _:
                print("Unknown option! try again.\n")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
