from ..common.ShopRefreshEnum import ShopRefresh


def ShopGoodsExcelConfigData(config):
    newConfig = {
        "goodsId": config["goodsId"],
        "shopType": config["shopType"],
        "itemCount": config["itemCount"],
        "costItems": config["costItems"],
        "minPlayerLevel": config["minPlayerLevel"],
        "maxPlayerLevel": config["maxPlayerLevel"]
    }

    if "itemId" in config:
        newConfig["itemId"] = config["itemId"]

    if "costScoin" in config:
        newConfig["costScoin"] = config["costScoin"]

    if "costHcoin" in config:
        newConfig["costHcoin"] = config["costHcoin"]

    if "costMcoin" in config:
        newConfig["costMcoin"] = config["costMcoin"]

    if "buyLimit" in config:
        newConfig["buyLimit"] = config["buyLimit"]

    if "subTabId" in config:
        newConfig["subTabId"] = config["subTabId"]

    if "refreshType" in config:
        newConfig["refreshType"] = ShopRefresh(config["refreshType"]).name

    if "refreshParam" in config:
        newConfig["refreshParam"] = config["refreshParam"]

    return newConfig
