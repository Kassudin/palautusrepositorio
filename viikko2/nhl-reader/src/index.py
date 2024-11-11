from player import Player
import requests


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN\n")

    finnish_players = [player for player in players if player.nationality == "FIN"]
    sorted_players = sorted(finnish_players, key=lambda p: p.goals + p.assists, reverse=True)

    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()