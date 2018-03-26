# Import necessary libraries
import fortniteapi
import sys

# Parse the arg
def parse_args():
    return sys.argv[1], sys.argv[2]

# Check to see if arguments were supplied
if len(sys.argv) == 3:
    user, platform = parse_args()
elif len(sys.argv) > 1 and len(sys.argv) != 3:
    print("\nUsage:")
    print("python fortnite_stats.py <fortnite username> <platform>\n")
    sys.exit()
# If they werent use input() to get them
else:
    user = input("Enter fortnite username: ")
    platform = input("Enter platform (pc, xbox, ps4): ")

api_key = "<YOUR API KEY HERE>" # From fortnite tracker api
tracker = fortniteapi.tracker(api_key, user=user, platform=platform)
tracker.get_stats()

print("\n{platform} - {user}:\n".format(platform=tracker.FULL_PLATFORM, user=tracker.EPIC_USER))
print("Solo:")
print("Wins - {}".format(tracker.ALL_SOLO_WINS))
print("Top 10 - {}".format(tracker.ALL_SOLO_TOP10))
print("Top 25 - {}".format(tracker.ALL_SOLO_TOP25))
print("Kills - {}".format(tracker.ALL_SOLO_KILLS))
print("K/D - {}".format(tracker.ALL_SOLO_KD))
print("Kills per Match - {}".format(tracker.ALL_SOLO_KPG))
print("Win Chance - {}".format(tracker.ALL_SOLO_WIN_CHANCE))

print("\nDuo:")
print("Wins - {}".format(tracker.ALL_DUO_WINS))
print("Top 5 - {}".format(tracker.ALL_DUO_TOP5))
print("Top 12 - {}".format(tracker.ALL_DUO_TOP12))
print("Kills - {}".format(tracker.ALL_DUO_KILLS))
print("K/D - {}".format(tracker.ALL_DUO_KD))
print("Kills per Match - {}".format(tracker.ALL_DUO_KPG))
print("Win Chance - {}".format(tracker.ALL_DUO_WIN_CHANCE))

print("\nSquad:")
print("Wins - {}".format(tracker.ALL_SQUAD_WINS))
print("Top 3 - {}".format(tracker.ALL_SQUAD_TOP3))
print("Top 6 - {}".format(tracker.ALL_SQUAD_TOP6))
print("Kills - {}".format(tracker.ALL_SQUAD_KILLS))
print("K/D - {}".format(tracker.ALL_SQUAD_KD))
print("Kills per Match - {}".format(tracker.ALL_SQUAD_KPG))
print("Win Chance - {}".format(tracker.ALL_SQUAD_WIN_CHANCE))
print("\nTotal time played - {}".format(tracker.TOTAL_TIME_PLAYED))

input("\nPress any key to continue...") # Wait till the user presses a key before exiting
