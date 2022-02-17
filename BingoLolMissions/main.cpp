#include <chrono>
#include <thread>

#include "Missions/ClientData.h"
#include "Missions/Missions.h"

using json = nlohmann::json;

int main()
{
	json gameData;
	ClientData clientData(&gameData);
	M54 mission;
	mission.setGameData(&gameData);
	int TimebetweenTests(10);

	while (true)
	{
		std::this_thread::sleep_for(std::chrono::milliseconds(TimebetweenTests));
		if (clientData.uptadeGamedata())
		{
			mission.runMission();
		}
	}
}
