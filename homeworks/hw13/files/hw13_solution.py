# pylint: disable=unspecified-encoding


class StudentManager():
    def __init__(self,  filename="students.txt"):
        self.students = []
        self.filename = filename

    def create_students_file(self, students_content=None):
        if students_content is None:
            students_content = (
                "John Doe, Group 1, 85\nJane Smith, Group 2, 90\n"
                "Alice Johnson, Group 1, 78\nBob Brown, Group 2, 88\n"
            )

        with open(self.filename, "w") as file:
            file.write(students_content)

    def read_students_file(self):
        self.students = []
        with open(self.filename, "r") as file:
            for line in file:
                name, group, grade = line.split(",")
                self.students.append({
                    "name": name.strip(),
                    "group": group.strip(),
                    "grade": int(grade.strip())
                })

        student_tuples = []
        groups_summary = {}

        for student in self.students:
            student_tuples.append((student["name"], student["group"], student["grade"]))

            group = student["group"]
            if group not in groups_summary:
                groups_summary[group] = {"count": 0, "total_grade": 0}

            groups_summary[group]["count"] += 1
            groups_summary[group]["total_grade"] += student["grade"]

        return student_tuples, groups_summary

    def get_summary(self):
        if not self.students:
            return {}

        groups_summary = {}
        for student in self.students:
            group = student["group"]
            if group not in groups_summary:
                groups_summary[group] = {"count": 0, "total_grade": 0}

            groups_summary[group]["count"] += 1
            groups_summary[group]["total_grade"] += student["grade"]

        result = {}
        for group, stats in groups_summary.items():
            result[group] = {
                "count": stats["count"],
                "avg_grade": stats["total_grade"] / stats["count"]
            }
        return result

    def write_summary_to_file(self):
        summary = self.get_summary()
        output = f"\nTotal students: {sum(group['count'] for group in summary.values())}\n"
        for group, stats in summary.items():
            output += f"{group}: {stats['count']} students, middle mark: {stats['avg_grade']:.1f}\n"

        with open(self.filename, "a") as file:
            file.write(output)
