# 1 Vitsi vastaus per viikko pitää mielen virkeänä
from enum import StrEnum
from typing import Callable


def insertWord(prompt="Insert word: ") -> str:
    word = input(prompt)
    print("")
    return word


def printWord(Word: str) -> None:
    print(f'Current word - "{Word}"\n')
    return None


def reverseWord(Word: str) -> None:
    print(f'Word reversed - "{Word[::-1]}"\n')
    return None


def exitProgram() -> None:
    print("Exiting program.\n")
    return None


class Options(StrEnum):
    INSERT = "1"
    PRINT = "2"
    REVERSE = "3"
    EXIT = "0"


optionsMenu: dict[Options, str] = {
    Options.INSERT: "Insert word",
    Options.PRINT: "Show current word",
    Options.REVERSE: "Show current word in reverse",
    Options.EXIT: "Exit",
}

optionsFunctions: dict[Options, Callable] = {
    Options.INSERT: insertWord,
    Options.PRINT: printWord,
    Options.REVERSE: reverseWord,
    Options.EXIT: exitProgram,
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
        match (opt := input("Your choice: ")):
            case Options.INSERT:
                Word = optionsFunctions[opt]()
            case Options.PRINT:
                optionsFunctions[opt](Word)
            case Options.REVERSE:
                optionsFunctions[opt](Word)
            case Options.EXIT:
                optionsFunctions[opt]()
                break
            case _:
                print("Unknown option! try again.\n")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
# En keksi miten saisin vielä enemmän koodia järkevästi
