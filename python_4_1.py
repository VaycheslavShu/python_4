from datetime import datetime

from constant import NEWSPAPERS


results = []


def newspapers_strintime(newspapers: list) -> list:
    
    for name, date_str, fmt in newspapers:
        dt = datetime.strptime(date_str, fmt)
        results.append((name, dt, fmt))
    return results

def main(papers: list) -> None:
    
    results = newspapers_strintime(papers)

    for name, dt, fmt in results:
        print(f"{name}: {dt}")


if __name__ == '__main__':
    main(NEWSPAPERS)
