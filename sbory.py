from bs4 import BeautifulSoup
import requests
import telegram
import asyncio
from apscheduler.schedulers.blocking import BlockingScheduler

# Укажите свой токен и ID чата
TOKEN = "YOUR TOKEN"  # Замените на свой токен
CHAT_ID = "-1002211895966"  # Замените на свой ID чата

# Множество для хранения имен подопечных
processed_children = set()


async def send_notification(name, message):
    # Функция для отправки уведомлений через Telegram
    bot = telegram.Bot(token=TOKEN)
    full_message = f"{name} | {message}"
    await bot.send_message(chat_id=CHAT_ID, text=full_message)


async def check_funds():
    global processed_children  # Объявляем, что используем глобальную переменную
    url = "https://aleshafond.ru/children"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    children_cards = soup.find_all('div', class_='col-md-6 col-lg-4 col-xl-3')
    print(f"Запуск проверки статусов\nНайдено подопечных: {len(children_cards)}")

    for card in children_cards:
        # Получаем имя подопечного
        name_element = card.find('span', class_='card-box-cap-txt__name')
        if name_element:
            name = name_element.text.strip()
        else:
            print("Ошибка: Не удалось найти имя подопечного.")
            continue

        # Проверка, закрыт ли сбор
        closed_collection = card.find('b')
        if closed_collection:
            closed_text = closed_collection.text.strip()
            print(f"Найден элемент с закрытым сбором для {name}: {closed_text}")  # Отладочное сообщение
            if closed_text.startswith('Сбор закрыт') and name not in processed_children:
                processed_children.add(name)  # Добавляем имя в множество, чтобы избежать повторных уведомлений
                await send_notification(name, f"{closed_text}")

    print("Проверка завершена.")


async def main():
    # Запуск функции проверки фондов
    await check_funds()


def check_statuses():
    asyncio.run(main())  # Запуск проверки в асинхронном режиме


# Планировщик для проверки каждые 5 минут
scheduler = BlockingScheduler()
scheduler.add_job(check_statuses, 'interval', minutes=1)

# Запуск планировщика
scheduler.start()

