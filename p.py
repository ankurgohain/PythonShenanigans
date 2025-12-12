class Employee:
    def getdata(self):
        self.empid = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.desig=input("Enter Employee Designation: ")

class Salary:
    def getSalData(self):
        self.basicSalary = float(input("Enter Basic Salary: "))

class netSalary(Employee, Salary):
    def calculateNetSalary(self):
        self.HRA = 0.20 * self.basicSalary
        self.DA = 0.10 * self.basicSalary
        self.PF = 0.12 * self.basicSalary
        self.netSalary = self.basicSalary + self.HRA + self.DA - self.PF

    def display(self):
        print(f"\nEmployee ID: {self.empid}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Designation: {self.desig}")
        print(f"Basic Salary: {self.basicSalary}")
        print(f"HRA: {self.HRA}")
        print(f"DA: {self.DA}")
        print(f"PF: {self.PF}")
        print(f"Net Salary: {self.netSalary}")