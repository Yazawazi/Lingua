def RewardPreviewExcelConfigData(config):
    newConfig =  {
        "previewItems": config["previewItems"]
    }

    if "id" in config:
        newConfig["id"] = config["id"]

    return newConfig
