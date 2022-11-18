from collections import defaultdict

class Database:

    questions = [
        "¿Cómo esta tu estado de ánimo?",
        "¿Tienes malestar en la garganta?",
        "¿Tienes tos seca?",
        "¿Te sientes cansado?",
        "¿Has tenido dificultades para respirar?",
        "¿Has tenido fiebre recientemente?",
    ]

    current_question_user = {

    }

    user_answers = defaultdict(dict)

    def get_next_question(self, user):
        curr_q =  Database.current_question_user.get(user, 0)
        return Database.questions[curr_q]

    def save_answer(self, user, answer):
        current_question = Database.current_question_user.get(user, 0)
        Database.user_answers[user][current_question] = answer
        Database.current_question_user[user] = current_question + 1

    def has_answered_all_questions(self, user):
        current_question = Database.current_question_user.get(user, 0)
        return current_question == len(Database.questions)
