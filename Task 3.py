exam_results = [
    {"student_name": "Анна", "score": 91},
    {"student_name": "Богдан", "score": 58},
    {"student_name": "Вікторія", "score": 75},
    {"student_name": "Григорій", "score": 45}
]
passing_score = 60 # Прохідний бал

for exam in exam_results:
    if exam["score"] >= passing_score:
        exam["passed"] = True
    else:
        exam["passed"] = False

print(exam_results)