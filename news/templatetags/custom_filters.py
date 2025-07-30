from django import template

register = template.Library()

# Список нежелательных слов для цензуры
BAD_WORDS = [
    'редиска',
    'дурак',
    'негодяй',
]


@register.filter()
def censor(value):
    """
    Фильтр для цензурирования нежелательных слов в тексте.
    Заменяет все буквы слова, кроме первой, на '*'.
    """
    # Проверяем, что на вход пришла именно строка
    if not isinstance(value, str):
        raise TypeError(f"Фильтр 'censor' применяется только к строкам, а не к {type(value)}")

    text = value.split()  # Разбиваем текст на слова
    censored_text = []

    for word in text:
        # Убираем знаки препинания, чтобы они не мешали проверке
        clean_word = word.strip('.,!?;:()')

        # Проверяем, есть ли слово (в нижнем регистре) в нашем списке
        if clean_word.lower() in BAD_WORDS:
            # Если да, цензурируем его
            censored_word = word[0] + '*' * (len(word) - 1)
            censored_text.append(censored_word)
        else:
            # Если нет, оставляем как есть
            censored_text.append(word)

    return ' '.join(censored_text)  # Собираем текст обратно в строку

