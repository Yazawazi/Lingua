from ..common.ItemEnum import ItemEnum
from ..common.DestroyEnum import DestroyEnum
from ..common.FightPropEnum import FightPropEnum
from ..common.GrowCurveEnum import GrowCurveEnum


def WeaponExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "weaponPromoteId": config["weaponPromoteId"],
        "weaponBaseExp": config["weaponBaseExp"],
        "awakenCosts": [],
        "skillAffix": config["skillAffix"],
        "weaponProp": [],
        "nameTextMapHash": config["nameTextMapHash"]
    }

    if "rankLevel" in config:
        newConfig["rankLevel"] = config["rankLevel"]

    if "rank" in config:
        newConfig["rank"] = config["rank"]

    if "weight" in config:
        newConfig["weight"] = config["weight"]

    if "gadgetId" in config:
        newConfig["gadgetId"] = config["gadgetId"]

    if "destroyReturnMaterial" in config:
        newConfig["destroyReturnMaterial"] = config["destroyReturnMaterial"]

    if "destroyReturnMaterialCount" in config:
        newConfig["destroyReturnMaterialCount"] = config["destroyReturnMaterialCount"]

    if "itemType" in config:
        newConfig["itemType"] = ItemEnum(config["itemType"]).name

    if "destroyRule" in config:
        newConfig["destroyRule"] = DestroyEnum(config["destroyRule"]).name

    if "storyId" in config:
        newConfig["storyId"] = config["storyId"]

    if "awakenMaterial" in config:
        newConfig["awakenMaterial"] = config["awakenMaterial"]

    if "awakenCosts" in config:
        newConfig["awakenCosts"] = config["awakenCosts"]

    if "weaponProp" in config:
        newConfig["weaponProp"] = config["weaponProp"]
        for index, value in enumerate(newConfig["weaponProp"]):
            if "propType" in value:
                newConfig["weaponProp"][index]["propType"] = FightPropEnum(value["propType"]).name
            if "type" in value:
                newConfig["weaponProp"][index]["type"] = GrowCurveEnum(value["type"]).name

    return newConfig
