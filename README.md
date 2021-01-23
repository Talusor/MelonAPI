# MelonAPI

Custom API of Korea music site Melon

---

# Get Song Info

```http
GET /song/info?id=
```

| Parameter |            Description            | Required |
| :-------: | :-------------------------------: | :------: |
|   `id`    | id of song to get the information |   Yes    |

### Sample

```http
GET /song/info?id=4451155
```

### Response

```json
{
    "albumCover": "https://cdnimg.melon.co.kr/cm/album/images/022/33/048/2233048_500.jpg",
    "title": "겨울을 걷는다",
    "artist": "윤딴딴",
    "album": "반오십",
    "albumId": "2233048",
    "publishDate": "2014.02.14",
    "genre": ["인디음악", "록/메탈"],
    "lyric": "벌써 몇 달 짼가\n너 만난다는 그 사람 \n얘길 들었어\n아마 뭔 일이 \n있었나 저쨌나\n떠들어대던 심보가\n이젠 여기까지 \n발동해서 널\n떠올리게 됐나봐\n또 어쩌다 친구들에게\n그 시절 얘길 들어도\n내가 한 마디 못한 너를\n멋대로 막돼먹게 \n말을 맘대로 막해\n막 때리지도 못해 내 자신을\n난 그게 문제였어\n너와 이별에\n난 버린 것이 많고\n찾을 것이 많고\n가는 마음마다 \n머물지를 잘 못해\n사랑했던 시간 \n널 좋아했던\n그 많은 아픈 날을 걸었네\n너와 이별은\n또 많은 날을 울게 만들었어\n이젠 모두 지난 얘기지만\n시간이 지난 난\n처음 널 만났던\n그 겨울 속을 걸어가\n눈물없인 볼 수 없다던\n한참 인기 많은 \n영화를 봤어\n아마 주인공이 죽었나 저쨌나\n떠들어대는 사람들\n아마 둘은 다신 볼 수 없었지\n그건 영화이니까\n오 내 주변에 \n여자가 많단 그런\n헛소릴 듣고 \n웃을 때가 아니야\n아니 왜 내 얘길 \n내가 맘대로 못해\n변명도 못해 남탓도 못해\n암말도 못해 웃어 이자식이\n난 그게 재미없어\n너와 이별에\n난 버린 것이 많고\n찾을 것이 많고\n가는 마음마다 \n머물지를 잘 못해\n사랑했던 시간 널 좋아했던\n그 많은 아픈 날을 걸었네\n너와 이별은\n또 많은 날을 울게 만들었어\n이젠 모두 지난 얘기지만\n시간이 지난 난\n처음 널 만났던\n그 겨울 속을 걸어가\n걷다보면 시간이 말하겠지\n그 겨울 속을 걸어가\n걷다보면 마음이 말해주겠지\n너와 이별은\n참 버린 것이 많던\n찾을 것이 많던\n가는 마음 따라 \n흘러갔던 시간이\n내게 줬던 아픈 \n힘들었었던\n모든 걸 참으라고 말했네\n너와 이별은\n더 꺼내지도 않는 \n말이 돼버린걸\n이젠 모두 지난 얘긴거야\n시간이 지난 난\n시간이 지난 난\n그 겨울 속을 걸어가"
}
```

---

# Search Song by name

```http
GET /song/search?query=
```

| Parameter | Description  | Required |
| :-------: | :----------: | :------: |
|  `query`  | search query |   Yes    |

### Sample

```http
GET /song/search?query=진인사대천명
```

### Response

```json
{
    "count": 7,
    "result": [
        {
            "songId": "32334447",
            "title": "진인사대천명",
            "artist": "호미들",
            "artistId": "2754623",
            "album": "진인사대천명(盡人事待天命)",
            "albumId": "10379668"
        },
        {
            "songId": "31362504",
            "title": "진인사대천명",
            "artist": "고니밴드 (GonyBand)",
            "artistId": "2306503",
            "album": "끝없는 물음",
            "albumId": "10213084"
        },
        {
            "songId": "32334450",
            "title": "REDZONE",
            "artist": "호미들",
            "artistId": "2754623",
            "album": "진인사대천명(盡人事待天命)",
            "albumId": "10379668"
        },
        {
            "songId": "32334449",
            "title": "Boys from the mud",
            "artist": "호미들",
            "artistId": "2754623",
            "album": "진인사대천명(盡人事待天命)",
            "albumId": "10379668"
        },
        {
            "songId": "32334448",
            "title": "clink",
            "artist": "호미들",
            "artistId": "2754623",
            "album": "진인사대천명(盡人事待天命)",
            "albumId": "10379668"
        },
        {
            "songId": "2898397",
            "title": "진인사대천명",
            "artist": "박상문뮤직웍스",
            "artistId": "493013",
            "album": "한자학습동요 2",
            "albumId": "999605"
        },
        {
            "songId": "1596246",
            "title": "진인사대천명",
            "artist": "Various Artists",
            "artistId": null,
            "album": "노래로 배우는 고사성어",
            "albumId": "347536"
        }
    ]
}
```

---

# Get Album Info

```http
GET /album/info?id=
```

| Parameter |            Description             | Required |
| :-------: | :--------------------------------: | :------: |
|   `id`    | id of album to get the information |   Yes    |

### Sample

```http
GET /album/info?id=2233048
```

### Response

```json
{
    "albumCover": "https://cdnimg.melon.co.kr/cm/album/images/022/33/048/2233048_500.jpg",
    "kind": "[싱글]",
    "title": "반오십",
    "artist": "윤딴딴",
    "publishDate": "2014.02.14",
    "genre": ["인디음악", "록/메탈"],
    "publisher": "포크라노스",
    "entertainment": "Romantic Planet (로맨틱플래닛)",
    "titleTrack": 2,
    "songCount": 5,
    "songs": [
        {
            "track": 1,
            "songId": "4451154",
            "title": "친하게 지내자 (원래버전)",
            "artist": ["윤딴딴"]
        },
        {
            "track": 2,
            "songId": "4451155",
            "title": "겨울을 걷는다",
            "artist": ["윤딴딴"]
        },
        {
            "track": 3,
            "songId": "4451156",
            "title": "그대 눈에 톡",
            "artist": ["윤딴딴"]
        },
        {
            "track": 4,
            "songId": "4451157",
            "title": "친하게 지내자 (다른버전)",
            "artist": ["윤딴딴"]
        },
        {
            "track": 5,
            "songId": "4451158",
            "title": "겨울을 걷는다 (스튜디오 라이브 버전)",
            "artist": ["윤딴딴"]
        }
    ]
}
```
