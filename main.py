import os
import sys
import json
import convert
from rich.progress import track
from rich.console import Console


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



console.print("[green]正在转换...[/green]")

for convertConfig in convert.convertMap:
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
