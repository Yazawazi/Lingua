def QuestCodexExcelConfigData(config):
    newConfig = {
        "Id": config["id"],
        "parentQuestId": config["parentQuestId"],
        "chapterId": config["chapterId"],
        "sortOrder": config["sortOrder"]
    }

    if "isDisuse" in config:
        newConfig["isDisuse"] = config["isDisuse"]

    return newConfig
