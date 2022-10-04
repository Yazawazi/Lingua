def CookBonusExcelConfigData(config):
    newConfig = {
        "avatarId": config["avatarId"],
        "recipeId": config["recipeId"],
        "paramVec": config["paramVec"],
        "complexParamVec": config["complexParamVec"]
    }

    return newConfig
