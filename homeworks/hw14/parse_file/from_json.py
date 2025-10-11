import json


def get_club_with_most_wins(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        clubs = json.load(f)

    max_wins = max(club['wins'] for club in clubs)
    best_clubs = [club for club in clubs if club['wins'] == max_wins]

    return best_clubs


if __name__ == "__main__":
    best_club = get_club_with_most_wins('clubs.json')
    print(f"The best football clab: {best_club['name']} ({best_club['country']}) - {best_club['wins']} wins.")
