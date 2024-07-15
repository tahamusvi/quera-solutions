from multiprocessing import reduction


class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:
    # def __init__(self):
    #     self.line = []
        
    def set_file(self, address):
        self.address = address
        with open(address,'r') as file:
            self.lines = file.readlines()

    def load(self, line_number):
        line = self.lines[line_number-1]
        student_id_line  ,course_code_line ,score = line.split()
        grade = Grade(int(student_id_line)  ,int(course_code_line) ,float(score) )

        return grade

    def calc_student_average(self, student_id):
        temp = []
        for line in self.lines:
            student_id_line  ,course_code_line ,score = line.split()
            if str(student_id) == student_id_line:
                temp.append(score)

        return sum([float(x) for x in temp]) / len(temp)

    def calc_course_average(self, course_code):
        temp = []
        for line in self.lines:
            student_id ,course_code_line ,score = line.split()
            if str(course_code) == course_code_line :
                temp.append(score)

        return sum([float(x) for x in temp]) / len(temp)

    def count(self):
        return len(self.lines)

    def save(self, grade):
        temp = f"{grade.student_id} {grade.course_code} {grade.score}\n"
        if temp in self.lines:
            return
        
        with open(self.address,'a') as file:
            file.write(f"\n{temp}")
        
        self.set_file(self.address)



# file = "testt.txt"
# util = CourseUtil()
# util.set_file(file)
# print(util.count())    # 2

# print(util.lines)

