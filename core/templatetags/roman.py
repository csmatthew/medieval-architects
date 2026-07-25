from django import template

register = template.Library()

ROMAN_MAP = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


@register.filter
def roman(value):
    """
    Convert an integer (e.g., 2026) into a Roman numeral (e.g., MMXXVI).
    Usage: {{ 2026|roman }} or {% now "Y"|roman %}
    """
    try:
        num = int(value)
    except (TypeError, ValueError):
        return value  # fail gracefully

    result = []
    for arabic, numeral in ROMAN_MAP:
        while num >= arabic:
            result.append(numeral)
            num -= arabic

    return "".join(result)
