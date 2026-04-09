from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://cdn.nba.com/static/json"
ALL_JSON = "/liveData/scoreboard/todaysScoreboard_00.json"

printer = PrettyPrinter()


def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links


def get_scoreboard():
    data = get(BASE_URL + ALL_JSON).json()
    games = data['scoreboard']['games']

    for game in games:
        home_team = game['homeTeam']
        away_team = game['awayTeam']

        print("------------------------------------------")
        print(f"{home_team['teamTricode']} vs {away_team['teamTricode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"Status: {game['gameStatusText']}")


def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(
        BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", teams))
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        print(f"{i + 1}. {name} - {nickname} - {ppg}")


get_stats()