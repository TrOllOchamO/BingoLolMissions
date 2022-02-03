import os


def getMissionNumber():
    mission_number = ""
    while type(mission_number) != int:
        print("Please enter the number of the new mission class :")
        mission_number = input()
        try:
            mission_number = int(mission_number)
        except:
            print("Incorrect, you should enter a number")
    return mission_number

def createClassHeader(mission_number):
    template = f"""#pragma once

#include "AbstractMission.h"
#include "Missions.h"

class M{mission_number} : public AbstractMission
{{
public:
    M{mission_number}();
    ~M{mission_number}();
    void resetMission();

protected:
    bool mission();
}};"""
    with open(f"./BingoLolMissions/Missions/M{mission_number}.h", 'w') as file:
        file.write(template)


def createClassCpp(mission_number):
    template = f"""#include "Missions.h"

using json = nlohmann::json;

#define MISSION_NAME ""
#define MISSION_DESCRIPTION ""

M{mission_number}::M{mission_number}() : AbstractMission(MISSION_NAME, MISSION_DESCRIPTION)
{{
     m_inRealTime = false;
}}


M{mission_number}::~M{mission_number}()
{{

}}


bool M{mission_number}::mission()
{{

}}


void M{mission_number}::resetMission()
{{
    AbstractMission::resetMission();
}}"""
    with open(f"./BingoLolMissions/Missions/M{mission_number}.cpp", 'w') as file:
        file.write(template)


mission_number = getMissionNumber() #asking the user the number of the mission class
mission_list = os.listdir("./BingoLolMissions/Missions")
if (f"M{mission_number}.h" in mission_list) or (f"M{mission_number}.cpp" in mission_list): #verifying we won't overwrite an existing class
    print(f"A class named M{mission_number} alredy exist.")
    input("Press enter to quit.")
else:
    createClassHeader(mission_number)
    createClassCpp(mission_number)
    print(f"Class M{mission_number} successfully created !")
    print('You can now add the forlder "Missions" to the project.')
    input("Press enter to quit.")
