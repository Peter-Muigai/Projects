class Employee:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    def get_info(self):
        return f"Name: {self.name} ID: {self.id} Department:{self.department}"

class Manager(Employee):
    def __init__(self, name, id, department, team_size):
        super().__init__(name, id, department)
        self.team_size = team_size

    def get_info(self):
        parent_get_info = super().get_info()
        return parent_get_info + f" Team size: {self.team_size}"

class Engineer(Employee):
    def __init__(self, name, id, department, specialization):
        super().__init__(name, id, department)
        self.specialization = specialization

    def get_info(self):
        parent_get_info = super().get_info()
        return parent_get_info + f"Specializes in: {self.specialization}"

manager = Manager("Micheal Bosh", 13456, "Sales", 12)
engineer = Engineer("Paul Mathe", 43908, "Production Process", "Quality Assurance")

print(manager.get_info())
print(engineer.get_info())