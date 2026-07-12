import json

exam_results = [
    {"student_name": "Анна", "score": 91},
    {"student_name": "Богдан", "score": 58},
    {"student_name": "Вікторія", "score": 75},
    {"student_name": "Григорій", "score": 45}
]
passing_score = 60 # Прохідний бал

def final_result(exam_result):
    for exam in exam_result:
        if exam["score"] >= passing_score:
            exam["passed"] = True
        else:
            exam["passed"] = False
    return exam_result
print(json.dumps(final_result(exam_results), indent=2, ensure_ascii=False))