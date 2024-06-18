import random


def generate_exam_schedule(num_exams, days, times, ticket_numbers, disciplines):
    schedule = {}
    used_days = set()
    used_times = set()
    used_tickets = set()

    for i in range(num_exams):
        exam_day = random.choice([day for day in days if day not in used_days])
        used_days.add(exam_day)

        exam_time = random.choice([time for time in times if time not in used_times])
        used_times.add(exam_time)

        exam_ticket = random.choice([ticket for ticket in ticket_numbers if ticket not in used_tickets])
        used_tickets.add(exam_ticket)

        exam_discipline = random.choice(disciplines)
        disciplines.remove(exam_discipline)

        schedule[i + 1] = {
            'discipline': exam_discipline,
            'day': exam_day,
            'time': exam_time,
            'ticket': exam_ticket
        }

    for exam_num, details in schedule.items():
        print(f"Экзамен по дисциплине «{details['discipline']}» состоится в {details['day']} "
              f"время {details['time']}. Ваш счастливый билет N {details['ticket']}.")



num_exams = 4
days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
times = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00']
ticket_numbers = list(range(1, 21))
disciplines = ['математика', 'физика', 'химия', 'биология', 'история', 'литература', 'информатика', 'иностранный язык']

generate_exam_schedule(num_exams, days, times, ticket_numbers, disciplines)