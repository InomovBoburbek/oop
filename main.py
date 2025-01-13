class Pupil:
    def __init__(self, ism, fam, yosh, gpa):
        self.ism = ism
        self.fam = fam
        self.yosh = int(yosh)
        self.gpa = float(gpa)

    def get_info(self):
        return f"Ism: {self.ism}, Familiya: {self.fam}, Yosh: {self.yosh}, GPA: {self.gpa}"


class PupilManager:
    def __init__(self):
        self.pupils = []

    def add_pupil(self, ism, fam, yosh, gpa):
        new_pupil = Pupil(ism, fam, yosh, gpa)
        self.pupils.append(new_pupil)

    def get_pupils(self):
        for pupil in self.pupils:
            print(pupil.get_info())

    def max_gpa(self):
        if len(self.pupils) == 0:
            return "Hech qanday o'quvchi mavjud emas"
        top_pupil = max(self.pupils, key=lambda p: p.gpa)
        return f"Maksimal GPA: {top_pupil.gpa}, O'quvchi: {top_pupil.get_info()}"


# Manager obyekti yaratamiz va o'quvchilarni qo'shamiz
manager = PupilManager()
manager.add_pupil("Boburbek", "Inomov", 15, 3.8)
manager.add_pupil("Shuhrat", "Fayzullayev", 16, 3.9)

# O'quvchilarni ko'rsatish
manager.get_pupils()

# Maksimal GPAni ko'rsatish
print(manager.max_gpa())

