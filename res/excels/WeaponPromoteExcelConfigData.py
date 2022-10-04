from ..common.FightPropEnum import FightPropEnum


def WeaponPromoteExcelConfigData(config):
    newConfig = {
        "weaponPromoteId": config["weaponPromoteId"],
        "costItems": [{}, {}, {}],
        "unlockMaxLevel": config["unlockMaxLevel"],
        "addProps": [{}, {}, {}, {}, {}]
    }

    if "promoteLevel" in config:
        newConfig["promoteLevel"] = config["promoteLevel"]

    if "coinCost" in config:
        newConfig["coinCost"] = config["coinCost"]

    if "costItems" in config:
        for index, value in enumerate(config["costItems"]):
            newConfig["costItems"][index] = value

    if "addProps" in config:
        for index, value in enumerate(config["addProps"]):
            addPropConfig = value
            if "propType" in addPropConfig:
                addPropConfig["propType"] = FightPropEnum(addPropConfig["propType"]).name
            newConfig["addProps"][index] = addPropConfig

    if "requiredPlayerLevel" in config:
        newConfig["requiredPlayerLevel"] = config["requiredPlayerLevel"]

    return newConfig
