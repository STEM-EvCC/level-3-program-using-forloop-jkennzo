mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

missionAmount = 0
for missions in mission_names:
    missionAmount += 1
print("Total number of missions:", missionAmount)

succesfulMissions = 0
for success in mission_success:
    if success == True:
        succesfulMissions += 1
print("Number of succesful missions:", succesfulMissions)

successRate = (succesfulMissions/missionAmount)*100
print(f"Success Rate: {successRate:.2f}%")

print("Missions launched before the year 2000: ")
index = 0
for years in mission_years:
    if years < 2000:
        print(" - " + mission_names[index])
    index += 1

    