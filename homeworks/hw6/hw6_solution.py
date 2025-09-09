

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

    hours, minutes = time_str.split(':')
    hours = int(hours)
    minutes = int(minutes)
    if hours == 0:
        return f'12:{minutes} a.m.'
    if hours < 12:
        return f'{hours}:{minutes} a.m.'
    if hours == 12:
        return f'12:{minutes} a.m.'
    else:
        return f'{hours-12}:{minutes} a.m.'
