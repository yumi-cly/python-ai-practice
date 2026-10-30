case_id = "T001"
model ="A"
passed = False
latency_ms = 1999

# # 任务一
# print(type(passed))
# print(type(latency_ms))

# # 任务二
# if passed:
#     print(f"Case {case_id} passed for model {model} with latency {latency_ms} ms.")
# else:
#     print(f"Case {case_id} failed for model {model} with latency {latency_ms} ms.")

# # 任务三
# if latency_ms >2000:
#     print(f"Warning: Case {case_id} has high latency of {latency_ms} ms for model {model}.")
# else:
#     print(f"Case {case_id} has acceptable latency of {latency_ms} ms for model {model}.")

# 任务四
if passed:
    if latency_ms <=2000:
        print(f"Case {case_id} passed with acceptable latency for model {model}.")
    else:
        print(f"Case {case_id} passed but with high latency for model {model}.")
else:
    if latency_ms <=2000:
        print(f"Case {case_id} failed but with acceptable latency for model {model}.")
    else:
        print(f"Case {case_id} failed and has high latency for model {model}.")

