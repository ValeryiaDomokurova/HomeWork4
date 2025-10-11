import json


def get_club_with_most_wins(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        clubs = json.load(f)

    max_wins = max(club['wins'] for club in clubs)
    best_clubs = [club for club in clubs if club['wins'] == max_wins]

    return best_clubs
