def AvatarTalentExcelConfigData(config):
    newConfig = {
        "talentId": config["talentId"],
        "nameTextMapHash": config["nameTextMapHash"],
        "icon": config["icon"],
        "mainCostItemId": config["mainCostItemId"],
        "mainCostItemCount": config["mainCostItemCount"],
        "openConfig": "",
        "addProps": config["addProps"],
        "paramList": config["paramList"]
    }

    if "prevTalent" in config:
        newConfig["prevTalent"] = config["prevTalent"]

    if "openConfig" in config:
        newConfig["openConfig"] = config["openConfig"]

    return newConfig
