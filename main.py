import csv
import json
import datetime

data = str(datetime.datetime.now())
def save_game(game_data, file_name):
    print(game_data)
    with open(file_name, 'w', encoding="utf-8") as file:
        json.dump(game_data,  file, ensure_ascii=False)


def savCsv(game_data,file_name):
    with open(file_name, "w",  encoding="cp1251",  newline='') as file:
        a = [i for i in game_data.keys()]

        data = []
        data.append(game_data)
        writer = csv.DictWriter(file, delimiter=";", fieldnames=a)
        writer.writeheader()
        writer.writerows(data)

def load_game(file_name):
    with open(file_name, 'r') as file:
        game_data = json.load(file)
    return game_data

def main():
    print("Добро пожаловать в Escape Rooms!")
    print("1. Начать игру")
    print("2. Посмотреть сохранения")
    choice = input("Выберите действие:")
    if choice == "1":
        pass
    if choice == "2":
        loaded_games = load_game('saves.json')
        print(loaded_games)
        main()
main()

print("Введите ваше имя:")
name = input()
print(f"Ну что, начинаем, {name}")
inv = []


def call_for_help():
    print("Вы пытаетесь позвать напомощь, но никто не откликается..."
          "\nПохоже, вы здесь один.")
    story1()


def story1():
    print("Выберите действие:")
    print("1. Исследовать комнату.")
    print("2. Позвать на помощь.")
    choice = input("Введите номер действия: ")
    if choice == "1":
        explore_room()
    elif choice == "2":
        call_for_help()
    else:
        print("Некорректный ввод. Попробуйте еще раз.")
        story()


def explore_room():
    print("Вы исследуете комнату и находите...")
    print("1. Загадочную дверь.")
    print("2. Старый дневник.")
    print("3. Сундук.")
    choice = input("Введите номер предмета для исследования: ")
    if choice == "1":
        explore_door()
    elif choice == "2":
        explore_diary()
    elif choice == "3":
        explore_chest()
    else:
        print("Некорректный ввод. Попробуйте еще раз.")
        explore_room()


def explore_room1():
    print("Вы возвращаетесь в комнату и видите:")
    print("1. Загадочную дверь.")
    print("2. Сундук.")
    choice = input("Введите номер предмета для исследования: ")
    if choice == "1":
        explore_door()
    elif choice == "2":
        explore_chest()
    else:
        print("Некорректный ввод. Попробуйте еще раз.")
        explore_room1()


def explore_room2():
    print("Вы возвращаетесь в комнату и видите:")
    print("1. Загадочную дверь.")
    choice = input("Введите номер предмета для исследования: ")
    if choice == "1":
        explore_door()
    else:
        print("Некорректный ввод. Попробуйте еще раз.")
        explore_room2()
def trap():
    print("Вы решили пойти к огоньку"
          "\nК сожалению, его света было недостаточно, чтобы вы увидели капкан, лежащий на пути"
          "\nВы пытаетсь высвободиться, но боль со временем становится только сильнее"
          "\nВы падаете на землю и больше не встаете...")
    print("ВЫ ПОГИБЛИ")
    game_state = {
        "Имя:": name,
        "Причина смерти:": "Потеря крови",
        "Дата:": data
    }
    savCsv(game_state, 'saves.csv')
    save_game(game_state, 'saves.json')
    exit()
def levo():
    print("Вы решили свернуть налево"
          "\nПеред вами еще развилка."
          "\nТак же, как и в прошлый раз, слева темнота, а справа небольшой огонек. Куда теперь?"
          "\n1. Налево"
          "\n2. Направо")
    choice = input()
    if choice == "1":
        print("Вы решили снова свернуть налево"
              "\nВы идете вперед неизвестно сколько времени..."
              "\nВаши ноги скоро откажут и вы рухнете на землю..."
              "\nВдруг вы почувствовали небольшой ветерок, а пройдя еще немного, увидели солнечный свет, впервые задолгое время")
        print("ВЫ ВЫБРАЛИСЬ")
        exit()
    if choice == "2":
        trap()

def pravo():
    print("Вы решаете идти к огоньку"
          "\nПройдя вперед, вы натыкаетесь на еще одну развилку."
          "\nСлева вы опять видите небольшой огонек, а справа довольно освещенную комнату"
          "\nКуда теперь?"
          "\n1. Налево"
          "\n2. Направо")
    choice = input()
    if choice == "1":
        trap()
    if choice == "2":
        print("Вы идете к освещенной комнате и заходите в нее..."
              "\nВдруг, дверь за вами захлопывается и вы снова слышите шепот:"
              "\n\"ХА-ХА-ХА-ХА-ХА-ХА\""
              "\n\"Разве ты не знаешь, что незнакомых людей лучше не слушать?\""
              "\n\"Тем более если этот человек - голос в твоей голове\""
              "\n\"Теперь тебя ожидает томительное ожидание...ожидание твоей СМЕРТИ\"")
        print("ВЫ ПОГИБЛИ")
        game_state = {
            "Имя:": name,
            "Причина смерти:": "Голод",
            "Дата:": data
        }
        savCsv(game_state, 'saves.csv')
        save_game(game_state, 'saves.json')
        exit()

def stage2():
    print("Когда вы заходите в комнату, окутанную мраком, вы слышите шепот:"
          "\n\"Всегда следуй за светом...\""
          "\nЗдесь абсолютно темно, вы не видите ничего, кроме черного цвета..."
          "\nПройдя дальше, вы натыкаетесь на развилку..."
          "\nВ левом проходе ничего не видно, а в правом вы замечаете небольшой огонек..."
          "\nКуда же идти?"
          "\n1. Налево"
          "\n2. Направо")
    choice = input()
    if choice == "1":
        levo()
    if choice == "2":
        pravo()

def complete():
    if "1" and "2" and "3" and "4" in inv:
        print("Вдруг вы слышите, как дверь отпирается....")
        stage2()
    else:
        statues()


def eagle():
    print("Вы подошли к статуе Орла")
    print("Похоже, нужно сдвинуть ее на правильное место...")
    print("1. Вверх")
    print("2. Вниз")
    print("3. Налево")
    print("4. Направо")
    print("5. Отойти")
    choice = input("На какую позицию сдвинуть статую?")
    if choice == "1":
        print("Вы передвинули статую на верхнюю позицию")
        inv.append("1")
        complete()
    elif choice == "2":
        print("Вы передвинули статую на нижнюю позицию")
        statues()
    elif choice == "3":
        print("Вы передвинули статую на левую позицию")
        statues()
    elif choice == "4":
        print("Вы передвинули статую на правую позицию")
        statues()
    elif choice == "5":
        statues()
    else:
        print("Некорректный ввод.")
        eagle()


def owl():
    print("Вы подошли к статуе Совы")
    print("Похоже, нужно сдвинуть ее на правильное место...")
    print("1. Вверх")
    print("2. Вниз")
    print("3. Налево")
    print("4. Направо")
    print("5. Отойти")
    choice = input("На какую позицию сдвинуть статую?")
    if choice == "1":
        print("Вы передвинули статую на верхнюю позицию")
        statues()
    elif choice == "2":
        print("Вы передвинули статую на нижнюю позицию")
        statues()
    elif choice == "3":
        print("Вы передвинули статую на левую позицию")
        statues()
    elif choice == "4":
        print("Вы передвинули статую на правую позицию")
        inv.append("2")
        complete()
    elif choice == "5":
        statues()
    else:
        print("Некорректный ввод.")
        owl()


def lion():
    print("Вы подошли к статуе Льва")
    print("Похоже, нужно сдвинуть ее на правильное место...")
    print("1. Вверх")
    print("2. Вниз")
    print("3. Налево")
    print("4. Направо")
    print("5. Отойти")
    choice = input("На какую позицию сдвинуть статую?")
    if choice == "1":
        print("Вы передвинули статую на верхнюю позицию")
        statues()
    elif choice == "2":
        print("Вы передвинули статую на нижнюю позицию")
        statues()
    elif choice == "3":
        print("Вы передвинули статую на левую позицию")
        inv.append("3")
        complete()
    elif choice == "4":
        print("Вы передвинули статую на правую позицию")
        statues()
    elif choice == "5":
        statues()
    else:
        print("Некорректный ввод.")
        lion()


def horse():
    print("Вы подошли к статуе Лошади")
    print("Похоже, нужно сдвинуть ее на правильное место...")
    print("1. Вверх")
    print("2. Вниз")
    print("3. Налево")
    print("4. Направо")
    print("5. Отойти")
    choice = input("На какую позицию сдвинуть статую?")
    if choice == "1":
        print("Вы передвинули статую на верхнюю позицию")
        statues()
    elif choice == "2":
        print("Вы передвинули статую на нижнюю позицию")
        statues()
    elif choice == "3":
        print("Вы передвинули статую на левую позицию")
        inv.append("4")
        complete()
    elif choice == "4":
        print("Вы передвинули статую на правую позицию")
        statues()
    elif choice == "5":
        statues()
    else:
        print("Некорректный ввод.")
        horse()


def statues():
    print("Перед вами 4 статуи, к какой хотите подойти?")
    print("1. Орел")
    print("2. Сова")
    print("3. Лев")
    print("4. Лошадь")
    choice = input("Подойти к статуе номер: ")
    if choice == "1":
        eagle()
    elif choice == "2":
        owl()
    elif choice == "3":
        lion()
    elif choice == "4":
        horse()
    else:
        print("Некорректный ввод.")
        statues()


def stage1():
    print("Вас ослепляет сильно освещенная комната"
          "\nПривыкнув к свету, вы видите перед собой 4 статуи: Орла, Совы, Льва и Лошади, а за ними большую дверь"
          "\nПодойдя к двери вы видите рядом с ней букву N, а под ней лежит записка:"
          "\nКороль всех птиц летел выше Совы."
          "\nКонь не хотел спать, поэтому он бежал от темноты на Запад."
          "\nСова летела тихо, подобно шепоту в темноте. Она натолкнулась на реку и отправилась на Юг."
          "\nЧетырехногий хищник крался к своей добыче. Он готов напасть в любой момент."
          "\nМожет, это загадка?")
    statues()


def explore_door():
    print("Вы подходите к странной двери и пробуете ее открыть, но она заперта.")
    if "Ключ" in inv:
        print("Вы отпираете дверь ключом, найденным в сундуке, и проходите дальше.")
        stage1()
    else:
        print("У вас нет ключа...")
        print("Попробовать выбить?"
              "\n1.Да"
              "\n2.Нет")
        choice = input()
        if choice == "1":
            print("Вы попытались выбить дверь, ударив по ней ногой со всей силы"
                  "\nВы почувствовали невыносимую боль"
                  "\nЧерез время вы перестали чувствовать боль, впрочем, вы перестали вообще что-либо чувствовать...")
            print("ВЫ ПОГИБЛИ")
            game_state = {
                "Имя:": name,
                "Причина смерти:": "Потеря крови от перелома",
                "Дата:": data
            }
            savCsv(game_state, 'saves.csv')
            save_game(game_state, 'saves.json')
            exit()
        elif choice == "2":
            print("Вам нужно найти этот ключ")
            explore_room()


def explore_diary():
    print("Вы находите старый дневник."
          "\nВы приступаете к чтению..."
          "\nВ дневнике описаны загадочные события, происходившие в этой комнате."
          "\nОднако, некоторые страницы сильно повреждены и прочитать их невозможно."
          "\nВдруг на одной из страниц вы замечаете цифры: 1602."
          "\nИнтересно, зачем они?")
    inv.append("Код")
    print("Рядом с дневником вы замечаете бутылку вина"
          "\nОна выглядит довольно новой. Выпить?"
          "\n1.Да"
          "\n2.Нет")
    choice = input()
    if choice == "1":
        print("Вы выпиваете вино. Внезапно вы чувствуете помутнение в глазах и падаете на землю")
        print("ВЫ ПОГИБЛИ")
        game_state = {
            "Имя:": name,
            "Причина смерти:": "Отравление",
            "Дата:": data
        }
        savCsv(game_state, 'saves.csv')
        save_game(game_state, 'saves.json')
        exit()
    elif choice == "2":
        print("Вы продолжаете исследование комнаты.")
        explore_room1()


def explore_chest():
    print("Вы обнаруживаете старый сундук."
          "\nСундук заперт на замок, требующий код.")
    if "Код" in inv:
        print("В прочтенном дневнике вы нашли цифры, может они подойдут?"
              "\nВы открыли сундук, и в нем оказался ключ!")
        inv.remove("Код")
        inv.append("Ключ")
        explore_room2()
    else:
        print("Вы не знаете код, может он где-то спрятан?")
        explore_room()


def story():
    print("Вы очнулись в странном месте..."
          "\nВокруг вас темно и неизвестно, что произошло."
          "\nВаша цель - выбраться отсюда.")
    print()
    print("Выберите действие:")
    print("1. Исследовать комнату.")
    print("2. Позвать на помощь.")
    choice = input("Введите номер действия: ")
    if choice == "1":
        explore_room()
    elif choice == "2":
        call_for_help()
    else:
        print("Некорректный ввод. Попробуйте еще раз.")
        story()

story()