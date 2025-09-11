

def level_up(experience: int, threshold: int, reward: int) -> bool:
    return experience + reward >= threshold


def motor_time(n: int) -> int:

    total_minutes = 24 * 60
    minutes_pass = n % total_minutes
    hours = minutes_pass // 60
    minutes = minutes_pass % 60
    time_str = f'{hours:02d}{minutes:02d}'
    return sum(map(int, time_str))


def time_converter(time_str: str) -> str:

    time_parts = time_str.split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    if hours < 12:
        period = "a.m."
    else:
        period = "p.m."
    if hours == 0:
        hours = 12
    if hours > 12:
        hours -= 12
    return f'{hours}:{minutes:02d} {period}'
