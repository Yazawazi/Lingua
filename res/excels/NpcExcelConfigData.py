def NpcExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "jsonName": "",
        "alias": "",
        "scriptDataPath": config["scriptDataPath"],
        "luaDataPath": "",
        "dyePart": "",
        "billboardIcon": "",
        "nameTextMapHash": config["nameTextMapHash"],
        "campID": config["campId"]
    }

    if "jsonName" in config:
        newConfig["jsonName"] = config["jsonName"]

    if "alias" in config:
        newConfig["alias"] = config["alias"]

    if "luaDataPath" in config:
        newConfig["luaDataPath"] = config["luaDataPath"]

    if "hasMove" in config:
        newConfig["hasMove"] = config["hasMove"]

    if "billboardIcon" in config:
        newConfig["billboardIcon"] = config["billboardIcon"]

    return newConfig
