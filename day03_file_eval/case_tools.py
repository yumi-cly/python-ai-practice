def evaluate_case(case, threshold_ms=2000):
    slow = case["latency_ms"] > threshold_ms
    case["slow"] = slow
    return case

def summarize(results):
    total_count = len(results)
    passed_count = 0
    slow_count = 0
    passed_slow_count = 0
    total_latency_ms = 0

    for result in results:
        total_latency_ms += result["latency_ms"]
        if result["passed"]:
            passed_count += 1
            if result["slow"]:
                passed_slow_count += 1
        if result["slow"]:
            slow_count += 1
    failed_count = total_count - passed_count
    if total_count > 0:
        pass_rate = passed_count / total_count
        average_latency_ms = total_latency_ms / total_count
    else:
        pass_rate = None
        average_latency_ms = None

    return {
        "total_count": total_count,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "slow_count": slow_count,
        "passed_slow_count": passed_slow_count,
        "pass_rate": pass_rate,
        "average_latency_ms": average_latency_ms
    }