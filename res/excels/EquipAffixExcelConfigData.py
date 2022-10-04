def EquipAffixExcelConfigData(config):
    newConfig = {
        "affixId": config["affixId"],
        "id": config["id"],
        "nameTextMapHash": config["nameTextMapHash"],
        "openConfig": "",
        "addProps": config["addProps"],
        "paramList": config["paramList"]
    }

    if "openConfig" in config:
        newConfig["openConfig"] = config["openConfig"]

    if "level" in config:
        newConfig["level"] = config["level"]

    return newConfig
