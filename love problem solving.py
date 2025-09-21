import random

def love_dice(name1, name2):
    roll = random.randint(1, 6)
    outcomes = {
        1: "💖 Love is in the air!",
        2: "😊 Good friendship bond.",
        3: "😅 Some ups and downs.",
        4: "💌 Romance is coming soon.",
        5: "🌹 Strong feelings are mutual.",
        6: "💍 Wedding bells in the future!"
    }
    print(f"\n{name1} + {name2} → Dice Roll: {roll}")
    print("Result:", outcomes[roll])

n1 = input("Enter your name: ")
n2 = input("Enter partner's name: ")
love_dice(n1, n2)
