#include "Missions.h"

using json = nlohmann::json;

#define MISSION_NAME ""
#define MISSION_DESCRIPTION ""

M56::M56() : AbstractMission(MISSION_NAME, MISSION_DESCRIPTION)
{
     m_inRealTime = false;
}


M56::~M56()
{

}


bool M56::mission()
{

}


void M56::resetMission()
{
    AbstractMission::resetMission();
}