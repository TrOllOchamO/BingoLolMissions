#include "Missions.h"

using json = nlohmann::json;

#define MISSION_NAME "FFÂ ?"
#define MISSION_DESCRIPTION "There is a difference of 10 kills between the 2 teams."

M54::M54() : AbstractMission(MISSION_NAME, MISSION_DESCRIPTION)
{
     m_inRealTime = true;
}


M54::~M54()
{

}


bool M54::mission()
{
	int team1(0);
	int team2(0);

	for (auto it : m_gameData->operator[]("allPlayers"))
	{
		if (it["team"] == "ORDER")
		{
			team1 += it["scores"]["kills"];
		}
		else
		{
			team2 += it["scores"]["kills"];
		}
	}

	if (std::abs(team1 - team2) >= 10)
	{
		m_isMissionDone = true;
		return true;
	}

	return false;
}


void M54::resetMission()
{
    AbstractMission::resetMission();
}