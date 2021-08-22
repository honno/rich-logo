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
from math import pi, sin
from random import randint
from time import sleep

from rich.align import Align
from rich.color import Color, blend_rgb
from rich.console import Group, RenderableType
from rich.live import Live
from rich.markup import render
from rich.padding import Padding
from rich.style import Style

__all__ = ["logo"]


logo = Group(
    render(r" [bold white]_.[/bold white][bright_black]─────────[/bright_black][bold white]._[/bold white] "),
    render(r"[white]╱[bold]/[/white][bright_black]___________[/bright_black][white]\\[/bold]╲[/white]"),
    render(r"[bold bright_black]\\[/bold bright_black]             [bold bright_black]/[/bold bright_black]"),
    render(r" [bold bright_black]\_[/bold bright_black] [bright_yellow]o8o88o[/bright_yellow] [bold bright_black]__/[/bold bright_black] "),
    render(r" [bright_black]╱[/bright_black][bright_yellow]o888888888o[/bright_yellow][bright_black]╲[/bright_black] "),
    render(r"[bright_black][bold]·[/bold]──────┰[/bright_black][bold][green]([/green][black].[/black][green]'[/green][black].[/black][green])[/green][bright_black]─[bold]·[/bold][/bright_black]"),
    render(r"[white]║[/white]  [bold green]`.[/bold green]    [bold green]\ /[/bold green]  [white]║[/white]"),
    render(r"[white]║[/white]   [bold][green])\___|[/green][red]^[/red][green]|[/green][/bold]  [white]║[/white]"),
    render(r"[white][bold]`[/bold]══[/white][bold green](________)[/bold green][white]═[bold]´[/bold][/white]"),
    render(r"  [bold green](__________)[/bold green]  "),
)

if __name__ == "__main__":
    g_positions = []
    for y, text in enumerate(logo.renderables):
        for x, char in enumerate(str(text)):
            if char in ["o", "8"]:
                g_positions.append((y, x))
    g_y = min(y for y, _ in g_positions)
    g_x = min(x for _, x in g_positions)
    g_h = max(y for y, _ in g_positions) - g_y + 1
    g_w = max(x for _, x in g_positions) - g_x + 1
    g_dim = Color.parse("yellow").get_truecolor()
    g_bright = Color.parse("bright_yellow").get_truecolor()

    framerate = 8
    nframes = 4 * framerate

    def draw(frame: int) -> RenderableType:
        brightest_y = 0.25 + sin(2 * (frame / nframes) * 2 * pi) * 1 / 2
        brightest_x = 0.25 + sin((frame / nframes) * 2 * pi) * 1 / 2
        for y, x in g_positions:
            rel_y = (y - g_y) / g_h
            rel_x = (x - g_x) / g_w
            intensity = 1 - abs(brightest_x - rel_x)
            intensity *= 1 - abs(brightest_y - rel_y) / 4
            color = blend_rgb(g_dim, g_bright, intensity)
            style = Style(color=Color.from_triplet(color))
            logo.renderables[y].stylize(style, x, x+1)

        return Align(Padding(logo, (2, 0)), align="center")

    try:
        frame = randint(0, nframes - 1)
        with Live(draw(frame), auto_refresh=False) as live:
            frame = (frame + 1) % nframes
            for _ in range(1000):
                sleep(1 / framerate)
                live.update(draw(frame))
                live.refresh()
                frame = (frame + 1) % nframes
    except KeyboardInterrupt:
        pass
