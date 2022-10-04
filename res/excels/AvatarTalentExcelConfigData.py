from ..common.FightPropEnum import FightPropEnum


def AvatarTalentExcelConfigData(config):
    newConfig = {
        "talentId": config["talentId"],
        "nameTextMapHash": config["nameTextMapHash"],
        "icon": config["icon"],
        "mainCostItemId": config["mainCostItemId"],
        "mainCostItemCount": config["mainCostItemCount"],
        "openConfig": "",
        "addProps": [{}, {}],
        "paramList": config["paramList"]
    }

    if "prevTalent" in config:
        newConfig["prevTalent"] = config["prevTalent"]

    if "openConfig" in config:
        newConfig["openConfig"] = config["openConfig"]

    if "addProps" in config:
        for index, value in enumerate(config["addProps"]):
            addPropConfig = value
            if "propType" in addPropConfig:
                addPropConfig["propType"] = FightPropEnum(addPropConfig["propType"]).name
            newConfig["addProps"][index] = addPropConfig

    return newConfig
