# VERSION: 1.01
# AUTHORS: ALAA_BRAHIM
# LICENSING INFORMATION

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from helpers import retrieve_url, download_file
from novaprinter import prettyPrinter
import json


class animetosho(object):
    url = "https://animetosho.xyz"
    name = "Anime Tosho"
    supported_categories = {
        "all": "all",
        "anime": "anime",
    }

    def __init__(self):
        pass

    def download_torrent(self, info):
        print(download_file(info))

    def search(self, what, cat='all'):
        url = f"https://feed.animetosho.xyz/json/v1/search?q={what}"
        _link = json.loads(retrieve_url(url))
        link = _link["data"]

        for result in link:
            current_result = {"engine_url": "https://animetosho.xyz/"}
            current_result["link"] = result["magnet"]
            current_result["name"] = result["title"]
            current_result["size"] = str(result["size_bytes"]) + " B"
            current_result["seeds"] = result["seeders"]
            current_result["leech"] = result["leechers"]
            current_result["desc_link"] = "https://animetosho.xyz/view/" + str(result["id"])

            prettyPrinter(current_result)


if __name__ == "__main__":
    a = animetosho()
    a.search("zom+judas")
