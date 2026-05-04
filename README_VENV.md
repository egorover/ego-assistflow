# Настройка виртуального окружения

## Создание виртуального окружения

```powershell
# Создать виртуальное окружение
python -m venv .venv

# Активировать (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Активировать (CMD)
.venv\Scripts\activate.bat

# Активировать (Linux/Mac)
source .venv/bin/activate
```

## Установка зависимостей

```powershell
# После активации .venv
pip install -r requirements.txt
```

## Или все сразу (без активации)

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Запуск бота

```powershell
# Способ 1: С активацией
.\.venv\Scripts\Activate.ps1
python main.py

# Способ 2: Без активации
.\.venv\Scripts\python.exe main.py
```

## Запуск тестов

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v
```

## Индексация документов

```powershell
.\.venv\Scripts\python.exe index_documents.py
```

## Проверка ProxyAPI

```powershell
.\.venv\Scripts\python.exe test_proxyapi.py
```

## Деактивация виртуального окружения

```powershell
deactivate
```

## Полезные команды

```powershell
# Показать все установленные пакеты
.\.venv\Scripts\python.exe -m pip list

# Обновить все пакеты
.\.venv\Scripts\python.exe -m pip install --upgrade -r requirements.txt

# Сохранить текущие зависимости
.\.venv\Scripts\python.exe -m pip freeze > requirements.txt

# Удалить виртуальное окружение (если нужно пересоздать)
Remove-Item -Recurse -Force .venv
```

## Почему виртуальное окружение?

- **Изоляция зависимостей** - не конфликтует с другими Python проектами
- **Воспроизводимость** - все используют одинаковые версии пакетов
- **Безопасность** - изменения не влияют на системный Python
- **Легкость удаления** - можно удалить .venv и создать заново
