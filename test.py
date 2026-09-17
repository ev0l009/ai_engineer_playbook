students = ["Mary", "Mary", "John", "Tony", "Jude", "Tony"]
student_dict = {}
for name in students:
    if name not in student_dict.keys():
        student_dict[name] = 1
    else:
        student_dict[name] += 1

print(student_dict)