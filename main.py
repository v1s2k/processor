R1 = 0
R2 = 0
R3 = 0
cmem = []


def commands(index):
    global R1, R2, R3

    command = cmem[index]
    match command["operation"]:
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
        print("Операция:", cmem[index])
        print("Значение регистров : R1 =", R1, "R2 =", R2, "R3 =", R3)
        print("Состояние памяти:", cmem)
        commands(index)

        max_value = max(R1, R2, R3)

        index += 1

    print("Maximum :", max_value)


def sum_of_registers():
    R1, R2, R3

    return R1 + R2 + R3



cmem = [{"operation": "mov", "arg1": "R1", "arg2": 10}, {"operation": "mov", "arg1": "R2", "arg2": 5},
        {"operation": "add", "arg1": "R3", "arg2": 10}, {"operation": "add", "arg1": "R1", "arg2": 3},
        {"operation": "add", "arg1": "R2", "arg2": 2},
        {"operation": "sub", "arg1": "R1", "arg2": 2}, {"operation": "sub", "arg1": "R2", "arg2": 1},
        {"operation": "mul", "arg1": "R1", "arg2": 2}, {"operation": "mul", "arg1": "R2", "arg2": 3},
        {"operation": "div", "arg1": "R1", "arg2": 4}, {"operation": "div", "arg1": "R2", "arg2": 2},
        {"operation": "mul", "arg1": "R1", "arg2": 50}, {"operation": "mul", "arg1": "R1", "arg2": 50}]

execute()
register_sum = R1+R2+R3
print("Sum of Registers", register_sum)

