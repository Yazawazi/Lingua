from ..common.ElementEnum import ElementEnum


def AvatarSkillExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "maxChargeNum": config["maxChargeNum"],
        "nameTextMapHash": config["nameTextMapHash"],
        "descTextMapHash": config["descTextMapHash"],
        "abilityName": ""
    }

    if "isAttackCameraLock" in config:
        newConfig["isAttackCameraLock"] = config["isAttackCameraLock"]

    if "triggerId" in config:
        newConfig["triggerID"] = config["triggerId"]

    if "cdTime" in config:
        newConfig["cdTime"] = config["cdTime"]

    if "costElemVal" in config:
        newConfig["costElemVal"] = config["costElemVal"]

    if "proudSkillGroupId" in config:
        newConfig["proudSkillGroupId"] = config["proudSkillGroupId"]

    if "costElemType" in config:
        newConfig["costElemType"] = ElementEnum(config["costElemType"]).name

    if "abilityName" in config:
        newConfig["abilityName"] = config["abilityName"]

    return newConfig
