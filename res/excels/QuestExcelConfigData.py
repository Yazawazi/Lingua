from ..common.QuestGuideEnum import QuestGuideEnum


def QuestExcelConfigData(config):
    newConfig = {
        "descTextMapHash": config["descTextMapHash"],
        "acceptCond": [],
        "finishCond": [],
        "failCond": [],
        "beginExec": [],
        "finishExec": [],
        "failExec": []
    }

    if "subId" in config:
        newConfig["subId"] = config["subId"]

    if "mainId" in config:
        newConfig["mainId"] = config["mainId"]

    if "order" in config:
        newConfig["order"] = config["order"]

    if "guide" in config:
        newConfig["guide"] = config["guide"]
        if "type" in newConfig["guide"]:
            newConfig["guide"]["type"] = QuestGuideEnum(newConfig["guide"]["type"]).name

    return newConfig
