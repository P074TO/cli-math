from random import randint
from time import perf_counter

correct_ans = 0
lives = 5
x = 0
y = 0
z = 0
ans = 0
p_ans = 0
tick = perf_counter()
t1 = 0
t2 = 0
t3 = 0
total_time = 0
avg_time = 0
score = 0
inp = ''
oprtr1 = ''
oprtr2 = ''


def print_stats(answers, lives, time, score=0):
    if score == 0:
        print(f"""
        Correct Answers: {answers}
        Lives: {lives}
        Time Elapsed = {time:.2f}
        """)
    else:
        print(f"""
        Correct Answers: {answers}
        Lives: {lives}
        Time Elapsed = {time:.2f}
        Score: {score:.0f}
        """)


def compute_score(answers, lives, time):
    score = 10*((answers+lives)/(time/10))
    if answers > 5:
        score = score + (score * 0.75)
    elif answers > 10:
        score = score * 
    else:
        score = score - (score * 0.5)
    return score


print("""
**** Brain Buster Math Levels Adventure ****
Each level has a series of questions to be answered by the player.
The player will start with 5 lives which can be deducted for every
incorrect answer, and incremented for completing a level if there is at least
one missing life.
The player will be scored by the number of questions answered correctly
and time elapsed.
""")

while True:
    print("Proceed? Answer 'Y'es or 'N'o")
    inp = input()
    if inp == 'n' or inp == 'N':
        print("Exiting program...")
        exit(1)
    elif inp == 'y' or inp == 'Y':
        break
    else:
        continue

inp = ''


while lives > 0:
    while correct_ans != 5:
        if lives == 0:
            break
        oprtr1 = '+' if (randint(0,1) == 0) else '-'
        x = randint(1, 9)
        y = randint(1, 9)
        if x < y and oprtr1 == '-':
            x = randint(y, 9)
        if oprtr1 == '+':
            ans = x+y
        else:
            ans = x-y
        print("Easy Question")
        print(f"{x} {oprtr1} {y}")
        inp = input()
        try:
            if int(inp) == ans:
                correct_ans += 1
                print("Correct!")
                print_stats(correct_ans, lives, perf_counter() - tick)
            else:
                lives -= 1
                print("Incorrect!")
                print_stats(correct_ans, lives, perf_counter() - tick)
        except ValueError:
            print("Input a valid integer!")
    t1 = (perf_counter() - tick)
    t2 = perf_counter()
    print("******** EASY LEVEL STATS ********")
    print_stats(correct_ans, lives, t1)
    if lives == 0:
        while True:
            print("Used all lives! Play Again? Answer 'Y'es or 'N'o")
            inp = input()
            if inp == 'n' or inp == 'N':
                avg_time = t1/3
                score = compute_score(correct_ans, lives, avg_time)
                print_stats(correct_ans, lives, t1, score)
                print(f"""
                Thanks for playing!
                Exiting program...
                """)
                exit(1)
            elif inp == 'y' or inp == 'Y':
                correct_ans = 0
                lives = 5
                tick = perf_counter()
                t1 = 0
                t2 = 0
                t3 = 0
                print("Restarting game...")
                break
            else:
                continue
        continue
    print("Moving on to the next level (MEDIUM)")
    if lives < 5:
        lives += 1
        print("Adding 1 life")
        print(f"Lives: {lives}")
    while correct_ans != 10:
        if lives == 0:
            break
        oprtr1 = '+' if (randint(0,1) == 0) else '-'
        x = randint(10, 75)
        y = randint(10, 75)
        if x < y and oprtr1 == '-':
            x = randint(y, 99)
        if oprtr1 == '+':
            ans = x+y
        else:
            ans = x-y
        print("Medium Question")
        print(f"{x} {oprtr1} {y}")
        inp = input()
        try:
            if int(inp) == ans:
                correct_ans += 1
                print("Correct!")
                print_stats(correct_ans, lives, perf_counter() - tick)
            else:
                lives -= 1
                print("Incorrect!")
                print_stats(correct_ans, lives, perf_counter() - tick)
        except ValueError:
            print("Input a valid integer!")
    t2 = (perf_counter() - t2)
    t3 = perf_counter()
    print("******** MEDIUM LEVEL STATS ********")
    print_stats(correct_ans, lives, t2)
    if lives == 0:
        while True:
            print("Used all lives! Play Again? Answer 'Y'es or 'N'o")
            inp = input()
            if inp == 'n' or inp == 'N':
                avg_time = t1+t2/3
                score = compute_score(correct_ans, lives, avg_time)
                print_stats(correct_ans, lives, t1+t2, score)
                print(f"""
                Thanks for playing!
                Exiting program...
                """)
                exit(1)
            elif inp == 'y' or inp == 'Y':
                correct_ans = 0
                lives = 5
                tick = perf_counter()
                t1 = 0
                t2 = 0
                t3 = 0
                print("Restarting game...")
                break
            else:
                continue
        continue
    print("Moving on to the next level (HARD)")
    if lives < 5:
        lives += 1
        print("Adding 1 life")
        print(f"Lives: {lives}")
    while correct_ans != 15:
        if lives == 0:
            break
        oprtr1 = randint(0,2)
        oprtr2 = randint(0,2)
        match oprtr1:
            case 0:
                oprtr1 = '+'
            case 1:
                oprtr1 = '-'
            case 2:
                oprtr1 = '*'
        match oprtr2:
            case 0:
                oprtr2 = '+'
            case 1:
                oprtr2 = '-'
            case 2:
                oprtr2 = '*'
        x = randint(1, 50)
        y = randint(1, 50)
        z = randint(1, 50)
        if x < y and oprtr1 == '-':
            x = randint(y, 99)
        if oprtr1 == '+':
            p_ans = x+y
        elif oprtr1 == '-':
            p_ans = x-y
        else:
            p_ans = x*y
        if oprtr2 == '+':
            ans = p_ans+z
        elif oprtr2 == '-':
            ans = p_ans-z
        else:
            ans = p_ans*z
        if p_ans < z and oprtr2 == '-':
            x = randint(y, 99)
        print("Hard Question")
        print(f"({x} {oprtr1} {y}) {oprtr2} {z}")
        inp = input()
        try:
            if int(inp) == ans:
                correct_ans += 1
                print("Correct!")
                print_stats(correct_ans, lives, perf_counter() - tick)
            else:
                lives -= 1
                print("Incorrect!")
                print_stats(correct_ans, lives, perf_counter() - tick)
        except ValueError:
            print("Input a valid integer!")
    t3 = (perf_counter() - t3)
    print("******** HARD LEVEL STATS ********")
    print_stats(correct_ans, lives, t2)
    if lives == 0:
        while True:
            print("Used all lives! Play Again? Answer 'Y'es or 'N'o")
            inp = input()
            if inp == 'n' or inp == 'N':
                avg_time = t1+t2+t3/3
                score = compute_score(correct_ans, lives, avg_time)
                print_stats(correct_ans, lives, t1+t2+t3, score)
                print(f"""
                Thanks for playing!
                Exiting program...
                """)
                exit(1)
            elif inp == 'y' or inp == 'Y':
                correct_ans = 0
                lives = 5
                tick = perf_counter()
                t1 = 0
                t2 = 0
                t3 = 0
                print("Restarting game...")
                break
            else:
                continue
        continue
    total_time = t1+t2+t3
    avg_time = total_time/3
    score = compute_score(correct_ans, lives, avg_time)
    print_stats(correct_ans, lives, total_time, score)
    while True:
        print("Play Again? Answer 'Y'es or 'N'o")
        inp = input()
        if inp == 'n' or inp == 'N':
            print(f"""
            Thanks for playing!
            Exiting program...
            """)
            exit(1)
        elif inp == 'y' or inp == 'Y':
            correct_ans = 0
            lives = 5
            tick = perf_counter()
            t1 = 0
            t2 = 0
            t3 = 0
            print("Restarting game...")
            break
        else:
            continue        

