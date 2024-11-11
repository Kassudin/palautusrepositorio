from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

def main():
    console = Console()

    console.print("NHL statistics by nationality")
    console.print("")

    season = Prompt.ask("Enter the season", choices=["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"])
    console.print("")
    while True:
        nationality = Prompt.ask("Enter the nationality", choices=["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"])

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")

        table.add_column("name", style="cyan", no_wrap=True)
        table.add_column("neam", style="magenta")
        table.add_column("noals", style="green", justify="right")
        table.add_column("assists", style="green", justify="right")
        table.add_column("points", style="green", justify="right")

        for player in players:
            points = player.goals + player.assists
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(points))

        console.print(table)

if __name__ == "__main__":
    main()
