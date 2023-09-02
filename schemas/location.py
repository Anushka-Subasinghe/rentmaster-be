def locationEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "date": item["date"],
        "day": item["day"],
        "time": item["time"],
        "reason": item["reason"],
        "location": item["location"]
    }


def usersEntity(entity) -> list:
    return [locationEntity(item) for item in entity]


def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
