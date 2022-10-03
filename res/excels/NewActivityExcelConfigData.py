from ..common.NewActivityEnum import NewActivityEnum


def NewActivityExcelConfigData(config):
    newConfig = {
        "activityId": config["activityId"],
        "activityType": "",
        "nameTextMapHash": "",
        "condGroupId": [],
        "watcherId": []
    }

    if "nameTextMapHash" in config:
        newConfig["nameTextMapHash"] = config["nameTextMapHash"]

    if "condGroupId" in config:
        newConfig["condGroupId"] = config["condGroupId"]

    if "watcherId" in config:
        newConfig["watcherId"] = config["watcherId"]

    if "activityType" in config:
        try:
            newConfig["activityType"] = NewActivityEnum(config["activityType"]).name
        except:
            newConfig["activityType"] = "UNDEFINED"
    else:
        newConfig["activityType"] = "UNDEFINED"

    return newConfig
