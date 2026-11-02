# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Postprandial Somnolence Glycemic Dip Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentPostprandialSomnolenceGlycemicDip

mcp = FastMCP("PersonalAgentPostprandialSomnolenceGlycemicDip")
client = PersonalAgentPostprandialSomnolenceGlycemicDip()

@mcp.tool()
def evaluate_meal_somnolence_risk(
    carbohydrate_grams: float = 85.0,
    glycemic_index: float = 72.0,
    protein_grams: float = 30.0,
    fat_grams: float = 25.0,
    meal_calories: float = 685.0
) -> str:
    """Calculates Glycemic Load (GL), Postprandial Somnolence Index (PSI: 0-100), and orexin suppression."""
    import json
    return json.dumps(client.evaluate_meal_somnolence_risk(
        carbohydrate_grams, glycemic_index, protein_grams, fat_grams, meal_calories
    ), indent=2)

@mcp.tool()
def prescribe_postprandial_countermeasure(
    psi_score: float = 65.0,
    meal_time_24h: float = 12.5
) -> str:
    """Prescribes GLUT4 glucose-clearing walking timing and duration post-meal."""
    import json
    return json.dumps(client.prescribe_postprandial_countermeasure(
        psi_score, meal_time_24h
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
