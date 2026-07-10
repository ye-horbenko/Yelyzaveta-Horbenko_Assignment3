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

    total_salary = sum(employee["salary"] for employee in employee_list)
    average_salary = total_salary / len(employee_list)
    top_earner = max(employee["salary"] for employee in employee_list)

    return {
        "department": target_debt,
        "average_salary": average_salary,
        "top_earner": top_earner["name"],
        "count": count,
    }

result1 = get_department_stats(employees, "Marketing")
print(result1)

result2 = get_department_stats(employees, "IT")
print(result2)


