def CookRecipeExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "rankLevel": config["rankLevel"],
        "maxProficiency": config["maxProficiency"],
        "qualityOutputVec": config["qualityOutputVec"],
        "inputVec": config["inputVec"]
    }

    if "isDefaultUnlocked" in config:
        newConfig["isDefaultUnlocked"] = config["isDefaultUnlocked"]

    return newConfig
