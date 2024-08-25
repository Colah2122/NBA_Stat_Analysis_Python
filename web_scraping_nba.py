import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import csv

years = list(range(2023,2024))

team_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}.html"

for year in years:
    url = team_stats_url.format(2024)

    data = requests.get(url)

    with open("team_stats/{}.html".format(year), "w+", encoding="utf-8") as f:
        f.write(data.text)

# year = 2023
dfs = []
for year in years: 
    with open("team_stats/{}.html".format(year), encoding="utf-8") as f:
        page = f.read()

    soup = BeautifulSoup(page, "html.parser")
    #soup.find('tr', class_="thead").decompse()
    team_table = soup.find(id="per_game-team")
    team = pd.read_html(str(team_table))[0]
    # team["Year"] = year
    # team["Team"] = team["Eastern Conference"]
    # del team["Eastern Conference"]
    dfs.append(team)

    # soup = BeautifulSoup(page, "html.parser")
    #soup.find('tr', class_="thead").decompse()
    # team_table = soup.find(id="divs_standings_W")
    # team = pd.read_html(str(team_table))[0]
    # team["Year"] = year
    # team["Team"] = team["Western Conference"]
    # del team["Western Conference"]
    # dfs.append(team)

teams = pd.concat(dfs)
teams.to_csv("team_stats.csv")

# d = pd.read_csv("team_stats.csv")
# x = d['3P']
# y = d['Team']
# plt.plot(x,y, 'x')
# plt.grid()
# plt.yticks(size=8)
# plt.title("NBA Teams Total Made 3 Pointers Per Game")
# plt.xlabel("Total Attempts")
# plt.ylabel("NBA Teams")
# plt.show()

# nba_teams = []
# total_three_pointers = []

# with open('team_stats.csv', 'r') as csvfile:
#     lines = csv.reader(csvfile)
#     for row in csvfile:
#         nba_teams.append(row[2])
#         total_three_pointers.append(row[1])

# plt.scatter(nba_teams, total_three_pointers, color='g', s=100)

# plt.xlabel('NBA Teams Shooting Stats')
# plt.ylabel('Percentage (%)')
# plt.title('NBA Team Shooting Percentage', fontsize = 20)
# plt.show()
