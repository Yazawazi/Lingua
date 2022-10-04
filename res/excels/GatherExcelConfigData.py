def GatherExcelConfigData(config):
    # thank ayy lmao
    newConfig = {
        "pointType": config["pointType"],
        "id": config["id"],
        "gadgetId": config["gadgetId"],
        "itemId": config["itemId"],
        "cd": config["cd"]
    }

    if "isForbidGuest" in config:
        newConfig["isForbidGuest"] = config["isForbidGuest"]

    if "initDisableInteract" in config:
        newConfig["initDisableInteract"] = config["initDisableInteract"]

    return newConfig
