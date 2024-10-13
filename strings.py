# Employee Information Management System

# A list of employee data
employee_data = "Name: John Doe, Age: 30, Role: Engineer"

employee_info = employee_data.split(",")

# Use strip to clean data and join to create a string with newlines
cleaned_data = "\n".join(info.strip() for info in employee_info)

print(cleaned_data)
# A tiny piece of code that represents an HR Employee Data Management system.
# This code will manage a simple string that contains employee data.

employee_data = "Alice,Developer,30|Bob,Manager,45|Charlie,Designer,25"
# Splitting the employee data by '|' to separate each employee's info
employee_list = employee_data.split('|')

# TODO: For each employee, create a formatted string with stripped details and role eligibility for a junior position
for employee in employee_list:
    name, role, age = employee.split(",")
    if role == "Developer" or role == "Designer":
        eligibility = "Eligible for junior position"
    else:
        eligibility = "Not eligible for junior position"    
    # TODO: Parse the employee data and add eligibility note if applicable
    print(f"Name: {name} - Role: {role} - Age: {age} - {eligibility}")
    # Example: Name: Alice - Role: Developer - Age: 30 - Eligible for junior position