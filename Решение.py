days = [
    "перводневник",
    "трудник",
    "маленькопятница",
    "постработник",
    "отдыхатница",
    "приветник",
    "дружник",
    "семейник",
    "радостник",
    "отсыпальник",
    "релаксенье"
]

today = "семейник"
n = 10522

today_index = days.index(today)
future_index = (today_index + n) % 11

print(f"Сегодня: {today} (номер {today_index})")
print(f"Через {n} дней наступит: {days[future_index]} (номер {future_index})")
