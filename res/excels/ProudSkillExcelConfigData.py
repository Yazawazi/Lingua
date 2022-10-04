from ..common.FightPropEnum import FightPropEnum
from ..common.TalentFilterEnum import TalentFilterEnum


def ProudSkillExcelConfigData(config):
    newConfig = {
        "proudSkillId": config["proudSkillId"],
        "proudSkillGroupId": config["proudSkillGroupId"],
        "level": config["level"],
        "proudSkillType": config["proudSkillType"],
        "openConfig": "",
        "costItems": config["costItems"],
        "filterConds": [],
        "lifeEffectParams": config["lifeEffectParams"],
        "addProps": [{}, {}],
        "paramList": config["paramList"],
        "paramDescList": config["paramDescList"],
        "nameTextMapHash": config["nameTextMapHash"]
    }

    if "coinCost" in config:
        newConfig["coinCost"] = config["coinCost"]

    if "breakLevel" in config:
        newConfig["breakLevel"] = config["breakLevel"]

    if "openConfig" in config:
        newConfig["openConfig"] = config["openConfig"]

    if "filterConds" in config:
        newConfig["filterConds"] = config["filterConds"]
        for index, value in enumerate(newConfig["filterConds"]):
            newConfig["filterConds"][index] = TalentFilterEnum(value).name

    if "addProps" in config:
        for index, value in enumerate(config["addProps"]):
            addPropConfig = value
            if "propType" in addPropConfig:
                addPropConfig["propType"] = FightPropEnum(addPropConfig["propType"]).name
            newConfig["addProps"][index] = addPropConfig

    return newConfig
