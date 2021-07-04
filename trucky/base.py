from typing import Union
import urllib3
import json
from .baseExceptions import ConnectionError, NotFoundError, RateLimitError

http = urllib3.PoolManager()


class TruckersMP:
    def __init__(self):
        self._root_url = "https://api.truckyapp.com/v2/"

    def __checkError(self, errorCode) -> Union[bool, Exception]:
        if errorCode in [400, 401, 403, 502, 503, 504]:
            raise ConnectionError()
        elif errorCode == 404:
            raise NotFoundError()
        elif errorCode == 429:
            raise RateLimitError()

    def __decode_data(self, req) -> dict:
        return json.loads(req.data.decode("utf-8"))

    # In Game
    def get_player(self, player_name) -> dict:
        """
        Fetches a player using the player ID given.
        """
        req = http.request("GET", f"{self._root_url}/map/searchPlayer?query=:{player_name}")
        self.__checkError(req.status)

        return self.__decode_data(req)

    

    def get_servers(self) -> dict:
        """
        Fetches server information for the mod.
        """
        req = http.request("GET", f"{self._root_url}/traffic/servers")
        self.__checkError(req.status)

        return self.__decode_data(req)



    def get_tmp_version(self) -> dict:
        """
        Fetches the version that the mod is running on.
        """
        req = http.request("GET", f"{self._root_url}/truckersmp/version")
        self.__checkError(req.status)

        return self.__decode_data(req)

    # Events
    def get_events(self) -> dict:
        """
        Fetches all events happening from the events page.
        """
        req = http.request("GET", f"{self._root_url}/events")
        self.__checkError(req.status)

        return self.__decode_data(req)




        return self.__decode_data(req)
