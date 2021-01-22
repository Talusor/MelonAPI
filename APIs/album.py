from flask import Response, Blueprint, request
from bs4 import BeautifulSoup
import constant
import json
import requests
import re


album_api = Blueprint("album", __name__)


@album_api.route("/info", methods=["GET"])
def Info():
    try:
        albumId = request.args.get("id")
        res = requests.get(
            constant.MELON_INFO_ALBUM.format(albumId),
            headers=constant.MELON_HEADER,
        )
        soup = BeautifulSoup(res.text, "html.parser")
        if soup.select_one("#targetId") is not None:
            return Response(
                json.dumps({"msg": "Not Found"}),
                status=404,
                mimetype="application/json",
            )

        album = {}
        info_section = soup.select_one("div.wrap_info")
        album["albumCover"] = info_section.select_one("div.thumb a img")["src"]
        if album["albumCover"].find("/melon") != -1:
            album["albumCover"] = album["albumCover"][
                : album["albumCover"].find("/melon")
            ]
        entry = info_section.select_one("div.entry")
        album["kind"] = entry.select_one("div.info span.gubun").text.strip()
        album["title"] = entry.select_one("div.info div.song_name").contents[-1].strip()
        album["artist"] = entry.select_one("div.info div.artist").text.strip()
        meta_data = entry.select("div.meta dd")
        album["publishDate"] = meta_data[0].text.strip()
        album["genre"] = meta_data[1].text.strip().split(", ")
        album["publisher"] = meta_data[2].text.strip()
        album["entertainment"] = meta_data[3].text.strip()
        contin_section = soup.select_one("div.section_contin")
        songs_html = contin_section.select("tbody tr")
        album["titleTrack"] = -1
        tT = False
        songs = []
        for song in songs_html:
            td = song.select("td")
            temp = {}
            temp["track"] = int(td[1].select_one("span.rank").text.strip())
            songId = re.search(
                r"goSongDetail\('(\d+)'\)", td[2].select_one("a")["href"]
            )
            temp["songId"] = songId.group(1)
            temp["title"] = td[3].select_one("div.wrap_song_info > div a").text.strip()
            if td[3].select_one("div.wrap_song_info > div span.title") is not None:
                if tT:
                    album["titleTrack"] = -1
                else:
                    album["titleTrack"] = temp["track"]
                    tT = True
            temp["artist"] = (
                td[3]
                .select_one("div.wrap_song_info div.rank02 span")
                .text.strip()
                .split(", ")
            )

            songs.append(temp)

        album["songCount"] = len(songs)
        album["songs"] = songs
        return Response(
            json.dumps(album),
            status=200,
            mimetype="application/json",
        )
    except:
        return Response(
            json.dumps({"msg": "Internal error"}),
            status=500,
            mimetype="application/json",
        )