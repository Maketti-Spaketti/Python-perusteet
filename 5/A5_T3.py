def askName() -> str:
    return input("Insert name: ")


def greetUser(PName: str) -> None:
    print(f"Hello {PName}!")
    return None


def main() -> None:
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
