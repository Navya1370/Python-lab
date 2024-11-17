def calculate_gpa(subjects):
    total_points = 0
    total_credits = 0
    
    for subject in subjects:
        name, credit, grade_point = subject
        total_points += credit * grade_point
        total_credits += credit
    
    if total_credits == 0:
        return 0
    return total_points / total_credits

def calculate_cgpa(semesters):
    total_points = 0
    total_credits = 0
    
    for semester in semesters:
        gpa, semester_credits = semester
        total_points += gpa * semester_credits
        total_credits += semester_credits
    
    if total_credits == 0:
        return 0
    return total_points / total_credits

# Input subjects for each semester
semesters = []
num_semesters = int(input("Enter number of semesters: "))

for i in range(num_semesters):
    num_subjects = int(input(f"\nEnter the number of subjects in Semester {i+1}: "))
    subjects = []
    
    for j in range(num_subjects):
        subject_name = input(f"Enter the name of Subject {j+1}: ")
        credit = float(input(f"Enter the credits for {subject_name}: "))
        grade_point = float(input(f"Enter the grade points for {subject_name}: "))
        subjects.append((subject_name, credit, grade_point))
    
    semester_gpa = calculate_gpa(subjects)
    semester_credits = sum(credit for _, credit, _ in subjects)
    semesters.append((semester_gpa, semester_credits))
    
    print(f"GPA for Semester {i+1}: {semester_gpa:.2f}")

# Calculate overall CGPA
cgpa = calculate_cgpa(semesters)
print(f"\nOverall CGPA: {cgpa:.2f}")
2
