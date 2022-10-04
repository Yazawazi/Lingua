from ..common.ElementEnum import ElementEnum


def WorldAreaConfigData(config):
    newConfig = {
        "ID": config["id"],
        "AreaID1": config["areaId1"],
        "SceneID": config["sceneId"]
    }

    if "AreaId2" in config:
        newConfig["AreaID2"] = config["areaId2"]

    if "elementType" in config:
        newConfig["elementType"] = ElementEnum(config["elementType"]).name

    return newConfig
