"""
Cardiac Autonomic Valsalva Ratio & Baroreflex Reactivity Client.
Zero-mock pure Python standard library implementation.
Calculates Valsalva Ratio (VR = max RR_Phase4 / min RR_Phase2),
Heart Rate Tachycardia/Bradycardia response, and autonomic neuropathy risk based on Ewing criteria.
"""

import math
from typing import Dict, Any, Optional


class ValsalvaRatioClient:
    """
    Evaluates parasympathetic cardiovagal and sympathetic baroreflex integrity via standardized Valsalva maneuver:
    - Strain: 40 mmHg for 15 seconds
    - Phase II: reflex tachycardia (shortest RR interval in ms, or highest HR in bpm)
    - Phase IV: reflex bradycardia post-release (longest RR interval in ms, or lowest HR in bpm)
    - Valsalva Ratio (VR): longest_rr_phase4_ms / shortest_rr_phase2_ms
    - Age-stratified autonomic classification based on Ewing battery standards
    """

    def __init__(self):
        pass

    def evaluate_valsalva_ratio(
        self,
        shortest_rr_phase2_ms: float,
        longest_rr_phase4_ms: float,
        patient_age_years: Optional[int] = 35,
        baseline_heart_rate_bpm: Optional[float] = 72.0,
        strain_duration_sec: Optional[float] = 15.0
    ) -> Dict[str, Any]:
        """
        Calculates Valsalva Ratio.
        shortest_rr_phase2_ms: minimum R-R interval during strain phase (typically 350 - 700 ms).
        longest_rr_phase4_ms: maximum R-R interval during post-strain overshoot (typically 700 - 1500 ms).
        patient_age_years: subject age in years (age attenuates normal VR).
        baseline_heart_rate_bpm: resting HR before maneuver (bpm).
        strain_duration_sec: duration of strain (typically 15s).
        """
        if shortest_rr_phase2_ms <= 0 or longest_rr_phase4_ms <= 0:
            raise ValueError("R-R interval durations must be strictly positive.")
        if longest_rr_phase4_ms < shortest_rr_phase2_ms:
            raise ValueError("Phase IV recovery R-R interval must be greater than Phase II strain R-R interval.")

        # Valsalva Ratio calculation
        valsalva_ratio = longest_rr_phase4_ms / shortest_rr_phase2_ms

        # Equivalent heart rates
        peak_hr_phase2_bpm = round(60000.0 / shortest_rr_phase2_ms, 1)
        nadir_hr_phase4_bpm = round(60000.0 / longest_rr_phase4_ms, 1)
        hr_swing_delta_bpm = round(peak_hr_phase2_bpm - nadir_hr_phase4_bpm, 1)

        # Age-adjusted normative threshold (Ewing & Clarke):
        # Age < 30: VR normal >= 1.45
        # Age 30 - 50: VR normal >= 1.35
        # Age 50 - 70: VR normal >= 1.25
        # Age > 70: VR normal >= 1.20
        age = patient_age_years if patient_age_years else 35
        if age < 30:
            norm_threshold = 1.45
            borderline_lower = 1.25
        elif age <= 50:
            norm_threshold = 1.35
            borderline_lower = 1.20
        elif age <= 70:
            norm_threshold = 1.25
            borderline_lower = 1.15
        else:
            norm_threshold = 1.20
            borderline_lower = 1.10

        # Clinical classification
        if valsalva_ratio >= norm_threshold:
            autonomic_grade = "Normal Cardiovagal & Sympathetic Baroreflex Integrity"
            pathology_risk = "Robust vagal modulation with intact adrenergic vasoconstrictive blood pressure recovery."
        elif valsalva_ratio >= borderline_lower:
            autonomic_grade = "Borderline Autonomic Function"
            pathology_risk = "Mildly blunted baroreflex response; recommend postural orthostatic and deep breathing tests."
        else:
            autonomic_grade = "Abnormal / Cardiovascular Autonomic Neuropathy (CAN)"
            pathology_risk = "Significant cardiovagal denervation or adrenergic failure; failure to evoke reflex bradycardia following hemodynamic overshoot."

        return {
            "status": "success",
            "valsalva_indices": {
                "valsalva_ratio": round(valsalva_ratio, 3),
                "age_adjusted_normal_threshold": norm_threshold,
                "shortest_rr_phase2_ms": round(shortest_rr_phase2_ms, 1),
                "longest_rr_phase4_ms": round(longest_rr_phase4_ms, 1)
            },
            "hemodynamic_metrics": {
                "peak_heart_rate_phase2_bpm": peak_hr_phase2_bpm,
                "nadir_heart_rate_phase4_bpm": nadir_hr_phase4_bpm,
                "heart_rate_swing_bpm": hr_swing_delta_bpm,
                "baseline_heart_rate_bpm": baseline_heart_rate_bpm,
                "strain_duration_sec": strain_duration_sec
            },
            "autonomic_assessment": {
                "autonomic_grade": autonomic_grade,
                "pathology_risk": pathology_risk
            }
        }
