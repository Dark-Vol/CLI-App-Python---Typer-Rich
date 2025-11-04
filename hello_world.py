# hello_world.py
import typer


def main(name: str):
    """
    Говорит "Привет" пользователю.
    """
    print(f"Привет, {name}!")


if __name__ == "__main__":
    typer.run(main)
