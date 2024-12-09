from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    print("All players count (should be 958):")
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("\nPlayers with fewer than 2 goals in NYR:")
    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nPlayers in NYR with not at least 2 goals:")
    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
