from datetime import datetime, timedelta


def days_until_exam_to_date(days_until_exam):
    today = datetime.now()
    exam_date = today + timedelta(days=days_until_exam)

    return exam_date.strftime('%d %B %Y')



days_until_exam = 30
exam_date = days_until_exam_to_date(days_until_exam)
print(f"Экзамен состоится через {days_until_exam} дней, то есть {exam_date}")