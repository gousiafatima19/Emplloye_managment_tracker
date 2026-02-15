# attendance = {
#     "E001": [
#         {"date": "2025-10-01", "status": "Present", "hours": 8},
#         {"date": "2025-10-02", "status": "Present", "hours": 7},
#         {"date": "2025-10-03", "status": "Absent", "hours": 0}
#     ],
#     "E002": [
#         {"date": "2025-10-01", "status": "Present", "hours": 8},
#         {"date": "2025-10-02", "status": "Present", "hours": 8}
#     ],
#     "E003": [
#         {"date": "2025-10-01", "status": "Absent", "hours": 0},
#         {"date": "2025-10-02", "status": "Present", "hours": 6}
#     ]
# }
# def mark_attendance():
#     emp_id = input("Enter Employee ID: ")
#     date = input("Enter Date (YYYY-MM-DD): ")
#     status = input("Enter Attendance Status (Present/Absent): ")
#     hours = int(input("Enter Working Hours (if Present): ")) if status.lower() == "present" else 0
    
#     if emp_id in attendance:
#         attendance[emp_id].append({"date": date, "status": status, "hours": hours})
#     else:
#         attendance[emp_id] = [{"date": date, "status": status, "hours": hours}]
    
#     print("Attendance marked successfully.")
# def record_working_hours():
#     emp_id = input("Enter Employee ID: ")
#     date = input("Enter Date (YYYY-MM-DD): ")
#     hours = int(input("Enter Working Hours: "))
    
#     if emp_id in attendance:
#         for record in attendance[emp_id]:
#             if record["date"] == date:
#                 record["hours"] = hours
#                 print("Working hours updated successfully.")
#                 return
#         attendance[emp_id].append({"date": date, "status": "Present", "hours": hours})
#         print("Working hours recorded successfully.")
#     else:
#         attendance[emp_id] = [{"date": date, "status": "Present", "hours": hours}]
#         print("Working hours recorded successfully.")
# def view_attendance_report():
#     emp_id = input("Enter Employee ID: ")
#     if emp_id in attendance:
#         print(f"Attendance Report for Employee ID: {emp_id}")
#         for record in attendance[emp_id]:
#             print(f"Date: {record['date']}, Status: {record['status']}, Hours: {record['hours']}")
#     else:
#         print("No attendance records found for this employee.")
attendance={}
def mark_attendance(emp_id,date,status):
    if emp_id not in attendance:
        attendance[emp_id] = {}
    if date in attendance[emp_id]:
        print("Attendance already marked")
        return
    attendance[emp_id][date] = status
    print("Attendance Marked")
 
work_hours={}
def record_work_hours(emp_id, date, hours):
    if hours <= 0:
        print("Invalid working hours")
        return
    if emp_id not in work_hours:
        work_hours[emp_id] = {}
    if date in work_hours[emp_id]:
        print("Working hours already recorded for this date")
        return
    work_hours[emp_id][date] = hours
    print("Working hours recorded successfully")
 
def monthly_attendance(emp_id,month):
    if emp_id not in attendance:
        print("No attendance found.")
        return
    print("\nMonthly Attendance for", month)
    print("---------------------------")
    for date in attendance[emp_id]:
        if month in date:
            print(date, ":", attendance[emp_id][date])