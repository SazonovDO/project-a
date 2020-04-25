from flask import blueprints, render_template, session, request
import random

bulls_game = blueprints.Blueprint(__name__, 'bulls_game')


@bulls_game.route('/')
def cows_bulls():
    print(session.get('computer_number'))

    return render_template('rule_game_cows.html')


@bulls_game.route('/start')
def start_game():
    computer_no = 1111
    while not check_repeated(computer_no):
        computer_no = random.randrange(1000, 10000)
    session['computer_number'] = computer_no
    return render_template('cows_bulls.html', message='number was made up')


def check_repeated(number):
    a = number // 1000
    b = number // 100 % 10
    c = number % 100 // 10
    d = number % 10
    l = [a, b, c, d]
    s = set(l)
    return len(s) == 4


def validate_answer(secret, users):
    cow = 0
    bull = 0
    a = secret // 1000
    b = secret // 100 % 10
    c = secret % 100 // 10
    d = secret % 10
    e = users // 1000
    f = users // 100 % 10
    g = users % 100 // 10
    h = users % 10
    l1 = [a, b, c, d]
    l2 = [e, f, g, h]

    for i in range(4):
        if l1[i] == l2[i]:
            bull += 1
        for k in range(4):
            if l1[k] == l2[i] and i != k:
                cow += 1
    answer = 'yuo have - {} bulls, and {} cows'.format(bull, cow)
    return answer


@bulls_game.route('/guss', methods=['post'])
def guss():
    user_no = int(request.form.get('user_number', 0))
    computer_no = int(session.get('computer_number'))
    answer = validate_answer(computer_no, user_no)
    return render_template('cows_bulls.html', message=answer)
