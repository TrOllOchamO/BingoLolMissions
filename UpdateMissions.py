import os


def remove_non_ascii_chars(non_ascii_str):
    cleaned = non_ascii_str.replace("’", "'")  # replace the weird apostrophe given by the csv with the ascii one
    cleaned = cleaned.replace("\xa0", " ")  # replace the weird space given by the csv with the ascii one
    cleaned = cleaned.replace("\xC2", "")  # replace the extra weird space given by the csv
    return cleaned


missionListDir = os.listdir("BingoLolMissions/Missions")

with open("missionList.csv", "r") as missionsList:  # open the csv

    # create a list of list who contains mission's info
    linesList = missionsList.readlines()  # get the list of every lines
    for i in range(len(linesList)):
        linesList[i] = linesList[i].split("\t")  # split in sublist [ mission number, name, description ]

    # update the info in every files
    for i in range(1, len(linesList)):
        if (linesList[i][0].rstrip() + ".cpp") in missionListDir:  # if the file exist
            lines = []
            changed = False

            # open the file
            with open(f"BingoLolMissions/Missions/{linesList[i][0].rstrip()}.cpp", "r") as fileToModify:
                lines += fileToModify.readlines()
                for j in range(len(lines)):
                    if "#define MISSION_NAME" in lines[j]:  # if the MISSION_NAME line exist
                        newName = linesList[i][1].rstrip()  # get the name from the list
                        newName = remove_non_ascii_chars(newName)
                        lines[j] = f"""#define MISSION_NAME "{newName}"\n"""
                        changed = True
                    if "#define MISSION_DESCRIPTION" in lines[j]:  # if the MISSION_DESCRIPTION line exist
                        newDescription = linesList[i][2].rstrip()
                        newDescription = remove_non_ascii_chars(newDescription)
                        lines[j] = f"""#define MISSION_DESCRIPTION "{newDescription}"\n"""
                        changed = True

            # rewrite the file if we successfully change something
            if changed:
                with open(f"BingoLolMissions/Missions/{linesList[i][0].rstrip()}.cpp", "w") as fileToModify:
                    for line in lines:
                        fileToModify.write(line)
