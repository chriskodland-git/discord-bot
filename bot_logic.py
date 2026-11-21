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

def meme():
    return random.choice(["images/meme1.png", "images/meme2.png", "images/meme3.png"])




def pollution():
    messages = [
        " Water Pollution: Plastic waste harms marine animals. Stop using single-use plastics!",
        " Air Pollution: Car exhaust releases harmful gases. Try walking or cycling instead!",
        " Deforestation: Trees absorb carbon dioxide. Help by planting more trees!",    
        " Recycling: Recycling plastic, paper and metal helps reduce waste!",
        " Climate Change: Save electricity by turning off lights when you leave a room!",
    ]
    fact = random.choice(messages)
    return fact

currentanswer = ""

def pollution_quiz():
    global currentanswer
    pollution_questions = {
        "Air pollution can cause breathing problems and lung diseases.": True,
        "Plastic waste takes only a few days to break down in the ocean.": False,
        "Carbon dioxide is a greenhouse gas that contributes to global warming.": True,
        "Noise pollution is not considered a type of pollution.": False,
        "Burning fossil fuels is a major source of air pollution.": True,
        "Oil spills can harm marine animals and ecosystems.": True,
        "Water pollution only affects the fish that live in the water.": False,
        "Acid rain is caused by pollutants like sulfur dioxide and nitrogen oxides.": True,
        "Recycling helps reduce pollution and waste.": True,
        "The ozone layer protects the Earth from harmful ultraviolet rays.": True,
        "Planting trees can help reduce air pollution.": True,
        "Factories are the only source of pollution.": False,
        "Light pollution can affect the behavior of animals such as birds and sea turtles.": True,
        "Plastic bags are biodegradable and disappear quickly in nature.": False,
        "Using public transport instead of cars can reduce air pollution.": True,
        "Pesticides and fertilizers from farms can pollute rivers and lakes.": True,
    }
    question = random.choice(list(pollution_questions))
    currentanswer = str(pollution_questions[question]).lower()
    return question + " Type ?answer true or ?answer false"

def correct_answer(guess):
    if guess.lower() == currentanswer:
        return "Correct!"
    else:
        return "Incorrect!"

def lottry():
    number = random.randint(0,50)
    return number
