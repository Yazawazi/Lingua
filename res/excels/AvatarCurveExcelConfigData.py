from ..common.ArithEnum import ArithEnum
from ..common.GrowCurveEnum import GrowCurveEnum


def AvatarCurveExcelConfigData(config):
    newConfig = {
        "level": config["level"],
        "curveInfos": []
    }

    if "curveInfos" in config:
        for curveInfo in config["curveInfos"]:
            try:
                typeName = GrowCurveEnum(curveInfo["type"]).name
            except:
                typeName = "UNDEFINED"

            try:
                arith = ArithEnum(curveInfo["arith"]).name
            except:
                arith = "UNDEFINED"

            newConfig["curveInfos"].append({
                "type": typeName,
                "arith": arith,
                "value": curveInfo["value"]
            })

    return newConfig
