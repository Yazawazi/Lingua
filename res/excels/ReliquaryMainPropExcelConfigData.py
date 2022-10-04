from ..common.FightPropEnum import FightPropEnum


def ReliquaryMainPropExcelConfigData(config):
    return {
        "id": config["id"],
        "propDepotId": config["propDepotId"],
        "propType": FightPropEnum(config["propType"]).name
    }
