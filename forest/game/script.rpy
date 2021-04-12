# Вы можете расположить сценарий своей игры в этом файле.
define i = Character("Я")

label phone:

    if phone.mode:
        menu:
            "Выключить телефон?"

            "Да":
                $ phone.turn_off()
            "Нет":
                return

    else:
        menu:
            "Включить телефон?"

            "Да":
                $ phone.turn_on()
            "Нет":
                return

    $ MyReturn()()
    return

label hoodie:

    if hoodie.mode:
        menu:
            "Снять кофту?"

            "Да":
                $ hoodie.put_off()
            "Нет":
                return

    else:
        menu:
            "Надеть кофту?"

            "Да":
                $ hoodie.put_on()
            "Нет":
                return

    $ MyReturn()()
    return

label basket:

    menu:
        "Оставить корзину?"

        "Да":
            $ basket.leave()
        "Нет":
            return

    $ MyReturn()()
    return

label water:

    menu:
        "Выпить воды?"

        "Да":
            $ bottle.drink()
        "Нет":
            return

    $ MyReturn()()
    return


# Игра начинается здесь:
label start:

    "Мы с друзьями отправились за грибами в лес."
    #тут будет картинка
    "Год выдался богатый на грибы, и мы быстро все разбрелись, стараясь собрать побольше."
    "И через какое-то время я поняла, что потерялась."
    #тут будет картинка
    i "Ау!"
    i "АУ!"
    i "Ау! Кто-нибудь!"
    "Вот так я оказалась одна посреди леса, с одним только телефоном на руках. Связи, впрочем, ожидаемо нет"
    "Хорошо ещё, что у меня с собой была бутылка воды, а то на такой жаре могло сосвем туго стать."
    "Может снять кофту?"

    call screen info("Вы можете взаимодействовать с объектами через инвентарь. Состояния предметов по разному влияют на параметры. Например, при надетой кофте будет быстрее падать жажда.")


    show screen inventory
    show screen using_stats
    i "АУУУУ!"
    "Никого нет. Видимо, я совсем заблудилась."
    "Ну ничего, когда все поймут, что я тут потерялась, они вызовут МЧС."
    "Надо только дождаться, пока меня вытащят отсюда."
    "Да..."
    menu:
        "Может, пока попытаться выбраться самой?"

        "Оставаться на месте":
            $ me.time_in_forest += 1

        "Поискать выход":
            jump finding_way

    "Оставаться на месте безопаснее."
    "Так я не заблужусь ещё сильнее."

    pause 1

    "Начинает становиться скучно."

    menu:
        "Может, всё-таки поискать дорогу?"

        "Оставаться на месте":
            $ me.time_in_forest += 1

        "Поискать выход":
            jump finding_way

    "Да, всё-таки стоит остаться тут. Так меня быстрее найдут."
    "А скуку как-нибудь переживу."

    pause 1

    "Скука становиться невыносимой."
    "Вокруг меня такой живописный лес, а я торчу на одном месте."
    "Всё равно я слишком далеко никуда не уйду."

    menu:
        "Кажется, всё-таки стоит куда-нибудь пойти."

        "Оставаться на месте":
            $ me.time_in_forest += 1

        "Поискать выход":
            jump finding_way


    "Правильно, надо ждать и верить, что меня найдут"

    pause 1

    #тут будет картинка лося
    "Ой! Наверное, всё же стоит уйти."
    "Но можно сделать фото напоследок, не каждый день встречаешь лося"

    jump moose


label moose:

    menu:
        "Сделать фото?"

        "Да, конечно!":
            if phone_mode:
                $ photos += ["moose"]
                $ check_phone()
                "Класс, у меня теперь есть фотка лося!"
                jump finding_way
            else:
                "Эх, телефон выключен"
                jump moose

        "Нет, не стоит":
            "Нет, лучше поберегу заряд на телефоне, он ещё может пригодиться"
            jump finding_way


label finding_way:

    "Ну ладно. Значит в путь!"
    "Кажется, дорога должна быть где-то впереди"

    jump in_maze

label in_maze:

    "Куда пойти дальше?"

    call screen ways()

label go_down:

    show screen inventory
    show screen using_stats

    if not maze.go_down():
        jump fainting
    jump in_maze

label go_up:

    show screen inventory
    show screen using_stats

    if not maze.go_up():
        jump fainting
    if maze.pos == 0:
        jump road
    jump in_maze

label go_right:

    show screen inventory
    show screen using_stats

    if not maze.go_right():
        jump fainting
    jump in_maze

label go_left:

    show screen inventory
    show screen using_stats

    if not maze.go_left():
        jump fainting
    jump in_maze

label road:

    "Я вышла к дороге!"

    return

label fainting:

    "Что-то мне нехорошо"

    scene black with fade

    "Очнулась в больнице, концовку допишу"
    return
