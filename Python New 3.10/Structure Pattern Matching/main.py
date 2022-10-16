def run_command(command: str) -> None:
    match command:
        case "quit":
            print("Quitting the program.")
            quit()
        case "reset":
            print("Restting the system.")
        case other:
            print(f"Unknown Command: {other!r}.")

def main() -> None:

    while True:
        command = input("$ ")
        run_command(command)

if __name__ == "__main__":
    main()