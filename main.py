import art
import random
import game_data
import copy


def get_data(lst):
    sample = random.choice(lst)
    lst.remove(sample)
    return [sample, lst]


def compare(value_a, value_b):
    """Takes account values, user input and return if input is correct"""
    flag = False
    while not flag:
        answer = input("Who has more followers? Type 'A' or 'B':").lower()
        if answer == "a":
            flag = True
            return value_a >= value_b
        elif answer == "b":
            flag = True
            return value_a <= value_b
        else:
            print("That is not an available choice")


def print_compare(person_a, person_b):
    vowels = ["a", "e", "i", "o"]
    article_a = "a"
    article_b = "a"
    if person_a['description'][0] in vowels:
        article_a = "an"
    if person_b['description'][0] in vowels:
        article_b = "an"
    print(f"Compare A: {person_a['name']}, {article_a} {person_a['description']}, from {person_a['country']}.")
    print(art.vs)
    print(f"Against B: {person_b['name']}, {article_b} {person_b['description']}, from {person_b['country']}.")
    return compare(person_a['follower_count'], person_b['follower_count'])


correct = True
scores = 0
info = copy.deepcopy(game_data.data)

print(art.logo)
print("Compare who has more followers on social media")
print("")
print("")
info_a = {}
[info_b, info] = get_data(info)

while correct:
    if len(info) < 2:
        info = copy.deepcopy(game_data.data)
    info_a = info_b
    [info_b, info] = get_data(info)
    if print_compare(info_a, info_b):
        scores += 1
        print(f"Correct! {info_a['name']} is indeed has more followers than {info_b['name']}. Your current score is {scores}")
        print("----------------------------------------------")
    else:
        print(f"Sorry, that's wrong. Final score {scores}")
        correct = False
