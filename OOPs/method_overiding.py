# Consider a scenario where you have a base class called Employee and derived classes such as Manager, Engineer, and Salesperson. 
# How would you handle implementing a common method, such as calSalary(), in each derived class using inheritance and method overriding?

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
        
    def cal_salary(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name,salary)
        self.bonus = bonus
        
    def cal_salary(self):
        return super().cal_salary()+self.bonus
    
class Engineer(Employee):
    def __init__(self, name, salary, overtime_hours):
        super().__init__(name,salary)
        self.overtime = overtime_hours
        
        
    def cal_salary(self):
        return super().cal_salary()+(self.overtime*10) #10 per hour
    
class Salesperson(Employee):
    def __init__(self, name, salary, commission):
        super().__init__(name, salary)
        self.commission = commission
        
    def cal_salary(self):
        return super().cal_salary()+(self.commission * 0.1)
    
    
# Example usage:
manager = Manager("John Doe", 50000, 10000)
engineer = Engineer("Jane Smith", 60000, 5)
salesperson = Salesperson("Alice Johnson", 40000, 5000)

print("Manager's Salary:", manager.cal_salary())
print("Engineer's Salary:", engineer.cal_salary())
print("Salesperson's Salary:", salesperson.cal_salary())