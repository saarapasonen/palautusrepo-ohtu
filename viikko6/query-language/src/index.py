from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)


    print("at least 45 goals or 70 assists")
    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
)
    for player in stats.matches(matcher):
        print(player)


    print("at least 70 points and playing in NYR, FLA or BOS")
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
    )
)
    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
