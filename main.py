import os
import sys
import json
from rich.progress import track
from rich.console import Console
from res.excels.AvatarExcelConfigData import AvatarExcelConfigData
from res.excels.AvatarLevelExcelConfigData import AvatarLevelExcelConfigData
from res.excels.NewActivityExcelConfigData import NewActivityExcelConfigData
from res.excels.AvatarCurveExcelConfigData import AvatarCurveExcelConfigData
from res.excels.AvatarCostumeExcelConfigData import AvatarCostumeExcelConfigData
from res.excels.AvatarFlycloakExcelConfigData import AvatarFlycloakExcelConfigData
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
