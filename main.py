R1 = 0
R2 = 0
R3 = 0
cmem = []


def commands(index):
    global R1, R2, R3

    command = cmem[index]
    match command["type"]:
        case "mov":  # С помощью этой команды можно переместить значение из ИСТОЧНИКА в ПРИЁМНИК.
            # То есть по сути команда MOV копирует содержимое ИСТОЧНИКА и помещает это содержимое в ПРИЁМНИК.
            match command["arg1"]:
                case "R1":
                    R1 = command["arg2"]
                case "R2":
                    R2 = command["arg2"]
                case "R3":
                    R3 = command["arg2"]
        case "add":  # сложение
            match command["arg1"]:
                case "R1":
                    R1 += command["arg2"]
                case "R2":
                    R2 += command["arg2"]
                case "R3":
                    R3 += command["arg2"]
        case "sub":  # вычитание
            match command["arg1"]:
                case "R1":
                    R1 -= command["arg2"]
                case "R2":
                    R2 -= command["arg2"]
                case "R3":
                    R3 -= command["arg2"]
        case "mul":  # multiply - умножение)
            match command["arg1"]:
                case "R1":
                    R1 *= command["arg2"]
                case "R2":
                    R2 *= command["arg2"]
                case "R3":
                    R3 *= command["arg2"]
        case "div":  # div (divide - деление).
            match command["arg1"]:
                case "R1":
                    R1 /= command["arg2"]
                case "R2":
                    R2 /= command["arg2"]
                case "R3":
                    R3 /= command["arg2"]

    # if command["type"] == "mov":  # С помощью этой команды можно переместить значение из ИСТОЧНИКА в ПРИЁМНИК.
    #     # То есть по сути команда MOV копирует содержимое ИСТОЧНИКА и помещает это содержимое в ПРИЁМНИК.
    #     if command["arg1"] == "R1":
    #         R1 = command["arg2"]
    #     elif command["arg1"] == "R2":
    #         R2 = command["arg2"]
    #     elif command["arg1"] == "R3":
    #         R3 = command["arg2"]
    # elif command["type"] == "add":  # сложение
    #     if command["arg1"] == "R1":
    #         R1 += command["arg2"]
    #     elif command["arg1"] == "R2":
    #         R2 += command["arg2"]
    #     elif command["arg1"] == "R3":
    #         R3 += command["arg2"]
    # elif command["type"] == "sub":  # вычитание
    #     if command["arg1"] == "R1":
    #         R1 -= command["arg2"]
    #     elif command["arg1"] == "R2":
    #         R2 -= command["arg2"]
    #     elif command["arg1"] == "R3":
    #         R3 -= command["arg2"]
    #
    # elif command["type"] == "mul":  # multiply - умножение)
    #     if command["arg1"] == "R1":
    #         R1 *= command["arg2"]
    #     elif command["arg1"] == "R2":
    #         R2 *= command["arg2"]
    # elif command["arg1"] == "R3":
    #     R3 *= command["arg2"]
    # elif command["type"] == "div":  # div (divide - деление).
    #     if command["arg1"] == "R1":
    #         R1 /= command["arg2"]
    # elif command["arg1"] == "R2":
    #     R2 /= command["arg2"]
    # elif command["arg1"] == "R3":
    #     R3 /= command["arg2"]


def execute():
    index = 0
    max_value = 0

    while index < len(cmem):
        print(f'Команда № {index + 1}')
        print("Command:", cmem[index])
        print("Registers: R1 =", R1, "R2 =", R2, "R3 =", R3)
        print("Memory:", cmem)
        commands(index)


        max_value = max(R1, R2, R3)

        index += 1


    print("Maximum Value:", max_value)


cmem = [{"type": "mov", "arg1": "R1", "arg2": 10}, {"type": "mov", "arg1": "R2", "arg2": 5},
        {"type": "add", "arg1": "R3", "arg2": 10}, {"type": "add", "arg1": "R1", "arg2": 3},
        {"type": "add", "arg1": "R2", "arg2": 2},
        {"type": "sub", "arg1": "R1", "arg2": 2}, {"type": "sub", "arg1": "R2", "arg2": 1},
        {"type": "mul", "arg1": "R1", "arg2": 2}, {"type": "mul", "arg1": "R2", "arg2": 3},
        {"type": "div", "arg1": "R1", "arg2": 4}, {"type": "div", "arg1": "R2", "arg2": 2},
        {"type": "mul", "arg1": "R1", "arg2": 50}, {"type": "mul", "arg1": "R1", "arg2": 50}]

execute()
