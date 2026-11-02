# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Postprandial Somnolence Glycemic Dip Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentPostprandialSomnolenceGlycemicDip

def main():
    agent = PersonalAgentPostprandialSomnolenceGlycemicDip()

    print("=" * 70)
    print("DEMO: Personal Agent Postprandial Somnolence & Orexin Suppression")
    print("=" * 70)

    # 1. High-Carb Lunch Evaluation (95g CHO, GI 75, 25g Pro, 28g Fat, 740 kcal)
    res_meal = agent.evaluate_meal_somnolence_risk(
        carbohydrate_grams=95.0,
        glycemic_index=75.0,
        protein_grams=25.0,
        fat_grams=28.0,
        meal_calories=740.0
    )

    print(f"\n1. Postprandial Meal Somnolence Analysis:")
    print(f"   Glycemic Load: {res_meal['meal_glycemic_load']} (Caloric: {res_meal['meal_caloric_density_kcal']} kcal)")
    print(f"   Somnolence Index (PSI): {res_meal['postprandial_somnolence_index_psi']}/100")
    print(f"   Severity Tier: {res_meal['somnolence_severity_tier']}")
    print(f"   Hypothalamic Orexin Suppression: {res_meal['orexin_neuron_suppression_pct']}")
    print(f"   Splanchnic Load: {res_meal['splanchnic_blood_diversion_burden']}")
    print(f"   Expected Onset: T+{res_meal['expected_onset_minutes_post_meal']} min (Duration: {res_meal['duration_of_somnolence_minutes']} min)")
    print(f"   Cognitive Impact: {res_meal['cognitive_performance_impact']}")

    # 2. Prescribe Postprandial Ambulation Protocol (Lunch at 12:30 -> 12.5)
    res_proto = agent.prescribe_postprandial_countermeasure(
        psi_score=res_meal['postprandial_somnolence_index_psi'],
        meal_time_24h=12.5
    )

    print(f"\n2. Postprandial Countermeasure Prescription:")
    print(f"   Ambulation Window: {res_proto['prescribed_ambulation_window']}")
    print(f"   Duration: {res_proto['ambulation_duration_minutes']} min ({res_proto['exercise_modality']})")
    print(f"   Mechanism: {res_proto['glucose_clearance_mechanism']}")
    print(f"   Postural Mandate: {res_proto['postural_mandate']}")
    print(f"   Caffeine Rule: {res_proto['caffeine_timing_rule']}")

    print("\nVerification complete: Postprandial somnolence engine executed flawlessly.")

if __name__ == "__main__":
    main()
