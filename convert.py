from res.excels.NpcExcelConfigData import NpcExcelConfigData
from res.excels.WorldAreaConfigData import WorldAreaConfigData
from res.excels.QuestExcelConfigData import QuestExcelConfigData
from res.excels.SceneExcelConfigData import SceneExcelConfigData
from res.excels.AvatarExcelConfigData import AvatarExcelConfigData
from res.excels.GadgetExcelConfigData import GadgetExcelConfigData
from res.excels.GatherExcelConfigData import GatherExcelConfigData
from res.excels.RewardExcelConfigData import RewardExcelConfigData
from res.excels.WeaponExcelConfigData import WeaponExcelConfigData
from res.excels.ChapterExcelConfigData import ChapterExcelConfigData
from res.excels.CombineExcelConfigData import CombineExcelConfigData
from res.excels.DailyDungeonConfigData import DailyDungeonConfigData
from res.excels.MonsterExcelConfigData import MonsterExcelConfigData
from res.excels.WeatherExcelConfigData import WeatherExcelConfigData
from res.excels.MaterialExcelConfigData import MaterialExcelConfigData
from res.excels.CookBonusExcelConfigData import CookBonusExcelConfigData
from res.excels.ReliquaryExcelConfigData import ReliquaryExcelConfigData
from res.excels.ShopGoodsExcelConfigData import ShopGoodsExcelConfigData
from res.excels.CookRecipeExcelConfigData import CookRecipeExcelConfigData
from res.excels.EquipAffixExcelConfigData import EquipAffixExcelConfigData
from res.excels.ProudSkillExcelConfigData import ProudSkillExcelConfigData
from res.excels.QuestCodexExcelConfigData import QuestCodexExcelConfigData
from res.excels.TowerFloorExcelConfigData import TowerFloorExcelConfigData
from res.excels.TowerLevelExcelConfigData import TowerLevelExcelConfigData
from res.excels.WorldLevelExcelConfigData import WorldLevelExcelConfigData
from res.excels.AnimalCodexExcelConfigData import AnimalCodexExcelConfigData
from res.excels.AvatarCurveExcelConfigData import AvatarCurveExcelConfigData
from res.excels.AvatarLevelExcelConfigData import AvatarLevelExcelConfigData
from res.excels.AvatarSkillExcelConfigData import AvatarSkillExcelConfigData
from res.excels.NewActivityExcelConfigData import NewActivityExcelConfigData
from res.excels.PlayerLevelExcelConfigData import PlayerLevelExcelConfigData
from res.excels.WeaponCodexExcelConfigData import WeaponCodexExcelConfigData
from res.excels.WeaponCurveExcelConfigData import WeaponCurveExcelConfigData
from res.excels.WeaponLevelExcelConfigData import WeaponLevelExcelConfigData
from res.excels.AvatarTalentExcelConfigData import AvatarTalentExcelConfigData
from res.excels.MonsterCurveExcelConfigData import MonsterCurveExcelConfigData
from res.excels.PersonalLineExcelConfigData import PersonalLineExcelConfigData
from res.excels.ReliquarySetExcelConfigData import ReliquarySetExcelConfigData
from res.excels.AvatarCostumeExcelConfigData import AvatarCostumeExcelConfigData
from res.excels.AvatarPromoteExcelConfigData import AvatarPromoteExcelConfigData
from res.excels.MaterialCodexExcelConfigData import MaterialCodexExcelConfigData
from res.excels.RewardPreviewExcelConfigData import RewardPreviewExcelConfigData
from res.excels.TowerScheduleExcelConfigData import TowerScheduleExcelConfigData
from res.excels.WeaponPromoteExcelConfigData import WeaponPromoteExcelConfigData
from res.excels.AvatarFlycloakExcelConfigData import AvatarFlycloakExcelConfigData
from res.excels.ReliquaryAffixExcelConfigData import ReliquaryAffixExcelConfigData
from res.excels.ReliquaryCodexExcelConfigData import ReliquaryCodexExcelConfigData
from res.excels.ReliquaryLevelExcelConfigData import ReliquaryLevelExcelConfigData
from res.excels.MonsterDescribeExcelConfigData import MonsterDescribeExcelConfigData
from res.excels.AvatarSkillDepotExcelConfigData import AvatarSkillDepotExcelConfigData
from res.excels.ReliquaryMainPropExcelConfigData import ReliquaryMainPropExcelConfigData
from res.excels.AvatarFettersLevelExcelConfigData import AvatarFettersLevelExcelConfigData


convertMap = [{
    "file": "NewActivityExcelConfigData.json",
    "function": NewActivityExcelConfigData
}, {
    "file": "AvatarCostumeExcelConfigData.json",
    "function": AvatarCostumeExcelConfigData
}, {
    "file": "AvatarCurveExcelConfigData.json",
    "function": AvatarCurveExcelConfigData
}, {
    "file": "AvatarExcelConfigData.json",
    "function": AvatarExcelConfigData
}, {
    "file": "AvatarFettersLevelExcelConfigData.json",
    "function": AvatarFettersLevelExcelConfigData
}, {
    "file": "AvatarFlycloakExcelConfigData.json",
    "function": AvatarFlycloakExcelConfigData
}, {
    "file": "AvatarLevelExcelConfigData.json",
    "function": AvatarLevelExcelConfigData
}, {
    "file": "AvatarPromoteExcelConfigData.json",
    "function": AvatarPromoteExcelConfigData
}, {
    "file": "AvatarSkillExcelConfigData.json",
    "function": AvatarSkillExcelConfigData
}, {
    "file": "AvatarSkillDepotExcelConfigData.json",
    "function": AvatarSkillDepotExcelConfigData
}, {
    "file": "AvatarTalentExcelConfigData.json",
    "function": AvatarTalentExcelConfigData
}, {
    "file": "ChapterExcelConfigData.json",
    "function": ChapterExcelConfigData
}, {
    "file": "AnimalCodexExcelConfigData.json",
    "function": AnimalCodexExcelConfigData
}, {
    "file": "MaterialCodexExcelConfigData.json",
    "function": MaterialCodexExcelConfigData
}, {
    "file": "QuestCodexExcelConfigData.json",
    "function": QuestCodexExcelConfigData
}, {
    "file": "ReliquaryCodexExcelConfigData.json",
    "function": ReliquaryCodexExcelConfigData
}, {
    "file": "WeaponCodexExcelConfigData.json",
    "function": WeaponCodexExcelConfigData
}, {
    "file": "CombineExcelConfigData.json",
    "function": CombineExcelConfigData
}, {
    "file": "CookBonusExcelConfigData.json",
    "function": CookBonusExcelConfigData
}, {
    "file": "CookRecipeExcelConfigData.json",
    "function": CookRecipeExcelConfigData
}, {
    "file": "DailyDungeonConfigData.json",
    "function": DailyDungeonConfigData
}, {
    "file": "EquipAffixExcelConfigData.json",
    "function": EquipAffixExcelConfigData
}, {
    "file": "GadgetExcelConfigData.json",
    "function": GadgetExcelConfigData
}, {
    "file": "GatherExcelConfigData.json",
    "function": GatherExcelConfigData
}, {
    "file": "MaterialExcelConfigData.json",
    "function": MaterialExcelConfigData
}, {
    "file": "WeaponExcelConfigData.json",
    "function": WeaponExcelConfigData
}, {
    "file": "ReliquaryExcelConfigData.json",
    "function": ReliquaryExcelConfigData
}, {
    "file": "MonsterCurveExcelConfigData.json",
    "function": MonsterCurveExcelConfigData
}, {
    "file": "MonsterExcelConfigData.json",
    "function": MonsterExcelConfigData
}, {
    "file": "MonsterDescribeExcelConfigData.json",
    "function": MonsterDescribeExcelConfigData
}, {
    "file": "NpcExcelConfigData.json",
    "function": NpcExcelConfigData
}, {
    "file": "PersonalLineExcelConfigData.json",
    "function": PersonalLineExcelConfigData
}, {
    "file": "PlayerLevelExcelConfigData.json",
    "function": PlayerLevelExcelConfigData
}, {
    "file": "ProudSkillExcelConfigData.json",
    "function": ProudSkillExcelConfigData
}, {
    "file": "QuestExcelConfigData.json",
    "function": QuestExcelConfigData
}, {
    "file": "ReliquaryAffixExcelConfigData.json",
    "function": ReliquaryAffixExcelConfigData
}, {
    "file": "ReliquaryLevelExcelConfigData.json",
    "function": ReliquaryLevelExcelConfigData
}, {
    "file": "ReliquaryMainPropExcelConfigData.json",
    "function": ReliquaryMainPropExcelConfigData
}, {
    "file": "ReliquarySetExcelConfigData.json",
    "function": ReliquarySetExcelConfigData
}, {
    "file": "RewardExcelConfigData.json",
    "function": RewardExcelConfigData
}, {
    "file": "RewardPreviewExcelConfigData.json",
    "function": RewardPreviewExcelConfigData
}, {
    "file": "SceneExcelConfigData.json",
    "function": SceneExcelConfigData
}, {
    "file": "ShopGoodsExcelConfigData.json",
    "function": ShopGoodsExcelConfigData
}, {
    "file": "TowerFloorExcelConfigData.json",
    "function": TowerFloorExcelConfigData
}, {
    "file": "TowerLevelExcelConfigData.json",
    "function": TowerLevelExcelConfigData
}, {
    "file": "TowerScheduleExcelConfigData.json",
    "function": TowerScheduleExcelConfigData
}, {
    "file": "WeaponCurveExcelConfigData.json",
    "function": WeaponCurveExcelConfigData
}, {
    "file": "WeaponLevelExcelConfigData.json",
    "function": WeaponLevelExcelConfigData
}, {
    "file": "WeaponPromoteExcelConfigData.json",
    "function": WeaponPromoteExcelConfigData
}, {
    "file": "WeatherExcelConfigData.json",
    "function": WeatherExcelConfigData
}, {
    "file": "WorldAreaConfigData.json",
    "function": WorldAreaConfigData
}, {
    "file": "WorldLevelExcelConfigData.json",
    "function": WorldLevelExcelConfigData
}]
