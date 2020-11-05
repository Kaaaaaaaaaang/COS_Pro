def solution(scores):
    grade_counter = [0 for i in range(5)]
    for x in scores:
        if 85<=x<=100:
            grade_counter[0] += 1
        elif 70<=x<=84:
            grade_counter[1] += 1
        elif 55<=x<=69:
            grade_counter[2] += 1
        elif 40<=x<=54:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter
