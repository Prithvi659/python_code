import random
import game_data
import art
print(art.logo)

def account(compare):
    acc_name=compare["name"]
    acc_desp=compare['description']
    acc_country=compare['country']
    print(f"{acc_name} is a {acc_desp} from {acc_country}")

compare_b=random.choice(game_data.data)

game_should_countine=True

score=0

while game_should_countine:
    compare_a=compare_b
    compare_b=random.choice(game_data.data)
    while compare_a==compare_b:
          compare_b=random.choice(game_data.data)

    account(compare_a)
    print(art.vs)
    account(compare_b)


    answer=input("who has more followers  'A' or 'B' ").lower()
    print("\n"*20)
    print(art.logo)
    acc_follow_a=compare_a["follower_count"]
    acc_follow_b=compare_b["follower_count"]
    print("followers of a ",acc_follow_a)
    print("followers of b ",acc_follow_b)


    correct_answer=""
    if acc_follow_a > acc_follow_b:
        correct_answer="a"
    else:
        correct_answer="b"

    if answer==correct_answer:
        score+=1
        print("correct your current score = ",score)

    else:
        print("wrong your final score = ",score)
        game_should_countine=False
