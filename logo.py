#!/usr/bin/env python
#  _.─────────._
# ╱/___________\╲
# \             /
#  \_ o8o88o __/
#  ╱o888888888o╲
# ·──────┰(.'.)─·
# ║  `.    \ /  ║
# ║   )\___|^|  ║
# `══(________)═´
#   (__________)   dew & hon
from rich import print
from rich.markup import render
from rich.console import Group


__all__ = ["art"]


markups = [
    r" [bold white]_.[/bold white][bright_black]─────────[/bright_black][bold white]._[/bold white] ",
    r"[white]╱[bold]/[/white][bright_black]___________[/bright_black][white]\\[/bold]╲[/white]",
    r"[bold bright_black]\\[/bold bright_black]             [bold bright_black]/[/bold bright_black]",
    r" [bold bright_black]\_[/bold bright_black] [bright_yellow]o8o88o[/bright_yellow] [bold bright_black]__/[/bold bright_black] ",
    r" [bright_black]╱[/bright_black][bright_yellow]o888888888o[/bright_yellow][bright_black]╲[/bright_black] ",
    r"[bright_black][bold]·[/bold]──────┰[/bright_black][bold][green]([/green][black].[/black][green]'[/green][black].[/black][green])[/green][bright_black]─[bold]·[/bold][/bright_black]",
    r"[white]║[/white]  [bold green]`.[/bold green]    [bold green]\ /[/bold green]  [white]║[/white]",
    r"[white]║[/white]   [bold][green])\___|[/green][red]^[/red][green]|[/green][/bold]  [white]║[/white]",
    r"[white][bold]`[/bold]══[/white][bold green](________)[/bold green][white]═[bold]´[/bold][/white]",
    r"  [bold green](__________)[/bold green]   [link=https://twitter.com/DanWesely]dew[/link] & [link=https://twitter.com/whostolehonno]hon[/link]",

]
texts = [render(line) for line in markups]
art = Group(*texts)


if __name__ == "__main__":
    print(art)
