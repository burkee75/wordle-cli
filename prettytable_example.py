# this is just an example render of what Pretty Table should look like for wordle-cli.

from string import printable
from prettytable import PrettyTable
from rich import print

wordle_table = PrettyTable()
wordle_table.field_names = ["Letter 1", "Letter 2", "Letter 3", "Letter 4", "Letter 5"]
wordle_table.add_row(["[green]H[/green]", "I", "K", "[yellow]E[/yellow]", "R"])
print(wordle_table)