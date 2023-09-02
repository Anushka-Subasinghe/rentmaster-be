def diaryEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "text": item["text"],
        "summerize": item["summerize"],
        "is_summerized": item["is_summerized"],
        "date": item["date"],
    }


def diaryEntity(entity) -> list:
    return [diaryEntity(item) for item in entity]


def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
