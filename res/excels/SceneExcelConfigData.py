from ..common.SceneEnum import SceneEnum


def SceneExcelConfigData(config):
    return {
        "id": config["id"],
        "type": SceneEnum(config["type"]).name,
        "scriptData": config["scriptData"]
    }
