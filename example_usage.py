"""
Example usage of Cardiac Autonomic Valsalva Ratio Skill.
Demonstrates normal cardiovagal response vs diabetic cardiovascular autonomic neuropathy (CAN).
"""

import json
from client import ValsalvaRatioClient


def main():
    print("=== Testing Cardiac Autonomic Valsalva Ratio Skill ===")
    client = ValsalvaRatioClient()

    # 1. Healthy young adult subject (Shortest RR Phase 2 = 520 ms [115 bpm], Longest RR Phase 4 = 920 ms [65 bpm] -> VR = 1.77 > 1.45)
    res_normal = client.evaluate_valsalva_ratio(
        shortest_rr_phase2_ms=520.0,
        longest_rr_phase4_ms=920.0,
        patient_age_years=29,
        baseline_heart_rate_bpm=74.0
    )
    print("\n[Case 1: Normal Cardiovagal & Baroreflex Integrity]")
    print(json.dumps(res_normal, indent=2))

    # 2. Patient with diabetic cardiovascular autonomic neuropathy (Fixed heart rate, minimal vagal bradycardia: Phase 2 RR = 660 ms [91 bpm], Phase 4 RR = 740 ms [81 bpm] -> VR = 1.12 < 1.20)
    res_neuropathy = client.evaluate_valsalva_ratio(
        shortest_rr_phase2_ms=660.0,
        longest_rr_phase4_ms=740.0,
        patient_age_years=58,
        baseline_heart_rate_bpm=86.0
    )
    print("\n[Case 2: Diabetic Cardiovascular Autonomic Neuropathy (CAN)]")
    print(json.dumps(res_neuropathy, indent=2))

    # Assertions
    assert res_normal["valsalva_indices"]["valsalva_ratio"] > 1.45
    assert "Normal" in res_normal["autonomic_assessment"]["autonomic_grade"]
    assert res_neuropathy["valsalva_indices"]["valsalva_ratio"] < 1.20
    assert "Abnormal" in res_neuropathy["autonomic_assessment"]["autonomic_grade"]
    print("\n[SUCCESS] Valsalva Ratio tests passed!")


if __name__ == "__main__":
    main()
