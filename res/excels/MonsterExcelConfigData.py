from ..common.MonsterEnum import MonsterEnum
from ..common.FightPropEnum import FightPropEnum
from ..common.GrowCurveEnum import GrowCurveEnum


def MonsterExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "monsterName": config["monsterName"],
        "type": MonsterEnum(config["type"]).name,
        "serverScript": "",
        "affix": [],
        "ai": "",
        "equips": config["equips"],
        "hpDrops": config["hpDrops"],
        "excludeWeathers": "",
        "mpPropID": config["mpPropId"],
        "skin": "",
        "hpBase": config["hpBase"],
        "propGrowCurves": [],
        "nameTextMapHash": config["nameTextMapHash"]
    }

    if "ai" in config:
        newConfig["ai"] = config["ai"]

    if "featureTagGroupId" in config:
        newConfig["featureTagGroupID"] = config["featureTagGroupId"]

    if "serverScript" in config:
        newConfig["serverScript"] = config["serverScript"]

    if "affix" in config:
        newConfig["affix"] = config["affix"]

    if "killDropId" in config:
        newConfig["killDropId"] = config["killDropId"]

    if "excludeWeathers" in config:
        newConfig["excludeWeathers"] = config["excludeWeathers"]

    if "skin" in config:
        newConfig["skin"] = config["skin"]

    if "describeId" in config:
        newConfig["describeId"] = config["describeId"]

    if "attackBase" in config:
        newConfig["attackBase"] = config["attackBase"]

    if "defenseBase" in config:
        newConfig["defenseBase"] = config["defenseBase"]

    if "fireSubHurt" in config:
        newConfig["fireSubHurt"] = config["fireSubHurt"]

    if "elecSubHurt" in config:
        newConfig["elecSubHurt"] = config["elecSubHurt"]

    if "grassSubHurt" in config:
        newConfig["grassSubHurt"] = config["grassSubHurt"]

    if "waterSubHurt" in config:
        newConfig["waterSubHurt"] = config["waterSubHurt"]

    if "windSubHurt" in config:
        newConfig["windSubHurt"] = config["windSubHurt"]

    if "rockSubHurt" in config:
        newConfig["rockSubHurt"] = config["rockSubHurt"]

    if "iceSubHurt" in config:
        newConfig["iceSubHurt"] = config["iceSubHurt"]

    if "physicalSubHurt" in config:
        newConfig["physicalSubHurt"] = config["physicalSubHurt"]

    if "combatBGMLevel" in config:
        newConfig["combatBGMLevel"] = config["combatBGMLevel"]

    if "entityBudgetLevel" in config:
        newConfig["entityBudgetLevel"] = config["entityBudgetLevel"]

    if "propGrowCurves" in config:
        newConfig["propGrowCurves"] = config["propGrowCurves"]
        for index, value in enumerate(newConfig["propGrowCurves"]):
            if "type" in value:
                newConfig["propGrowCurves"][index]["type"] = FightPropEnum(value["type"]).name

            if "growCurve" in value:
                newConfig["propGrowCurves"][index]["growCurve"] = GrowCurveEnum(value["growCurve"]).name

    if "campId" in config:
        newConfig["campID"] = config["campId"]

    return newConfig
