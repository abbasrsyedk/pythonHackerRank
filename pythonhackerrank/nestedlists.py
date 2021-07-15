if __name__ == '__main__':
    studs = []
    grades = []
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        stud = [name, grade]
        studs.append(stud)
        grades.append(grade)

    second_lowest_grade = sorted(set(grades))[1]
    new_stud_list = sorted(
        [stud[0]for stud in studs if stud[1] == second_lowest_grade])
    print("\n".join(new_stud_list))
