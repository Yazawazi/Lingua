def ChapterExcelConfigData(config):
    newConfig = {
        "id": config["id"]
    }

    if "beginQuestId" in config:
        newConfig["beginQuestId"] = config["beginQuestId"]

    if "endQuestId" in config:
        newConfig["endQuestId"] = config["endQuestId"]

    if "needPlayerLevel" in config:
        newConfig["needPlayerLevel"] = config["needPlayerLevel"]

    return newConfig
