class StudentManager():
    def __init__(self):
        self.students = []

    def create_students_file(self):
        with open("students.txt", "w") as file:
            file.write("John Doe, Group 1, 85\nJane Smith, Group 2, 90\nAlice Johnson, Group 1, 78\nBob Brown, Group 2, 88\n")

    def read_students_file(self):
        self.students = []
        with open("students.txt", "r") as file:
            for line in file:
                name, group, grade = line.split(",")
                self.students.append({"name": name, "group": group, "grade": float(grade)})

    def get_summary(self):
        groups = {}
        for student in self.students:
            group = student["group"]
            if group not in groups:
                groups[group] = []
            groups[group].append(student["grade"])

        result = f"Total students: {len(self.students)}\n"
        for group, grades in groups.items():
            mid = sum(grades) / len(grades)
            result += f"{group}: {len(grades)} students, middle mark: {mid:.1f}\n"
        return result

    def write_summary(self):
        summary = self.get_summary()
        with open("students.txt", "w") as file:
            file.write(summary)
