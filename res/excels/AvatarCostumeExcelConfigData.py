def AvatarCostumeExcelConfigData(config):
    newConfig = {
        "costumeId": config["skinId"],
        "characterId": config["characterId"]
    }

    if "itemId" in config:
        newConfig["itemId"] = config["itemId"]

    if "quality" in config:
        newConfig["quality"] = config["quality"]

    return newConfig
