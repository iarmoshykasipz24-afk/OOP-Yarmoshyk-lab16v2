from time import perf_counter

import data
import queries as q

REPEATS = 1000


def stopwatch(func, *args):
    """Аналог Stopwatch: повертає результат і час виконання в мікросекундах."""
    start = perf_counter()
    result = func(*args)
    return result, (perf_counter() - start) * 1_000_000


def average_us(func, *args, repeats: int = REPEATS) -> float:
    start = perf_counter()
    for _ in range(repeats):
        func(*args)
    return (perf_counter() - start) * 1_000_000 / repeats


def show(result) -> None:
    if isinstance(result, list):
        for item in result:
            print(f"      {item}")
    else:
        print(f"      {result}")


def run_query(title: str, query_func, method_func, students, courses) -> None:
    print(f"\n--- {title} ---")
    r1, t1 = stopwatch(query_func, students, courses)
    r2, t2 = stopwatch(method_func, students, courses)
    print("  Синтаксис запитів (comprehension):")
    show(r1)
    print(f"    Час (перший запуск): {t1:.1f} мкс")
    print("  Синтаксис методів (filter/map/min):")
    show(r2)
    print(f"    Час (перший запуск): {t2:.1f} мкс")
    print(f"  Результати збігаються: {r1 == r2}")
    a1 = average_us(query_func, students, courses)
    a2 = average_us(method_func, students, courses)
    print(f"  Середній час за {REPEATS} запусків: запити = {a1:.2f} мкс, методи = {a2:.2f} мкс")


def main() -> None:
    courses = data.create_courses()
    students = data.create_students()
    print(f"Тестові дані: {len(students)} студентів, {len(courses)} курсів")

    print("\n================ ЧАСТИНА 1. Запити на тестових даних ================")
    run_query("Запит 1: студенти до 20 років на курсі 'Programming Basics'",
              q.q1_query, q.q1_method, students, courses)
    run_query("Запит 2: join студентів із курсами",
              q.q2_query, q.q2_method, students, courses)
    run_query("Запит 3: кількість студентів на кожному курсі",
              q.q3_query, q.q3_method, students, courses)
    run_query("Запит 4: наймолодший студент",
              q.q4_query, q.q4_method, students, courses)

    big_students, big_courses = data.create_large_data(200_000, 200)
    print(f"\n================ ЧАСТИНА 2. Великий набір даних: "
          f"{len(big_students)} студентів, {len(big_courses)} курсів ================")
    print("Час одного виконання, мс:")
    for name, qf, mf in [
        ("Запит 1 (фільтр)", q.q1_query, q.q1_method),
        ("Запит 2 (join)", q.q2_query, q.q2_method),
        ("Запит 3 (підрахунок)", q.q3_query, q.q3_method),
        ("Запит 4 (мінімум)", q.q4_query, q.q4_method),
    ]:
        _, t1 = stopwatch(qf, big_students, big_courses)
        _, t2 = stopwatch(mf, big_students, big_courses)
        print(f"  {name:<22} запити = {t1 / 1000:8.2f} мс | методи = {t2 / 1000:8.2f} мс")

    print("\n================ ЧАСТИНА 3. Неефективні підходи (20 000 студентів, 200 курсів) ================")
    mid_students, mid_courses = data.create_large_data(20_000, 200)
    pairs = [
        ("Join: хеш-таблиця", q.q2_query, "Join: вкладені цикли", q.q2_nested_loop_join),
        ("Підрахунок: Counter", q.q3_query, "Підрахунок: прохід для кожного курсу", q.q3_count_per_course_naive),
        ("Мінімум: min()", q.q4_method, "Мінімум: sorted()[0]", q.q4_sorted_first),
    ]
    for good_name, good, bad_name, bad in pairs:
        _, tg = stopwatch(good, mid_students, mid_courses)
        _, tb = stopwatch(bad, mid_students, mid_courses)
        print(f"  {good_name:<24} {tg / 1000:8.2f} мс | {bad_name:<38} {tb / 1000:8.2f} мс | "
              f"повільніше у {tb / tg:5.1f} раза")


if __name__ == "__main__":
    main()
