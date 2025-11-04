# site_checker.py
import typer
import requests
from typing import List
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()


def get_status_emoji(status_code: int) -> str:
    """Возвращает эмодзи в зависимости от статус-кода."""
    if 200 <= status_code < 300:
        return "✅ OK"
    elif 300 <= status_code < 400:
        return "➡️ REDIRECT"
    elif 400 <= status_code < 500:
        return "❌ CLIENT ERROR"
    elif 500 <= status_code < 600:
        return "🔥 SERVER ERROR"
    return "❓ UNKNOWN"


def main(urls: List[str] = typer.Argument(..., help="Список URL для проверки.")):
    """
    Проверяет доступность сайтов и выводит результат в виде таблицы.
    """
    table = Table(title="Результаты проверки сайтов")
    table.add_column("URL", style="cyan", no_wrap=True)
    table.add_column("Статус код", justify="center")
    table.add_column("Статус", justify="left", style="green")

    for url in track(urls, description="Проверка сайтов..."):
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
            status_text = get_status_emoji(status_code)
            
            # Раскрашиваем строку в зависимости от статуса
            row_style = ""
            if 300 <= status_code < 400:
                row_style = "yellow"
            elif status_code >= 400:
                row_style = "red"
            
            table.add_row(url, str(status_code), status_text, style=row_style)

        except requests.exceptions.RequestException as e:
            table.add_row(url, "N/A", f"💥 ERROR: {e.__class__.__name__}", style="bold red")

    console.print(table)


if __name__ == "__main__":
    typer.run(main)