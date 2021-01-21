from flask import Response, Blueprint, request
from bs4 import BeautifulSoup
import constant
import json
import requests
import re


charts_api = Blueprint("charts", __name__)


@charts_api.route("/", methods=["GET"])
def Charts():
    try:
        type = request.args.get("type")
        if type is None:
            type = "day"
        if type != "day" and type != "week" and type != "month":
            return Response(
                json.dumps({"msg": "Invalid type"}),
                status=415,
                mimetype="application/json",
            )
        res = requests.get(
            constant.MELON_SONG_CHART.format(type),
            headers=constant.MELON_HEADER,
        )
        if res.status_code == 302:
            return Response(status=302)
        soup = BeautifulSoup(res.text, "html.parser")
        song_infos = soup.select("tbody tr")
        result = []
        for info in song_infos:
            song = {}
            rankChange = None

            songId = re.search(
                r"goSongDetail\('(\d+)'\)", info.select_one("a.song_info")["href"]
            )
            albumId = re.search(
                r"goAlbumDetail\('(\d+)'\)", info.select_one("div.rank03 a")["href"]
            )

            if info.select_one("span.rank_wrap span.rank_new") != None:
                rankChange = "New"
            else:
                if info.select_one("span.rank_wrap span.rank_up") != None:
                    rankChange = info.select_one("span.rank_wrap span.up").text
                else:
                    if info.select_one("span.rank_wrap span.rank_static") != None:
                        rankChange = None
                    else:
                        rankChange = (
                            "-" + info.select_one("span.rank_wrap span.down").text
                        )

            song["albumCover"] = info.select_one("a.image_typeAll img")["src"]
            if song["albumCover"].find("/melon") != -1:
                song["albumCover"] = song["albumCover"][
                    : song["albumCover"].find("/melon")
                ]
            song["songId"] = songId.group(1)
            song["rankInfo"] = {
                "rank": info.select_one("span.rank").text.strip(),
                "rankChange": rankChange,
            }
            song["title"] = info.select_one("div.rank01").text.strip()
            song["artist"] = info.select_one("div.rank02 span").text.split(", ")
            song["album"] = info.select_one("div.rank03").text.strip()
            song["albumId"] = albumId.group(1)
            result.append(song)
        return Response(json.dumps(result), status=200, mimetype="application/json")
    except:
        return Response(
            json.dumps({"msg": "Internal error"}),
            status=500,
            mimetype="application/json",
        )
