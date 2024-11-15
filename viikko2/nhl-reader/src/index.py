from playerreader import PlayerReader
from playerstats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    console = Console()

    season = input("Syötä kausi (2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/): ")
    nationality = input("Syötä kansalaisuus (FIN/AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/GBR/): ").upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.get_players_by_season_and_nationality(season, nationality)

    table = Table(title=f"{nationality} pelaajat kaudella {season}")
    
    table.add_column("Nimi", style="cyan")
    table.add_column("Joukkue", style="magenta")
    table.add_column("Maalit", justify="right", style="green")
    table.add_column("Syötöt", justify="right", style="yellow")
    table.add_column("Kokonaispisteet", justify="right", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.summa))

    console.print(table)

if __name__ == "__main__":
    main()
