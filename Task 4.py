import json

employees = [
    {"name": "Олена", "department": "Marketing", "salary":
25000},
    {"name": "Ігор", "department": "IT", "salary": 55000},
    {"name": "Наталія", "department": "Marketing", "salary":
28000},
    {"name": "Олег", "department": "HR", "salary": 22000},
    {"name": "Андрій", "department": "IT", "salary": 48000},
    {"name": "Марія", "department": "IT", "salary": 52000},
]

def get_department_stats(employee_list, target_debt):
    department_stats = []
    count = 0
    for employee in employee_list:
        if employee["department"] == target_debt:
            department_stats.append(employee)
            count += 1

    total_salary = 0
    average_salary = 0
    for department in department_stats:
        total_salary += department["salary"]
        average_salary = total_salary / count

    return {
        "department": target_debt,
        "average_salary": average_salary,
        "top_earner": max(department_stats, key=lambda x: x["salary"])["name"],
        "count": count
    }

result1 = get_department_stats(employees, "Marketing")
print(json.dumps(result1, indent=2, ensure_ascii=False))

result2 = get_department_stats(employees, "IT")
print(json.dumps(result2, indent=2, ensure_ascii=False))


