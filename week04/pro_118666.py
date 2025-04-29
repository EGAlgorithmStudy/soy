def solution(survey, choices):
    ans1 = "R"  # T
    ans2 = "C"  # F
    ans3 = "J"  # M
    ans4 = "A"  # N
    score_obj = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }

    for surv, choice in zip(survey, choices):
        score = 4 - choice
        if score == 0:
            continue
        is_first = score > 0
        if is_first:
            score_obj[surv[0]] += abs(score)
        else:
            score_obj[surv[1]] += abs(score)

    if score_obj['R'] < score_obj['T']:
        ans1 = 'T'
    if score_obj['C'] < score_obj['F']:
        ans2 = 'F'
    if score_obj['J'] < score_obj['M']:
        ans3 = 'M'
    if score_obj['A'] < score_obj['N']:
        ans4 = 'N'

    return ans1 + ans2 + ans3 + ans4