def WeaponCodexExcelConfigData(config):
    newConfig = {
        "Id": config["id"],
        "weaponId": config["weaponId"],
        "sortOrder": config["sortOrder"]
    }

    return newConfig
