class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def pass_student(self):
        return self.mark>10
