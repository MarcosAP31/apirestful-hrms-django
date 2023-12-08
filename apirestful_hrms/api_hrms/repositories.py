from .models import Employee

class EmployeeRepository:
    @staticmethod
    def get_all_employees():
        return Employee.objects.all()

    @staticmethod
    def get_employee_by_id(employee_id):
        return Employee.objects.get(pk=employee_id)
        
    @staticmethod
    def create_employee(data):
        return Employee.objects.create(**data)

    @staticmethod
    def update_employee(employee, data):
        for key, value in data.items():
            setattr(employee, key, value)
        employee.save()
        return employee

    @staticmethod
    def delete_employee(employee):
        employee.delete()