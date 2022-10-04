def AvatarSkillDepotExcelConfigData(config):
    newConfig = {
        "id": config["id"],
        "skills": config["skills"],
        "subSkills": [],
        "extraAbilities": config["extraAbilities"],
        "talents": config["talents"],
        "inherentProudSkillOpens": config["inherentProudSkillOpens"],
        "talentStarName": "",
        "skillDepotAbilityGroup": ""
    }

    if "energySkill" in config:
        newConfig["energySkill"] = config["energySkill"]

    if "attackModeSkill" in config:
        newConfig["attackModeSkill"] = config["attackModeSkill"]

    if "subSkills" in config:
        newConfig["subSkills"] = config["subSkills"]

    if "skillDepotAbilityGroup" in config:
        newConfig["skillDepotAbilityGroup"] = config["skillDepotAbilityGroup"]

    if "talentStarName" in config:
        newConfig["talentStarName"] = config["talentStarName"]

    return newConfig
