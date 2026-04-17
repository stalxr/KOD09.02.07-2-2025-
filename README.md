# Мастер пол - Система управления партнерами

Django-приложение для управления партнерами, продукцией и историей продаж компании "Мастер пол".

## Требования

- Python 3.10+
- PostgreSQL 12+
- pgAdmin 4 (опционально)

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

### 4. Настройка PostgreSQL

**Вариант А - Восстановление из бэкапа:**
```bash
# В pgAdmin 4 или psql:
# 1. Создайте базу master_pol
# 2. Восстановите из файла:
psql -U postgres -d master_pol -f db_er_backup/postgrebackup_db.sql
```

**Вариант Б - Новая база с нуля:**
1. Создайте базу `master_pol` в PostgreSQL
2. Выполните миграции: `python manage.py migrate`
3. Импортируйте данные: `python manage.py import_excel`

Настройки подключения в `master_pol/settings.py`:
- База: `master_pol`
- Пользователь: `postgres`
- Пароль: `postgres`
- Хост: `localhost`
- Порт: `5432`

### 5. Запуск сервера

```bash
python manage.py runserver
```

Откройте: http://127.0.0.1:8000/

## Доступ к админке

http://127.0.0.1:8000/admin/

Дефолтные пользователи (создаются автоматически):
- **admin** / admin123 (суперпользователь)
- **manager** / manager123

## Функционал

- **Партнеры**: список партнеров с расчетом скидок
- **Продукция**: каталог продукции
- **История продаж**: история реализации продукции
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
├── db_er_backup/          # ER-диаграмма и бэкап БД
│   ├── er-diagramm        # ER-диаграмма базы данных
│   └── postgrebackup_db.sql  # SQL бэкап базы
├── manage.py              # Управление проектом
└── requirements.txt       # Зависимости
```

## Документация БД

- **ER-диаграмма**: `db_er_backup/er-diagramm`
- **SQL бэкап**: `db_er_backup/postgrebackup_db.sql`

## Стилизация

- Шрифт: Segoe UI
- Основной фон: #FFFFFF
- Дополнительный фон: #F4E8D3
- Акцентный цвет: #67BA80
