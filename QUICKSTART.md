# 🚀 Быстрый старт

## Первое использование

### 1. Активировать виртуальное окружение

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Настроить .env файл

```powershell
# Проверить что .env существует
Get-Content .env

# Если нужно - отредактировать
notepad .env
```

### 3. Проверить API ключи

```powershell
.\.venv\Scripts\python.exe test_proxyapi.py
```

### 4. Проиндексировать документы (если нужно)

```powershell
.\.venv\Scripts\python.exe index_documents.py
```

### 5. Запустить бота

```powershell
python main.py
```

---

## Повседневное использование

### Запуск бота

```powershell
# Активация окружения
.\.venv\Scripts\Activate.ps1

# Запуск
python main.py

# Остановка
Ctrl+C
```

### Запуск тестов

```powershell
.\.venv\Scripts\Activate.ps1
python -m pytest tests/ -v
```

### Добавление новых документов

1. Положить файл в `data/documents/`
2. Запустить индексацию:
   ```powershell
   .\.venv\Scripts\python.exe index_documents.py
   ```

---

## Решение проблем

### Ошибка: "cannot load library 'gobject-2.0'"

Установить FFmpeg:
```powershell
winget install ffmpeg
```

### Ошибка: API ключ не работает

```powershell
# Проверить .env
Get-Content .env

# Перепроверить ключ на https://proxyapi.ru
```

### Ошибка: модуль не найден

```powershell
# Переустановить зависимости
.\.venv\Scripts\python.exe -m pip install -r requirements.txt --force-reinstall
```

### Ошибка: база данных заблокирована

```powershell
# Закрыть все процессы Python
Get-Process python | Stop-Process -Force

# Удалить базу и пересоздать
Remove-Item -Recurse -Force data\chroma_db
.\.venv\Scripts\python.exe index_documents.py
```

---

## Команды для копирования

### Полный запуск с нуля

```powershell
.\.venv\Scripts\Activate.ps1
python test_proxyapi.py
python index_documents.py
python main.py
```

### Обновление зависимостей

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade -r requirements.txt
```

### Пересоздание виртуального окружения

```powershell
deactivate
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
