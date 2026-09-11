import math

def evaluate_shadow(production_log, shadow_log, criteria):
    n = len(production_log)
    production_accuracy = sum(row["prediction"] == row["actual"] for row in production_log) / n
    shadow_accuracy = sum(row["prediction"] == row["actual"] for row in shadow_log) / n
    accuracy_gain = shadow_accuracy - production_accuracy
    latencies = sorted(row["latency_ms"] for row in shadow_log)
    shadow_latency_p95 = latencies[math.ceil(0.95 * n) - 1]
    agreement_rate = sum(a["prediction"] == b["prediction"] for a, b in zip(production_log, shadow_log)) / n
    promote = accuracy_gain >= criteria["min_accuracy_gain"] and shadow_latency_p95 <= criteria["max_latency_p95"] and agreement_rate >= criteria["min_agreement_rate"]
    return {"promote": promote, "metrics": {"shadow_accuracy": shadow_accuracy, "production_accuracy": production_accuracy, "accuracy_gain": accuracy_gain, "shadow_latency_p95": shadow_latency_p95, "agreement_rate": agreement_rate}}
