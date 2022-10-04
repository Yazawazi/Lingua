def ReliquaryCodexExcelConfigData(config):
    newConfig = {
        "Id": config["id"],
        "suitId": config["suitId"],
        "level": config["level"],
        "sortOrder": config["sortOrder"]
    }

    if "cupId" in config:
        newConfig["cupId"] = config["cupId"]

    if "leatherId" in config:
        newConfig["leatherId"] = config["leatherId"]

    if "capId" in config:
        newConfig["capId"] = config["capId"]

    if "flowerId" in config:
        newConfig["flowerId"] = config["flowerId"]

    if "sandId" in config:
        newConfig["sandId"] = config["sandId"]

    return newConfig
