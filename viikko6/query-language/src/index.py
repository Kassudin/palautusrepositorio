from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFeverThan, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
    Not(HasAtLeast(2, "goals")),
    PlaysIn("NYR")
)



    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
