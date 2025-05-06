def readstudents(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        students = [line.strip() for line in f]
    return students

def readscores(filename):
    scores = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            try:
                score_list = [int(score) for score in parts]
                scores.append(score_list)
            except ValueError:
                continue
    return scores    

def cal_total_scores(scores):
    return [sum(student_scores) for student_scores in scores]

def assign_grades(total_scores):
    grades = []
    for score in total_scores:
        if score >= 90:
            grades.append("A")
        elif score >= 80:
            grades.append("B")
        elif score >= 70:
            grades.append("C")
        elif score >= 60:
            grades.append("D")
        else:
            grades.append("FAIL")
        return grades

def type_grades(filename, students, total_scores, grades):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(len(students)):
            f.write(f"{students[i]} {total_scores[i]} {grades[i]}\n")

def main():
    students = readstudents("students.txt")
    scores = read_scores("scores.txt")
    total_scores = cal_total_scores(scores)
    grades = assign_grades(total_scores)
    type_grades('grades.txt', students, total_scores, grades)
    print('grades written to grads.txt')

if __name__ == "__main__":
    main()
        