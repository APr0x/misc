def find_unique(iterable):
    seen = set()  # Множество всех встреченных элементов
    unique = set()  # Множество элементов, встречающихся только один раз

    for item in iterable:
        if item in seen:
            # Если элемент уже встречался, удаляем его из уникальных
            unique.discard(item)
        else:
            # Если элемент встречается впервые, добавляем в оба множества
            seen.add(item)
            unique.add(item)

    # Возвращаем отсортированный список уникальных элементов
    return sorted(unique)


# Пример использования
if __name__ == "__main__":
    data = [3, 5, 2, 3, 8, 5, 10, 1]
    print("Уникальные элементы:", find_unique(data))
