"""
Примеры использования Rich для красивого вывода в терминале.
"""

from rich import print
from rich.table import Table
from rich.progress import track
import time


def example_colors_and_styles():
    """Демонстрация цветов и стилей."""
    print("Это обычный текст.")
    print("[bold green]Это жирный зеленый текст![/bold green]")
    print("[italic yellow]А это желтый курсив.[/italic yellow]")
    print("[underline cyan]Можно даже так.[/underline cyan]")
    print("[bold red on white]Красный на белом фоне![/bold red on white]")


def example_table():
    """Демонстрация создания таблиц."""
    # Создаем объект таблицы
    table = Table(title="Список моих любимых фреймворков")
    
    # Добавляем колонки
    table.add_column("Название", justify="left", style="cyan", no_wrap=True)
    table.add_column("Язык", style="magenta")
    table.add_column("Для чего", justify="right", style="green")
    
    # Наполняем данными
    table.add_row("FastAPI", "Python", "Веб-API")
    table.add_row("React", "JavaScript", "Фронтенд")
    table.add_row("Typer", "Python", "CLI-приложения")
    
    # Выводим таблицу в консоль
    print(table)


def example_progress_bar():
    """Демонстрация прогресс-бара."""
    print("[bold blue]Обработка данных с прогресс-баром:[/bold blue]")
    for step in track(range(10), description="Обработка данных..."):
        # Симулируем какую-то работу
        time.sleep(0.5)
    
    print("[bold green]Готово![/bold green]")


if __name__ == "__main__":
    print("[bold cyan]=== Примеры использования Rich ===[/bold cyan]\n")
    
    print("[bold yellow]1. Цвета и стили:[/bold yellow]")
    example_colors_and_styles()
    print()
    
    print("[bold yellow]2. Таблицы:[/bold yellow]")
    example_table()
    print()
    
    print("[bold yellow]3. Прогресс-бар:[/bold yellow]")
    example_progress_bar()
