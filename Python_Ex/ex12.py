def check_pass_fail(marks):
    if isinstance(marks, (int, float)) and 0 <= marks <= 100:
        if marks >= 40:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Invalid marks")

marks = 75

check_pass_fail(marks)