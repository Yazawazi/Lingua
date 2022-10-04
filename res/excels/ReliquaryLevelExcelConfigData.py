from ..common.FightPropEnum import FightPropEnum


def ReliquaryLevelExcelConfigData(config):
    newConfig = {
        "level": config["level"],
        "addProps": [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    }

    if "rank" in config:
        newConfig["rank"] = config["rank"]

    if "exp" in config:
        newConfig["exp"] = config["exp"]

    if "addProps" in config:
        for index, value in enumerate(config["addProps"]):
            addPropConfig = value
            if "propType" in addPropConfig:
                addPropConfig["propType"] = FightPropEnum(addPropConfig["propType"]).name
            newConfig["addProps"][index] = addPropConfig

    return newConfig
