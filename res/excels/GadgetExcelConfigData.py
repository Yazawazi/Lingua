from ..common.GadgetEnum import GadgetEnum


def GadgetExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "jsonName": "",
        "tags": [],
        "itemJsonName": "",
        "nameTextMapHash": config["nameTextMapHash"]
    }

    if "type" in config:
        newConfig["type"] = GadgetEnum(config["type"]).name

    if "jsonName" in config:
        newConfig["jsonName"] = config["jsonName"]

    if "tags" in config:
        newConfig["tags"] = config["tags"]

    if "isInteractive" in config:
        newConfig["isInteractive"] = config["isInteractive"]

    if "itemJsonName" in config:
        newConfig["itemJsonName"] = config["itemJsonName"]

    if "campId" in config:
        newConfig["campID"] = config["campId"]

    return newConfig
