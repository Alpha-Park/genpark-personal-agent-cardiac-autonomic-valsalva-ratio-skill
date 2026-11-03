# Cardiac Autonomic Valsalva Ratio Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Valsalva Ratio (longest RR in Phase IV / shortest RR in Phase II) to evaluate cardiovagal and adrenergic baroreflex integrity using Ewing diagnostic criteria.

## Architecture

```mermaid
flowchart TD
    A[40 mmHg Valsalva Strain 15s] --> B[Phase II Tachycardia: Measure Shortest RR ms]
    B --> C[Phase IV Post-Release Bradycardia: Measure Longest RR ms]
    C --> D[Compute Valsalva Ratio = RR_max / RR_min]
    D --> E[Apply Age-Adjusted Ewing Diagnostic Thresholds]
    E --> F[Classify Normal vs Cardiovascular Autonomic Neuropathy]
```

## Quickstart

```python
from client import ValsalvaRatioClient

client = ValsalvaRatioClient()
result = client.evaluate_valsalva_ratio(
    shortest_rr_phase2_ms=520.0,
    longest_rr_phase4_ms=920.0,
    patient_age_years=29
)
print(result)
```

## License

Apache-2.0
