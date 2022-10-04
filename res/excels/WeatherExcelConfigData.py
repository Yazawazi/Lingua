from ..common.ClimateEnum import ClimateEnum


def WeatherExcelConfigData(config):
    newConfig = {
        "areaID": config["areaId"],
        "weatherAreaId": config["weatherAreaId"],
        "maxHeightStr": "",
        "priority": config["priority"],
        "profileName": config["profileName"],
        "defaultClimate": ClimateEnum(config["defaultClimate"]).name,
        "sceneID": config["sceneId"]
    }

    if "maxHeightStr" in config:
        newConfig["maxHeightStr"] = config["maxHeightStr"]

    if "gadgetId" in config:
        newConfig["gadgetID"] = config["gadgetId"]

    if "isDefaultValid" in config:
        newConfig["isDefaultValid"] = config["isDefaultValid"]

    if "isUseDefault" in config:
        newConfig["isUseDefault"] = config["isUseDefault"]

    return newConfig
