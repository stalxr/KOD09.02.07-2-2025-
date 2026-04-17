# Мастер пол - Система управления партнерами

Django-приложение для управления партнерами, продукцией и историей продаж компании "Мастер пол".

## Требования

- Python 3.10+
- PostgreSQL 12+
- pgAdmin 4 (для управления БД)

## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/stalxr/KOD09.02.07-2-2025-.git
cd KOD_PROJECT
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка PostgreSQL в pgAdmin 4

1. Откройте pgAdmin 4
2. Подключитесь к серверу PostgreSQL
3. Создайте базу данных `master_pol`:
   - Правой кнопкой на "Databases" → Create → Database
   - Имя базы: `master_pol`
   - Owner: `postgres`
   - Нажмите Save

### 5. Применение миграций

```bash
python manage.py migrate
```

### 6. Импорт данных из Excel

```bash
python manage.py import_excel
```

### 7. Создание суперпользователя

```bash
python manage.py createsuperuser
```

Введите:
- Username: admin
- Email: (можно оставить пустым)
- Password: (ваш пароль)

### 8. Запуск сервера

```bash
python manage.py runserver
```

Откройте в браузере: http://127.0.0.1:8000/

## Функционал

- **Партнеры**: список партнеров с расчетом скидок на основе объема продаж
- **Продукция**: каталог продукции компании
- **История продаж**: история реализации продукции партнерам
- **Авторизация**: вход/выход для управления данными

## Структура проекта

```
KOD_PROJECT/
├── main/                   # Основное приложение
│   ├── models.py          # Модели БД
│   ├── views.py           # Представления
│   ├── urls.py            # Маршруты
│   ├── admin.py           # Настройка админки
│   └── management/        # Команды управления
├── master_pol/            # Настройки проекта
├── templates/             # HTML шаблоны
├── static/                # CSS, изображения
├── manage.py              # Управление проектом
└── requirements.txt       # Зависимости
```

## Стилизация

- Шрифт: Segoe UI
- Основной фон: #FFFFFF (белый)
- Дополнительный фон: #F4E8D3 (бежевый)
- Акцентный цвет: #67BA80 (зеленый)
- Логотип: Мастер пол (из ресурсов)

## Доступ к админке

http://127.0.0.1:8000/admin/

Логин: admin
Пароль: (тот что создали при createsuperuser)
