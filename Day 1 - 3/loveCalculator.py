name1 = input()
name2 = input()


names = (name1 + name2).upper()

love_count = names.count("L") + names.count("O") + names.count("V") + names.count("E")
true_count = names.count("T") + names.count("R") + names.count("U") + names.count("E")

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")



