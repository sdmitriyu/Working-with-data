import json


def employees_rewrite(sort_type):
    with open('employees.json', 'r') as file:
        data = json.load(file)
        employees = data.get("employees", [])

        if sort_type not in employees[0]:
            raise ValueError('Bad key for sorting')

        sorted_employees = sorted(employees, key=lambda x: x[sort_type], reverse=True) if isinstance(
            employees[0][sort_type], int) else sorted(employees, key=lambda x: x[sort_type])

        output_data = {"employees": sorted_employees}

        with open(f'employees_{sort_type}_sorted.json', 'w') as output_file:
            json.dump(output_data, output_file, indent=4)


employees_rewrite('salary')
