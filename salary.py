import employee
import attendance

def calculate_salary():
    emp_id = int(input("Enter Employee ID: "))
    emp = employee.search_by_id(emp_id)
    if emp:
        print(f"Employee Name: {emp['name']}")
        print(f"Position: {emp['position']}")
        print(f"Department: {emp['department']}")
        print(f"Base Salary: ${emp['salary']}")
    else:
        print("Employee not found.")

# employees = {
#      1: {
#         "name": "Afshan Tayyab",
#         "position": "Software Engineer",
#         "base_salary": 50000
#     }
# }
 
# attendance = {
#       1: {
#         "2025-11-01": {"status": "Present", "hours": 8},
#         "2025-11-02": {"status": "Present", "hours": 8},
#         "2025-11-03": {"status": "Absent", "hours": 0},
#         "2025-11-04": {"status": "Present", "hours": 8}
#     }
# }
 
# def calculate_salary(emp_id, month):
 
#     if emp_id not in employees:
#         print("Error: Employee not found.")
#         return
 
#     employee = employees[emp_id]
 
#     if emp_id not in attendance:
#         print("No attendance records found.")
#         return
 
#     total_days = 0
#     present_days = 0
#     total_hours = 0
 
#     for date, record in attendance[emp_id].items():
#         if month in date:   # Example: 2025-11
#             total_days += 1
 
#             if record["status"] == "Present":
#                 present_days += 1
#                 total_hours += record["hours"]
 
#     if total_days == 0:
#         print("No attendance.")
#         return
 
#     base_salary = employee["base_salary"]
 
#     deduction_per_day = base_salary / 26
#     deductions = (26 - present_days) * deduction_per_day
 
#     if present_days == 28:
#         bonus = 4000
#     else:
#         bonus = 0
 
#     net_pay = base_salary + bonus - deductions
 
#     print("\n=== PAYROLL SUMMARY ===")
#     print(f"Employee: {employee['name']} ({emp_id})")
#     print(f"Position: {employee['position']}")
#     print(f"Month: {month}")
#     print(f"Days Present: {present_days}/28")
#     print(f"Total Hours: {total_hours}")
#     print(f"Base Salary: {base_salary}")
#     print(f"Bonus: {bonus}")
#     print(f"Deductions: {deductions}")
#     print(f"Net Pay: {net_pay}")
 
# calculate_salary("E108", "2025-11")
