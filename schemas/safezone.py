def safezoneEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "north": item["north"],
        "south": item["south"],
        "east": item["east"],
        "western": item["western"],
        "square_kms": item["square_kms"]
    }


def usersEntity(entity) -> list:
    return [safezoneEntity(item) for item in entity]


def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
