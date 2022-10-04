from ..common.CodexEnum import CodexEnum
from ..common.CodexCountEnum import CodexCountEnum


def AnimalCodexExcelConfigData(config):
    newConfig = {
        "Id": config["id"],
        "describeId": config["describeId"],
        "sortOrder": config["sortOrder"]
    }

    if "type" in config:
        newConfig["type"] = CodexEnum(config["type"]).name

    if "countType" in config:
        newConfig["countType"] = CodexCountEnum(config["countType"]).name

    return newConfig
