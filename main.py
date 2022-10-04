import os
import sys
import json
from rich.progress import track
from rich.console import Console

from res.excels.NpcExcelConfigData import NpcExcelConfigData
from res.excels.QuestExcelConfigData import QuestExcelConfigData
from res.excels.GadgetExcelConfigData import GadgetExcelConfigData
from res.excels.GatherExcelConfigData import GatherExcelConfigData
from res.excels.AvatarExcelConfigData import AvatarExcelConfigData
from res.excels.WeaponExcelConfigData import WeaponExcelConfigData
from res.excels.RewardExcelConfigData import RewardExcelConfigData
from res.excels.DailyDungeonConfigData import DailyDungeonConfigData
from res.excels.ChapterExcelConfigData import ChapterExcelConfigData
from res.excels.CombineExcelConfigData import CombineExcelConfigData
from res.excels.MonsterExcelConfigData import MonsterExcelConfigData
from res.excels.MaterialExcelConfigData import MaterialExcelConfigData
from res.excels.CookBonusExcelConfigData import CookBonusExcelConfigData
from res.excels.ReliquaryExcelConfigData import ReliquaryExcelConfigData
from res.excels.CookRecipeExcelConfigData import CookRecipeExcelConfigData
from res.excels.EquipAffixExcelConfigData import EquipAffixExcelConfigData
from res.excels.ProudSkillExcelConfigData import ProudSkillExcelConfigData
from res.excels.QuestCodexExcelConfigData import QuestCodexExcelConfigData
from res.excels.AnimalCodexExcelConfigData import AnimalCodexExcelConfigData
from res.excels.AvatarLevelExcelConfigData import AvatarLevelExcelConfigData
from res.excels.NewActivityExcelConfigData import NewActivityExcelConfigData
from res.excels.PlayerLevelExcelConfigData import PlayerLevelExcelConfigData
from res.excels.AvatarCurveExcelConfigData import AvatarCurveExcelConfigData
from res.excels.AvatarSkillExcelConfigData import AvatarSkillExcelConfigData
from res.excels.WeaponCodexExcelConfigData import WeaponCodexExcelConfigData
from res.excels.AvatarTalentExcelConfigData import AvatarTalentExcelConfigData
from res.excels.MonsterCurveExcelConfigData import MonsterCurveExcelConfigData
from res.excels.PersonalLineExcelConfigData import PersonalLineExcelConfigData
from res.excels.ReliquarySetExcelConfigData import ReliquarySetExcelConfigData
from res.excels.AvatarCostumeExcelConfigData import AvatarCostumeExcelConfigData
from res.excels.AvatarPromoteExcelConfigData import AvatarPromoteExcelConfigData
from res.excels.MaterialCodexExcelConfigData import MaterialCodexExcelConfigData
from res.excels.RewardPreviewExcelConfigData import RewardPreviewExcelConfigData
from res.excels.AvatarFlycloakExcelConfigData import AvatarFlycloakExcelConfigData
from res.excels.ReliquaryAffixExcelConfigData import ReliquaryAffixExcelConfigData
from res.excels.ReliquaryCodexExcelConfigData import ReliquaryCodexExcelConfigData
from res.excels.ReliquaryLevelExcelConfigData import ReliquaryLevelExcelConfigData
from res.excels.MonsterDescribeExcelConfigData import MonsterDescribeExcelConfigData
from res.excels.AvatarSkillDepotExcelConfigData import AvatarSkillDepotExcelConfigData
from res.excels.ReliquaryMainPropExcelConfigData import ReliquaryMainPropExcelConfigData
from res.excels.AvatarFettersLevelExcelConfigData import AvatarFettersLevelExcelConfigData


console = Console()

console.print("[green]仅包含当前 Grasscutter 含有的字段。[/green]")
console.print("[green]正在读取配置文件...[/green]")

try:
    with open("./config.json", "r", encoding = "utf-8") as f:
        config = json.load(f)
except:
    console.print("[red]配置文件读取失败！[/red]")
    sys.exit(1)

os.makedirs(config["output"], exist_ok = True)

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
}]

console.print("[green]正在转换...[/green]")

for convertConfig in convertMap:
    inputFilePath = os.path.join(config["resPath"], convertConfig["file"])
    outputFilePath = os.path.join(config["output"], convertConfig["file"])
    with open(inputFilePath, "r", encoding = "utf-8") as fr:
        data = json.load(fr)
        configData = []
        for single in track(data, description = convertConfig["file"]):
            configData.append(convertConfig["function"](single))
        with open(outputFilePath, "w", encoding = "utf-8") as fw:
            json.dump(configData, fw, ensure_ascii = False, sort_keys = True, indent = 4)

console.print("[yellow]转换结束！[/yellow]")
