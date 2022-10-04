def PlayerLevelExcelConfigData(config):
    newConfig = {
        "level": config["level"],
        "unlockDescTextMapHash": config["unlockDescTextMapHash"]
    }

    if "exp" in config:
        newConfig["exp"] = config["exp"]

    if "rewardId" in config:
        newConfig["rewardId"] = config["rewardId"]

    if "expeditionLimitAdd" in config:
        newConfig["expeditionLimitAdd"] = config["expeditionLimitAdd"]

    if "unlockWorldLevel" in config:
        newConfig["unlockWorldLevel"] = config["unlockWorldLevel"]

    return newConfig
