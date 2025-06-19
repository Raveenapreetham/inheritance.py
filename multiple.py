# 2. Multiple Inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job):  # Inherits from both Employee and Job
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, salary)            # Initialize Job
