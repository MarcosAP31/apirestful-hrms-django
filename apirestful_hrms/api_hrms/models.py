from django.db import models

class Employee(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255)
    LastName=models.CharField(max_length=255)
    Birthday=models.DateField()
    Gender=models.CharField(max_length=255)
    Phone=models.BigIntegerField()
    Email=models.CharField(max_length=255)
    Address=models.CharField(max_length=255)
    HireDate=models.DateField()
    TerminationDate=models.DateField()
    DepartmentId=models.IntegerField()
    PositionId=models.IntegerField()
    ManagerId=models.IntegerField()
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Image = models.ImageField(upload_to='Employee_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.Name} {self.LastName}"

    class Meta:
        db_table = 'employee'  # Set the desired table name

class Department(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255)
    ManagerId=models.IntegerField()
    Description=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        db_table = 'department'  # Set the desired table name

class Position(models.Model):
    PositionId=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=255)
    Description=models.CharField(max_length=255)
    Responsabilities=models.CharField(max_length=1000)
    Requirements=models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.Title}"

    class Meta:
        db_table = 'position'  # Set the desired table name

class Salary(models.Model):
    SalaryId=models.AutoField(primary_key=True)
    EmployeeId=models.IntegerField()
    Amount=models.DecimalField(max_digits=10, decimal_places=2)
    EffectiveDate=models.DateField()
    Currency=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.Amount}"

    class Meta:
        db_table = 'salary'  # Set the desired table name

class Attendance(models.Model):
    AttendanceId=models.AutoField(primary_key=True)
    EmployeeId=models.IntegerField()
    Date=models.DateField()
    ClockInTime=models.DateTimeField()
    ClockOutTime=models.DateTimeField()
    def __str__(self):
        return f"{self.Date}"

    class Meta:
        db_table = 'attendance'  # Set the desired table name

class Leave(models.Model):
    LeaveId=models.AutoField(primary_key=True)
    EmployeeId=models.IntegerField()
    StartDate=models.DateField()
    EndDate=models.DateField()
    Type=models.CharField(max_length=255)
    Status=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.StartDate}"

    class Meta:
        db_table = 'leave'  # Set the desired table name

class Training(models.Model):
    TrainingId=models.AutoField(primary_key=True)
    EmployeeId=models.IntegerField()
    Title=models.CharField(max_length=255)
    TrainingDate=models.DateField()
    TrainerName=models.CharField(max_length=255)
    Duration=models.IntegerField()
    def __str__(self):
        return f"{self.Title}"

    class Meta:
        db_table = 'training'  # Set the desired table name

class Benefit(models.Model):
    BenefitId=models.AutoField(primary_key=True)
    EmployeeId=models.IntegerField()
    Type=models.CharField(max_length=255)
    Description=models.CharField(max_length=255)
    StartDate=models.DateField()
    EndDate=models.DateField()
    def __str__(self):
        return f"{self.Description}"

    class Meta:
        db_table = 'benefit'  # Set the desired table name



