def Grade(evaluated_list, answers_list):
    equal_count = sum(1 for a, e in zip(answers_list, evaluated_list) if a == e)
    total = len(evaluated_list)
    return (equal_count/total)*100