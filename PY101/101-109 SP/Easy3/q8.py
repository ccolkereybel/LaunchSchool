def get_grade(score1, score2, score3):
    average = (score1 + score2 + score3) / 3

    match average:
        case _ if average >= 90:
            return 'A'
        case _ if average >= 80:
            return 'B'
        case _ if average >= 70:
            return 'C'
        case _ if average >= 60:
            return 'D'
        case _:
            return 'F'
        
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

    