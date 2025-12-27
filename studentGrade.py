grades = {"Arun":"A", "Varun":"C", "Tarun":"B" } #grades dictionary with student, grade key value pairs
grades["Tina"]="A" # New student Tine with grade A
grades["Tarun"]="F" # Existing student Tarun grade change
for i, v in grades.items():
    print(i," ", v)

