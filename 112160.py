import random
from random import randint

def fight(monster_name,nickname):
    print("Сражение начинается!")
    print(f"{monster_name} vs {nickname}")
def run():
    m=randint(1,100)
    if m!=100:
       print("Вы успешно сбежали")
    # else:
    #    die()

def getcommand_prefight():
    command=str(input())
    if command=="fight":
        fight()
    elif command=="run":
        run()
    else:
        print("Неизвестная команда")
        getcommand_prefight()
def getcommand_adventure():
    command=str(input())
    if command=="go":
        go()
    elif command=="stats":
        stats()
    else:
        print("Неизвестная команда")
        getcommand_adventure()
def stats():
    print(".............................................")
    print(nickname)
    print(f"Уровень: {hlvl}")
    print(f"Опыт: {hexp}")
    print(f"Здоровье: {hhp}")
    print(f"Сила атаки: {hatk}")
    print(f"Защита: {hatk}")
    print(".............................................")

def go(command):
    if command == "go":
        global location
        location=(random.choice(location_list))
        print(f"Вы попали в {location}")
        g=randint(0,10)
        if g<9:
            monster()
        else:
            chest()

    else:
        print("Неизвестная команда")
        command = input()
        go(command)

def startstats(command):
    if command == "stats":
        stats()
        print("Отлично! Теперь давай попробуем одолеть первого монстра.")
        print("Введи go, чтобы отправиться в следующую локацию")
        command = str(input())
        go(command)
    else:
        print("Неизвестная команда")
        command=input()
        startstats(command)

def monster():
    global monster_name
    print("Вы нашли монстра:")
    print(".............................................")
    monster_name=random.choice(monster_name_list)
    print(monster_name)
    mlvl=randint(0,5)
    print(f"Уровень: {mlvl}")
    mhp=randint(0,20)
    print(f"Здоровье: {mhp}")
    matk=randint(0,5)
    print(f"Сила атаки: {matk}")
    mdef=randint(0,5)
    print(f"Защита: {mdef}")
    print(".............................................")
    print("Сражаться(fight) или сбежать(run)?")
    getcommand_prefight()

def chest():
    print("Поздравляю вы нашли предмет")



hhp=100
hdef=0
hatk=10
hexp=0
hlvl=1

location="0"
location_list=['лес','равнина','пляж','пустыня','гора','пещера']
monster_name_list=['гоблин','тролль','скелет','грабитель']
monster_name=""

print("Введите имя вашего персонажа")
nickname=str(input())
print(f"Приветствую {nickname}")
print(f"Я Беннни, дух прошлого героя. Я буду помогать тебе в твоем приключении.")
print("Один чародей призвал тебя в этот мир, чтобы ты помог ему справиться с могущенственным некромантом.")
print("Помоги ему и он исполнит любое твое желание")
print("*уррррр")
print("Кажется у тебя урчит в животе. Самое время добыть денег")
print("Но для начала попробуй узнать свои характеристики. Введи stats")
command=str(input())
startstats(command)


