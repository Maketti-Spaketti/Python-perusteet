def askDimension(PPrompt: str) -> float:
    Feed = float(input(f"Insert {PPrompt}: "))
    return Feed


def calcRectangleArea(Width: float, Height: float) -> float:
    return Width * Height


def main() -> None:
    print("Program starting.")
    Width = askDimension("width")
    Height = askDimension("height")
    Area = calcRectangleArea(Width, Height)
    print(f"\nArea is{Area: .1f}²")  # Buginen flake8 versio
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
