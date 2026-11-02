# -*- coding: utf-8 -*-
"""Personal Agent Postprandial Somnolence Glycemic Dip Skill.

Zero-dependency postprandial somnolence modeler, lateral hypothalamic orexin suppression indexer,
and post-meal glucose clearing ambulation scheduler.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentPostprandialSomnolenceGlycemicDip:
    """Quantitative postprandial somnolence and neuro-metabolic fatigue engine based on
    glycemic load, orexinergic neuron hyperpolarization, and splanchnic hemodynamic shift models."""

    def evaluate_meal_somnolence_risk(
        self,
        carbohydrate_grams: float = 85.0,
        glycemic_index: float = 72.0,
        protein_grams: float = 30.0,
        fat_grams: float = 25.0,
        meal_calories: float = 685.0
    ) -> Dict[str, Any]:
        """Calculates Glycemic Load (GL), lateral hypothalamic Orexin Suppression Index (OSI),
        splanchnic vascular diversion burden, and Postprandial Somnolence Index (PSI: 0-100)."""
        cho = max(0.0, float(carbohydrate_grams))
        gi = max(10.0, min(100.0, float(glycemic_index)))
        pro = max(0.0, float(protein_grams))
        fat = max(0.0, float(fat_grams))
        cals = max(50.0, float(meal_calories))

        # Glycemic Load: GL = (CHO * GI) / 100
        gl = round((cho * gi) / 100.0, 1)

        # 1. Glycemic Reactive Crash Component (rapid insulin surge -> reactive hypoglycemia risk)
        gl_factor = min(40.0, (gl / 45.0) * 35.0)

        # 2. Splanchnic Hemodynamic Burden (parasympathetic mesenteric blood diversion)
        # Driven by high total calories and fat density
        caloric_load = min(30.0, (cals / 900.0) * 25.0) + min(15.0, (fat / 40.0) * 12.0)

        # 3. Lateral Hypothalamic Orexinergic Suppression (glucose & tryptophan-induced serotonin)
        # Orexin neurons fire rapidly during fasting/mild hypoglycemia; silenced by glucose spikes
        orexin_suppression_pct = round(min(95.0, (gl * 1.4) + (cho * 0.3)), 1)

        # Total Postprandial Somnolence Index (PSI: 0 - 100)
        psi_raw = gl_factor + caloric_load + (orexin_suppression_pct * 0.25)
        psi = min(100.0, round(max(5.0, psi_raw), 1))

        if psi < 35.0:
            tier = "Low Somnolence / Alertness Intact"
            cognitive_impact = "Prefrontal executive function maintained; minimal alertness dip"
        elif psi < 60.0:
            tier = "Mild-to-Moderate Somnolence"
            cognitive_impact = "Slight working memory latency; ideal for routine administrative tasks"
        elif psi < 80.0:
            tier = "High Postprandial Somnolence"
            cognitive_impact = "Significant cognitive fog, reaction time deceleration, micro-sleep vulnerability"
        else:
            tier = "Severe Postprandial Food Coma"
            cognitive_impact = "Acute executive function collapse; profound orexin neuron silencing"

        return {
            "meal_glycemic_load": gl,
            "meal_caloric_density_kcal": cals,
            "postprandial_somnolence_index_psi": psi,
            "somnolence_severity_tier": tier,
            "orexin_neuron_suppression_pct": f"{orexin_suppression_pct}%",
            "splanchnic_blood_diversion_burden": round(caloric_load, 1),
            "expected_onset_minutes_post_meal": 35,
            "duration_of_somnolence_minutes": int(min(120, max(20, psi * 1.2))),
            "cognitive_performance_impact": cognitive_impact
        }

    def prescribe_postprandial_countermeasure(
        self,
        psi_score: float,
        meal_time_24h: float = 12.5
    ) -> Dict[str, Any]:
        """Prescribes non-insulin dependent glucose disposal protocol and chronobiological timing."""
        psi = max(0.0, min(100.0, float(psi_score)))
        m_time = meal_time_24h % 24.0

        def _fmt(h_float: float) -> str:
            h = int(h_float) % 24
            m = int(round((h_float - int(h_float)) * 60))
            if m >= 60:
                h = (h + 1) % 24
                m = 0
            return f"{h:02d}:{m:02d}"

        walk_start = (m_time + 0.33) % 24.0  # T+20 minutes
        walk_duration = 15 if psi < 60.0 else 25

        return {
            "evaluated_psi_score": psi,
            "prescribed_ambulation_window": f"{_fmt(walk_start)} (T+20 min post-meal)",
            "ambulation_duration_minutes": walk_duration,
            "exercise_modality": "Zone 1 light brisk walking (flat terrain, nasal breathing)",
            "glucose_clearance_mechanism": "Stimulates skeletal muscle GLUT4 translocation independent of insulin, flattening glycemic spike by ~30-40%.",
            "postural_mandate": "Avoid sitting or recumbency for at least 45 minutes post-ingestion.",
            "caffeine_timing_rule": "Delay caffeine consumption until 60 minutes post-meal to allow gastric clearance."
        }
