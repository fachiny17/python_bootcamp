import pandas
student_dict = {"student": ["Chisom", "Ikenna", "Venessa",
                            "Chinwendu", "Jack", "Kane", "Alex", "Hannah"],
                "score": [87, 34, 71, 53, 43, 56, 67, 72]}


student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Chisom":
        print(row.score)
