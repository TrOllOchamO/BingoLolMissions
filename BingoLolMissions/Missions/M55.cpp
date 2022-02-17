#include "Missions.h"

using json = nlohmann::json;

#define MISSION_NAME ""
#define MISSION_DESCRIPTION ""

M55::M55() : AbstractMission(MISSION_NAME, MISSION_DESCRIPTION)
{
     m_inRealTime = false;
}


M55::~M55()
{

}


bool M55::mission()
{

}


void M55::resetMission()
{
    AbstractMission::resetMission();
}