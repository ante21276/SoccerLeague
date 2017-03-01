import csv

TEAMS = ["Sharks", "Raptors", "Dragons"]

date_time_of_practice = {"Dragons": "31. January, 2017 at 12:00",
                         "Sharks": "31. January, 2017 at 14:00",
                         "Raptors": "31. January, 2017 at 16:00"}


def get_players():
    with open("teams.csv") as csvfile:
        file = csv.DictReader(csvfile)
        players = list(file)
    return players

def gen_team(name):

    return {'name': name, 'players': []}

def gen_team_roster(team):

    filename = team['name'].lower() + "_roster.txt"
    with open(filename, 'w') as file:

        file.write("\n\n\t\t\tSoccer League -- Team {} Roster\n\n"
                   "".format(team['name']))

        file.write("\tPlayers:\n")
        for player in team['players']:
            file.write("\t\tName: {}\n".format(player['Name']))
            file.write("\t\t\tExperienced: {}, Guardian(s): {}\n"
                       "".format(player['Soccer Experience'],
                                 player['Guardian Name(s)']))

def partition_players(players, league):
    while players:
        for team in league:
            team["players"].append(players.pop(0))


def generate_average(team):
    total = 0
    for player in team["players"]:
        total += int(player["Height (inches)"])
    return total / len(team["players"])

def generate_letter(team):
    for player in team["players"]:
        player_name = player["Name"].split()

        filename = "player_" + "_".join(player_name).lower() + ".txt"

        with open(filename, "w") as file:
            file.write("\n\n\t\t\t\tSoccer League -- Team {}\n\n".format(team["name"]))
            file.write("Dear {},\n\n".format(player["Guardian Name(s)"]))
            file.write("We would like to welcome you and {} to the Soccer League.\n".format(player["Name"]))
            file.write("This year, {} will be playing on Team {}.\n".format(player_name[0],team["name"]))
            file.write("The first practice will be on {} at Poljud.".format(date_time_of_practice[team["name"]]))
            file.write("\n\nWe look forward to another great year!\n\nRegards, {}.".format(team["name"]))


def main():

    league = []

    for name in TEAMS:
        league.append(gen_team(name))

    players = get_players()

    experience_players = []
    no_experience_players = []

    for player in players:
        if player["Soccer Experience"] == "YES":
            experience_players.append(player)
        else:
            no_experience_players.append(player)


    partition_players(players, league)

    for team in league:
        gen_team_roster(team)
        generate_letter(team)


if __name__ == "__main__":
    main()

