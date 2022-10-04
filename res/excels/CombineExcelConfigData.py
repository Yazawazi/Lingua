from ..common.RecipeEnum import RecipeEnum


def CombineExcelConfigData(config):
    newConfig = {
        "combineId": config["combineId"],
        "combineType": config["combineType"],
        "resultItemId": config["resultItemId"],
        "resultItemCount": config["resultItemCount"],
        "randomItems": [],
        "materialItems": config["materialItems"],
        "recipeType": RecipeEnum(config["recipeType"]).name
    }

    if "playerLevel" in config:
        newConfig["playerLevel"] = config["playerLevel"]

    if "isDefaultShow" in config:
        newConfig["isDefaultShow"] = config["isDefaultShow"]

    if "subCombineType" in config:
        newConfig["subCombineType"] = config["subCombineType"]

    if "scoinCost" in config:
        newConfig["scoinCost"] = config["scoinCost"]

    if "randomItems" in config:
        newConfig["randomItems"] = config["randomItems"]

    return newConfig
