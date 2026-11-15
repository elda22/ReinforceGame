import random


STARTING_BALANCE = 1000


def attempt_reinforcement(
    weapons: list[dict],
    current_weapon_index: int,
    balance: int,
    highest_weapon_index: int,
) -> tuple[int, int, int, str]:
    """강화 결과와 변경된 상태, 안내 메시지 키를 반환한다."""
    if current_weapon_index >= len(weapons) - 1:
        return current_weapon_index, balance, highest_weapon_index, "max_level_message"

    next_weapon = weapons[current_weapon_index + 1]
    reinforcement_cost = next_weapon["reinforcement_cost"]
    if balance < reinforcement_cost:
        return current_weapon_index, balance, highest_weapon_index, "insufficient_balance"

    balance -= reinforcement_cost
    if random.randint(1, 100) <= next_weapon["success_rate"]:
        current_weapon_index += 1
        if current_weapon_index > highest_weapon_index:
            highest_weapon_index = current_weapon_index
            message_key = "weapon_unlocked"
        else:
            message_key = "reinforcement_success"
    else:
        current_weapon_index = max(0, current_weapon_index - 1)
        message_key = "reinforcement_failure"

    return current_weapon_index, balance, highest_weapon_index, message_key


def sell_current_weapon(
    weapons: list[dict], current_weapon_index: int, balance: int
) -> tuple[int, int]:
    """무기를 판매하고 초기 무기와 변경된 잔액을 반환한다."""
    current_weapon = weapons[current_weapon_index]
    balance += current_weapon["sale_price"]
    return 0, balance
