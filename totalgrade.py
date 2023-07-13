hwWeight = 0.4
examWeight = 0.5
discussionWeight = 0.1

def weighted_grade(hw, exam, discussion):
    weighted_grade = hw * hwWeight + exam * examWeight + discussion * discussionWeight
    return weighted_grade

def main():
    hw = float(input("Enter your homework grade: "))
    exam = float(input("Enter your exam grade: "))
    discussion = float(input("Enter your discussion grade: "))

    weighted_grade_value = weighted_grade(hw, exam, discussion)
    print("Your weighted grade is:", weighted_grade_value)