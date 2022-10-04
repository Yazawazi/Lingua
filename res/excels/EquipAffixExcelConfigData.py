from ..common.FightPropEnum import FightPropEnum


def EquipAffixExcelConfigData(config):
    newConfig = {
        "affixId": config["affixId"],
        "id": config["id"],
        "nameTextMapHash": config["nameTextMapHash"],
        "openConfig": "",
        "addProps": [{}, {}, {}],
        "paramList": config["paramList"]
    }

    if "openConfig" in config:
        newConfig["openConfig"] = config["openConfig"]

    if "level" in config:
        newConfig["level"] = config["level"]

    if "addProps" in config:
        for index, value in enumerate(config["addProps"]):
            addPropConfig = value
            if "propType" in addPropConfig:
                addPropConfig["propType"] = FightPropEnum(addPropConfig["propType"]).name
            newConfig["addProps"][index] = addPropConfig

    return newConfig
