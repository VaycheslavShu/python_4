from datetime import datetime, timedelta


def date_range(start_date: str, end_date: str) -> list:

    fmt = '%Y-%m-%d'

    try:
        start = datetime.strptime(start_date, fmt)
        end = datetime.strptime(end_date, fmt)
    except (ValueError, TypeError):
        return []

    if start > end:
        return []

    result = []
    current = start
    while current <= end:
        result.append(current.strftime(fmt))
        current += timedelta(days=1)

    return result


def main() -> None:

    start_date = input('Введите начальную дату (YYYY-MM-DD): ').strip()
    end_date = input('Введите конечную дату (YYYY-MM-DD): ').strip()

    result = date_range(start_date, end_date)

    if result:
        print(result)
    else:
        print('Пустой список: неверный формат или start_date > end_date.')


if __name__ == '__main__':
    main()