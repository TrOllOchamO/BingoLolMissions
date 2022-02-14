#include "Missions.h"

using json = nlohmann::json;

#define MISSION_NAME ""
#define MISSION_DESCRIPTION ""

M54::M54() : AbstractMission(MISSION_NAME, MISSION_DESCRIPTION)
{
     m_inRealTime = false;
}


M54::~M54()
{

}


bool M54::mission()
{

}


void M54::resetMission()
{
    AbstractMission::resetMission();
}