from ..common.FightPropEnum import FightPropEnum


def ReliquaryAffixExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "depotId": config["depotId"],
        "groupId": config["groupId"],
        "propType": FightPropEnum(config["propType"]).name,
        "propValue": config["propValue"]
    }

    return newConfig
