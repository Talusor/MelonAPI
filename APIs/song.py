from flask import Response, Blueprint, request
from bs4 import BeautifulSoup
import constant
import json
import requests
import re


song_api = Blueprint("song", __name__)


@song_api.route("/info", methods=["GET"])
def Info():
    try:
        songId = request.args.get("id")

        res = requests.get(
            constant.MELON_INFO_SONG.format(songId),
            headers=constant.MELON_HEADER,
        )
        soup = BeautifulSoup(res.text, "html.parser")
        if soup.select_one("#targetId") is not None:
            return Response(
                json.dumps({"msg": "Not Found"}),
                status=404,
                mimetype="application/json",
            )

        song = {}
        info_section = soup.select_one("div.wrap_info")
        song["albumCover"] = info_section.select_one("div.thumb a img")["src"]
        if song["albumCover"].find("/melon") != -1:
            song["albumCover"] = song["albumCover"][: song["albumCover"].find("/melon")]
        entry = info_section.select_one("div.entry")
        song["title"] = entry.select_one("div.info div.song_name").contents[-1].strip()
        song["artist"] = entry.select_one("div.info div.artist").text.strip()
        meta_data = entry.select("div.meta dd")
        song["album"] = meta_data[0].text.strip()
        albumId = re.search(
            r"goAlbumDetail\('(\d+)'\)", meta_data[0].select_one("a")["href"]
        )
        song["albumId"] = albumId.group(1)
        song["publishDate"] = meta_data[1].text.strip()
        song["genre"] = meta_data[2].text.strip().split(", ")
        lyric = soup.select_one("div.lyric")
        song["lyric"] = None
        if lyric is not None:
            song["lyric"] = re.sub(
                r"<br\s*?/>",
                "\n",
                lyric.decode_contents(formatter="html"),
            )

            song["lyric"] = re.sub(
                r"<!--.*-->",
                "",
                song["lyric"],
            )

            song["lyric"] = song["lyric"].strip()

        return Response(
            json.dumps(song),
            status=200,
            mimetype="application/json",
        )
    except:
        return Response(
            json.dumps({"msg": "Internal error"}),
            status=500,
            mimetype="application/json",
        )


@song_api.route("/search", methods=["GET"])
def Search():
    try:
        query = request.args.get("query")
        if query == "":
            return Response(
                json.dumps({"msg": "query is emtpy"}),
                status=400,
                mimetype="application/json",
            )
        res = requests.get(
            constant.MELON_SEARCH_SONG.format(query),
            headers=constant.MELON_HEADER,
        )
        soup = BeautifulSoup(res.text, "html.parser")
        result = []
        for item in soup.select("tbody tr"):
            temp = {}
            reItem = re.search(
                r"'SONG','SO','(.*)','(\d+)'\)",
                item.select_one("button.play")["onclick"],
                re.MULTILINE,
            )
            temp["songId"] = reItem.group(2)
            if not item.select_one("a.fc_gray"):
                temp["title"] = (
                    item.select_one("td.t_left").select_one("span:not(.odd_span)").text
                )
            else:
                temp["title"] = item.select_one("a.fc_gray").text
            temp["artist"] = item.select_one("div#artistName>span").text
            if item.select_one("div#artistName a") != None:
                reItem = re.search(
                    r"goArtistDetail\('(\d+)'\)",
                    item.select_one("div#artistName a")["href"],
                    re.MULTILINE,
                )
                temp["artistId"] = reItem.group(1)
            else:
                temp["artistId"] = None
            temp["album"] = item.select("td")[4].select_one("a.fc_mgray").text
            reItem = re.search(
                r"goAlbumDetail\('(\d+)'\)",
                item.select("td")[4].select_one("a.fc_mgray")["href"],
                re.MULTILINE,
            )
            temp["albumId"] = reItem.group(1)
            result.append(temp)

        return Response(
            json.dumps({"count": len(result), "result": result}),
            status=200,
            mimetype="application/json",
        )
    except:
        return Response(
            json.dumps({"msg": "Internal error"}),
            status=500,
            mimetype="application/json",
        )
