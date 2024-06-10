import random


# Linear Congruential Generator parameters
def lcg(seed):
    a = 1103515245
    c = 12345
    m = 2**31
    while True:
        seed = (a * seed + c) % m
        yield seed


# Initialize the generator
seed = random.randint(0, 2**31 - 1)
lcg_gen = lcg(seed)

# Teams
teams = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F", "Team G", "Team H"]

# Leaderboard
leaderboard = {team: 0 for team in teams}

# Simulate matches for 5 weeks
for week in range(5):
    print(f"Week {week + 1}")
    random.shuffle(teams)
    for i in range(0, len(teams), 2):
        team1, team2 = teams[i], teams[i + 1]
        score1 = next(lcg_gen) % 9  # Scores between 0 and 8
        score2 = next(lcg_gen) % 9
        print(f"{team1} vs {team2}: {score1} - {score2}")
        if score1 > score2:
            leaderboard[team1] += 3  # 3 points for a win
        elif score1 < score2:
            leaderboard[team2] += 3
        else:
            leaderboard[team1] += 1  # 1 point for a draw
            leaderboard[team2] += 1

# Print final leaderboard
print("\nFinal Leaderboard:")
sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
for team, points in sorted_leaderboard:
    print(f"{team}: {points} points")
