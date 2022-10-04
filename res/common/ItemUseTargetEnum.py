from enum import Enum


class ItemUseTargetEnum(Enum):
    ITEM_USE_TARGET_NONE = 0
    ITEM_USE_TARGET_CUR_AVATAR = 1
    ITEM_USE_TARGET_CUR_TEAM = 2
    ITEM_USE_TARGET_SPECIFY_AVATAR = 3
    ITEM_USE_TARGET_SPECIFY_ALIVE_AVATAR = 4
    ITEM_USE_TARGET_SPECIFY_DEAD_AVATAR = 5
    ITEM_USE_TARGET_PLAYER_AVATAR = 6