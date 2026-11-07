import random

def gen_pass(pass_length):
    elements = "+-/!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def coin_flip():
    return random.choice(["Heads", "Tails"])
result = coin_flip
print(result)

def rps_game():
    return random.choice(["Rock", "Paper", "Scissors"])
result = rps_game
print(result)

def dice_roll(count, sides):
    rolls = [random.randint(1, sides) for _ in range(count)]
    return rolls, sum(rolls)

result = dice_roll(3, 20)
