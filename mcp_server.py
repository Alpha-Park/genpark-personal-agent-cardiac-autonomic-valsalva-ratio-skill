"""
MCP Server for Cardiac Autonomic Valsalva Ratio Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import ValsalvaRatioClient


def main():
    client = ValsalvaRatioClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_valsalva_ratio",
                            "description": "Calculates Valsalva Ratio (longest RR in Phase IV / shortest RR in Phase II) and evaluates cardiovagal and adrenergic baroreflex integrity using Ewing diagnostic criteria.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "shortest_rr_phase2_ms": {
                                        "type": "number",
                                        "description": "Shortest R-R interval during Phase II strain in milliseconds."
                                    },
                                    "longest_rr_phase4_ms": {
                                        "type": "number",
                                        "description": "Longest R-R interval during Phase IV post-release in milliseconds."
                                    },
                                    "patient_age_years": {
                                        "type": "integer",
                                        "description": "Patient age in years (optional)."
                                    },
                                    "baseline_heart_rate_bpm": {
                                        "type": "number",
                                        "description": "Resting baseline heart rate in bpm (default: 72.0)."
                                    },
                                    "strain_duration_sec": {
                                        "type": "number",
                                        "description": "Duration of 40 mmHg strain in seconds (default: 15.0)."
                                    }
                                },
                                "required": [
                                    "shortest_rr_phase2_ms",
                                    "longest_rr_phase4_ms"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_valsalva_ratio":
                try:
                    out = client.evaluate_valsalva_ratio(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
