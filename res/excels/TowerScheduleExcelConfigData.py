def TowerScheduleExcelConfigData(config):
    return {
        "scheduleId": config["scheduleId"],
        "entranceFloorId": config["entranceFloorId"],
        "schedules": config["schedules"],
        "monthlyLevelConfigId": config["monthlyLevelConfigId"]
    }
