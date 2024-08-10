import random
import time

rpc = ["グー", "チョキ", "パー"]  # rpc = rock_paper_scissors
print("じゃんけんしましょう")
print("1.グー 2.チョキ 3.パー")
print("数字を入力してね\n")

while True:
    while True:
        number = input("あなたの手は？: ")
        if number == '1':
            user = "グー"
            break
        elif number == '2':
            user = "チョキ"
            break
        elif number == '3':
            user = "パー"
            break
        else:
            print("無効な入力です。もう一度入力してください。")

    cpu = random.choice(rpc)

    print(f"{user}だね。いくよ！\n")
    time.sleep(1.5)
    print("じゃん！")
    time.sleep(0.7)
    print("けん！")
    time.sleep(0.7)
    print("ぽん！")
    print(f"【あなた】{user} vs {cpu}【CPU】")

    time.sleep(2.0)
    if user == cpu:
        print("あいこ！もう一度挑戦しましょう。\n")
    else:
        if user == "グー":
            if cpu == "チョキ":
                print("あなたの勝ち！")
            elif cpu == "パー":
                print("あなたの負け！")
        elif user == "チョキ":
            if cpu == "グー":
                print("あなたの負け！")
            elif cpu == "パー":
                print("あなたの勝ち！")
        elif user == "パー":
            if cpu == "グー":
                print("あなたの勝ち！")
            elif cpu == "チョキ":
                print("あなたの負け！")
        break