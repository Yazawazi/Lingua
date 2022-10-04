def MaterialCodexExcelConfigData(config):
    newConfig = {
        "Id": config["id"],
        "materialId": config["materialId"],
        "sortOrder": config["sortOrder"]
    }

    return newConfig
