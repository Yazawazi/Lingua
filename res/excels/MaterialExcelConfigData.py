from ..common.ItemEnum import ItemEnum
from ..common.DestroyEnum import DestroyEnum
from ..common.ItemUseEnum import ItemUseEnum
from ..common.MaterialEnum import MaterialEnum
from ..common.FoodQualityEnum import FoodQualityEnum
from ..common.ItemUseTargetEnum import ItemUseTargetEnum


def MaterialExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "effectName": "",
        "destroyReturnMaterial": [],
        "destroyReturnMaterialCount": [],
        "satiationParams": [],
        "itemUse": [],
        "nameTextMapHash": config["nameTextMapHash"]
    }

    if "stackLimit" in config:
        newConfig["stackLimit"] = config["stackLimit"]

    if "maxUseCount" in config:
        newConfig["maxUseCount"] = config["maxUseCount"]

    if "rankLevel" in config:
        newConfig["rankLevel"] = config["rankLevel"]

    if "effectName" in config:
        newConfig["effectName"] = config["effectName"]

    if "rank" in config:
        newConfig["rank"] = config["rank"]

    if "weight" in config:
        newConfig["weight"] = config["weight"]

    if "gadgetId" in config:
        newConfig["gadgetId"] = config["gadgetId"]

    if "itemType" in config:
        newConfig["itemType"] = ItemEnum(config["itemType"]).name

    if "materialType" in config:
        newConfig["materialType"] = MaterialEnum(config["materialType"]).name

    if "destroyRule" in config:
        newConfig["destroyRule"] = DestroyEnum(config["destroyRule"]).name

    if "foodQuality" in config:
        newConfig["foodQuality"] = FoodQualityEnum(config["foodQuality"]).name

    if "satiationParams" in config:
        newConfig["satiationParams"] = config["satiationParams"]

    if "useTarget" in config:
        newConfig["useTarget"] = ItemUseTargetEnum(config["useTarget"]).name

    if "itemUse" in config:
        newConfig["itemUse"] = config["itemUse"]
        for index, single in enumerate(newConfig["itemUse"]):
            if "useOp" in single:
                newConfig["itemUse"][index]["useOp"] = ItemUseEnum(single["useOp"]).name

    return newConfig
