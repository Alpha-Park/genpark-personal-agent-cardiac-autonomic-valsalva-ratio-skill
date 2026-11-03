---
name: genpark-personal-agent-cardiac-autonomic-valsalva-ratio-skill
version: 1.0.0
description: Calculates Valsalva Ratio (longest RR in Phase IV / shortest RR in Phase II) and evaluates cardiovagal and adrenergic baroreflex integrity using Ewing diagnostic criteria.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - cardiology
  - autonomic
  - valsalva-ratio
  - baroreflex
  - zero-dependency
---

# Cardiac Autonomic Valsalva Ratio Skill

## Mathematical Formulation

Standard Valsalva maneuver ($40\text{ mmHg}$ strain for $15\text{ seconds}$):

$$\text{Valsalva Ratio} = \frac{\text{Longest R-R interval in Phase IV}}{\text{Shortest R-R interval in Phase II}} = \frac{\text{RR}_{\max,\text{Phase IV}}}{\text{RR}_{\min,\text{Phase II}}}$$

Equivalent instantaneous heart rate swing:

$$\text{HR}_{\max,\text{Phase II}} = \frac{60000}{\text{RR}_{\min,\text{Phase II}}} \quad (\text{bpm})$$
$$\text{HR}_{\min,\text{Phase IV}} = \frac{60000}{\text{RR}_{\max,\text{Phase IV}}} \quad (\text{bpm})$$
$$\Delta \text{HR} = \text{HR}_{\max,\text{Phase II}} - \text{HR}_{\min,\text{Phase IV}}$$

## Ewing Diagnostic Criteria
- **Normal**: $\text{VR} \ge 1.40$ (young adults $\ge 1.45$, older adults $\ge 1.25$) — preserved cardiovagal reflex bradycardia
- **Borderline**: $1.21 \le \text{VR} < 1.40$
- **Abnormal (Cardiovascular Autonomic Neuropathy)**: $\text{VR} \le 1.20$ — loss of reflex vagal braking and blunted baroreflex sensitivity
