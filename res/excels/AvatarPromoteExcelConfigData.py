from ..common.FightPropEnum import FightPropEnum


def AvatarPromoteExcelConfigData(config):
    newConfig = {
        "avatarPromoteId": config["avatarPromoteId"],
        "costItems": [{}, {}, {}, {}],
        "unlockMaxLevel": config["unlockMaxLevel"],
        "addProps": [{}, {}, {}, {}]
    }

    if "promoteLevel" in config:
        newConfig["promoteLevel"] = config["promoteLevel"]

    if "scoinCost" in config:
        newConfig["scoinCost"] = config["scoinCost"]

    if "costItems" in config:
        for index, value in enumerate(config["costItems"]):
            newConfig["costItems"][index] = value

    if "addProps" in config:
        for index, value in enumerate(config["addProps"]):
            addPropConfig = value
            addPropConfig["propType"] = FightPropEnum(addPropConfig["propType"]).name
            newConfig["addProps"][index] = addPropConfig

    if "requiredPlayerLevel" in config:
        newConfig["requiredPlayerLevel"] = config["requiredPlayerLevel"]

    return newConfig
