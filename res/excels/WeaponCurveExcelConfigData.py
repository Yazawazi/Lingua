from ..common.ArithEnum import ArithEnum
from ..common.GrowCurveEnum import GrowCurveEnum


def WeaponCurveExcelConfigData(config):
    newConfig = {
        "level": config["level"]
    }

    if "curveInfos" in config:
        newConfig["curveInfos"] = config["curveInfos"]

        for index, value in enumerate(newConfig["curveInfos"]):
            if "type" in value:
                newConfig["curveInfos"][index]["type"] = GrowCurveEnum(value["type"]).name

            if "arith" in value:
                newConfig["curveInfos"][index]["arith"] = ArithEnum(value["arith"]).name

    return newConfig
