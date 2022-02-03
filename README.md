# BingoLolMissions

This repo is a sub repo for the [BingoLol](https://github.com/TrOllOchamO/BingoLol) project.

It contain everything relative to the missions, including missions themselves, generation of random missions list, request and parsing of the [Live Client Data API](https://developer.riotgames.com/docs/lol#game-client-api_live-client-data-api).

Its goal is to facilitate the creation and testing of [new missions](https://github.com/TrOllOchamO/BingoLolMissions/edit/main/MissionsChart.md).

It also include 2 pythons scripts and a csv file.
* The csv file is an index referencing every mission class to the actual name and desciption of the mission.
* The [CreateNewMissionClass.py](https://github.com/TrOllOchamO/BingoLolMissions/blob/main/CreateNewMissionClass.py) script simply create a template for a new mission class.
* Finaly the [UpdateMissions.py](https://github.com/TrOllOchamO/BingoLolMissions/blob/main/UpdateMissions.py) script will update the name and description of every missions according to the one currently given in the csv file. (its avoid to have to modify manually the .cpp file corresponding to the mission you want to rename.)
