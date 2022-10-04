from ..common.ItemEnum import ItemEnum
from ..common.EquipEnum import EquipEnum
from ..common.DestroyEnum import DestroyEnum


def ReliquaryExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "rankLevel": config["rankLevel"],
        "rank": config["rank"],
        "weight": config["weight"],
        "gadgetId": config["gadgetId"],
        "destroyReturnMaterial": [],
        "destroyReturnMaterialCount": [],
        "itemType": ItemEnum(config["itemType"]).name,
        "equipType": EquipEnum(config["equipType"]).name,
        "mainPropDepotId": config["mainPropDepotId"],
        "appendPropDepotId": config["appendPropDepotId"],
        "addPropLevels": [],
        "baseConvExp": config["baseConvExp"],
        "maxLevel": config["maxLevel"],
        "nameTextMapHash": config["nameTextMapHash"]
    }

    if "destroyReturnMaterial" in config:
        newConfig["destroyReturnMaterial"] = config["destroyReturnMaterial"]

    if "destroyReturnMaterialCount" in config:
        newConfig["destroyReturnMaterialCount"] = config["destroyReturnMaterialCount"]

    if "destroyRule" in config:
        newConfig["destroyRule"] = DestroyEnum(config["destroyRule"]).name

    if "appendPropNum" in config:
        newConfig["appendPropNum"] = config["appendPropNum"]

    if "setId" in config:
        newConfig["setId"] = config["setId"]

    if "addPropLevels" in config:
        newConfig["addPropLevels"] = config["addPropLevels"]

    return newConfig
