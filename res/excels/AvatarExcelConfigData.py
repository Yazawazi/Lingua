from ..common.BodyEnum import BodyEnum
from ..common.WeaponEnum import WeaponEnum
from ..common.QualityEnum import QualityEnum
from ..common.GrowCurveEnum import GrowCurveEnum
from ..common.FightPropEnum import FightPropEnum
from ..common.AvatarIdentityEnum import AvatarIdentityEnum


def AvatarExcelConfigData(config):
    newConfig = {
        "iconName": config["iconName"],
        "bodyType": BodyEnum(config["bodyType"]).name,
        "qualityType": QualityEnum(config["qualityType"]).name,
        "chargeEfficiency": config["chargeEfficiency"],
        "initialWeapon": config["initialWeapon"],
        "weaponType": WeaponEnum(config["weaponType"]).name,
        "imageName": config["imageName"],
        "avatarPromoteId": config["avatarPromoteId"],
        "cutsceneShow": "",
        "skillDepotId": config["skillDepotId"],
        "staminaRecoverSpeed": config["staminaRecoverSpeed"],
        "candSkillDepotIds": [],
        "avatarPromoteRewardLevelList": [],
        "avatarPromoteRewardIdList": [],
        "nameTextMapHash": config["nameTextMapHash"],
        "hpBase": config["hpBase"],
        "attackBase": config["attackBase"],
        "defenseBase": config["defenseBase"],
        "critical": config["critical"],
        "criticalHurt": config["criticalHurt"],
        "propGrowCurves": []
    }

    if "avatarIdentityType" in config:
        newConfig["avatarIdentityType"] = AvatarIdentityEnum(config["avatarIdentityType"]).name

    if "candSkillDepotIds" in config:
        newConfig["candSkillDepotIds"] = config["candSkillDepotIds"]

    if "avatarPromoteRewardLevelList" in config:
        newConfig["avatarPromoteRewardLevelList"] = config["avatarPromoteRewardLevelList"]

    if "avatarPromoteRewardIdList" in config:
        newConfig["avatarPromoteRewardIdList"] = config["avatarPromoteRewardIdList"]

    for propGrowCurve in config["propGrowCurves"]:
        try:
            typeName = FightPropEnum(propGrowCurve["type"]).name
        except:
            typeName = "UNDEFINED"

        try:
            growCurve = GrowCurveEnum(propGrowCurve["growCurve"]).name
        except:
            growCurve = "UNDEFINED"

        newConfig["propGrowCurves"].append({
            "type": typeName,
            "growCurve": growCurve
        })

    return newConfig
