from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    print("all players:")
    query = QueryBuilder()
    matcher = query.build()
    for player in stats.matches(matcher):
        print(player)

    print("\nPlayers in NYR:")
    matcher = query.plays_in("NYR").build()
    for player in stats.matches(matcher):
        print(player)

    print("\nPlayers in NYR with 10-19 goals:")
    matcher = (
        query
        .plays_in("NYR")
        .has_at_least(10, "goals")
        .has_fewer_than(20, "goals")
        .build()
    )
    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
