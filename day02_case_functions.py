cases = [
    {"id": "T001", "model": "A", "passed": True, "latency_ms": 1200},
    {"id": "T002", "model": "A", "passed": False, "latency_ms": 800},
    {"id": "T003", "model": "B", "passed": True, "latency_ms": 2500},
    {"id": "T004", "model": "B", "passed": False, "latency_ms": 3000},
    {"id": "T005", "model": "A", "passed": True, "latency_ms": 2000},
]
#自己的答案
# passed_count = 0
# passed_latency = 0
# failed_latency = 0
# modelA_count = 0
# modelA_latency = 0
# modelA_passed_count = 0
# failed_case_ids = []
# timeout_case_ids = []

# for case in cases:
#     case_id = case["id"]
#     model = case["model"]
#     passed = case["passed"]
#     latency_ms = case["latency_ms"]


#     if passed:
#         passed_latency += latency_ms
#         passed_count += 1

#     else:
#         failed_latency += latency_ms
#         failed_case_ids.append(case_id)

#     if latency_ms > 2000:
#         timeout_case_ids.append(case_id)

#     if model == "A":
#         modelA_count += 1
#         modelA_latency += latency_ms
#         if passed:
#             modelA_passed_count += 1



# print(f"Total_cases:{len(cases)},passed_rate:{passed_count/len(cases):.2%},"+
#       f"latency_avg:{(passed_latency+failed_latency)/len(cases):.2f}ms,"+
#       f"failed_case_ids:{failed_case_ids},timeout_case_ids:{timeout_case_ids},"+
#       f"modelA_count:{modelA_count},modelA_passed_count:{modelA_passed_count},modelA_latency_avg:{modelA_latency/modelA_count:.2f}ms")

# 正确答案
# threshold_ms = 2000

# passed_count = 0
# total_latency = 0
# failed_case_ids = []
# timeout_case_ids = []

# modelA_count = 0
# modelA_passed_count = 0
# modelA_latency = 0

# for case in cases:
#     case_id = case["id"]
#     model =case["model"]
#     passed =case["passed"]
#     latency_ms = case["latency_ms"]

#     # 全部用例统计
#     total_latency += latency_ms
#     if passed:
#         passed_count += 1
#     else:
#         failed_case_ids.append(case_id)
#     if latency_ms > threshold_ms:
#         timeout_case_ids.append(case_id)

#     # model A 统计
#     if model == "A":
#         modelA_count += 1
#         modelA_latency += latency_ms
#         if passed:
#             modelA_passed_count += 1

# total_count = len(cases)

# print(
#     f"总数：{total_count}\n"
#     f"通过数：{passed_count}\n"
#     f"通过率：{passed_count/total_count:.2%}\n"
#     f"平均延迟：{total_latency/total_count:.2f}ms\n"
#     f"失败用例：{failed_case_ids}\n"
#     f"超时用例：{timeout_case_ids}\n"
#     f"模型 A 总数：{modelA_count}\n"
#     f"模型 A 通过数：{modelA_passed_count}\n"
#     f"模型 A 平均延迟：{modelA_latency/modelA_count:.2f}ms"
# )

# def add(a, b):
#     total = a + b
#     return total

# answer = add(2,3)
# print(answer)

# def add(a,b):
#     print(a+b)

# value = add(2,3)
# print(value)  

# def show_sum(a,b):
#     return a + b

# value = show_sum(2,3)
# print(value)

# def is_slow(latency_ms, threshold_ms=2000):
#     slow = latency_ms > threshold_ms
#     return slow

# result1 = is_slow(2000)
# result2 = is_slow(2001)
# result3 = is_slow(2000,1500)
# print(result1)
# print(result2)
# print(result3)


def evaluate_case(case, threshold_ms=2000):
    slow = case["latency_ms"] > threshold_ms
    case["slow"] = slow
    return case

# case = {"id": "T001", "model": "A", "passed": True, "latency_ms": 2001}
# case = evaluate_case(case)
# print(case)

test_cases = [
    {"id": "S001", "model": "A", "passed": True, "latency_ms": 1999},
    {"id": "S002", "model": "A", "passed": True, "latency_ms": 2000},
    {"id": "S003", "model": "A", "passed": True, "latency_ms": 2001},
    {"id": "S004", "model": "A", "passed": False, "latency_ms": 1999},
    {"id": "S005", "model": "A", "passed": False, "latency_ms": 2000},
    {"id": "S006", "model": "A", "passed": False, "latency_ms": 2001}
]
passed = 0
slow = 0
passed_slow = 0
sum = len(test_cases)
threshold_ms = 2001

for case in test_cases:
    result = evaluate_case(case,threshold_ms)
    if result["passed"]:
        passed += 1
        if result["slow"]:
                passed_slow += 1
    if result["slow"]:
        slow += 1
    

print(f"Threshold_ms: {threshold_ms}, Sum: {sum}, Passed: {passed}, Slow: {slow}, Passed_Slow: {passed_slow}")
