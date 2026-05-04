# 🤖 MultiModal Telegram Bot Assistant

Умный Telegram-бот с поддержкой текста, голоса, изображений и базы знаний (RAG).

## ✨ Возможности

### 🔤 Текстовый режим
- Ответы на вопросы через GPT-4o
- Поддержка контекста диалога
- История сообщений

### 🎤 Голосовой режим
- Распознавание речи (Whisper)
- Синтез речи (TTS) - 6 голосов на выбор
- Голосовой ответ на голосовое сообщение

### 📸 Анализ изображений
- Распознавание объектов и сцен
- Извлечение текста из документов (OCR)
- Анализ диаграмм и графиков

### 📚 База знаний (RAG)
- Загрузка PDF, TXT, MD документов
- Семантический поиск по документам
- Ответы с указанием источников
- Интеграция с ChromaDB

### 🎨 Генерация изображений
- DALL-E 3 для создания изображений
- Автоматическое определение запросов на генерацию
- Сохранение сгенерированных изображений

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий
```bash
git clone <repository-url>
cd ego-assistflow
```

### 2. Создайте виртуальное окружение
```powershell
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

### 4. Настройте API ключи
```powershell
# Скопируйте пример и отредактируйте
copy .env.example .env
notepad .env
```

Добавьте в `.env`:
```env
TELEGRAM_BOT_TOKEN=ваш_токен_бота
OPENAI_API_KEY=ваш_ключ_proxyapi
USE_PROXYAPI=true
```

### 5. Запустите бота
```bash
python main.py
```

## 📖 Документация

### Основные руководства

| Документ | Описание |
|----------|----------|
| [START_HERE.md](START_HERE.md) | 📘 С чего начать - первое знакомство |
| [QUICKSTART.md](QUICKSTART.md) | ⚡ Быстрые команды для запуска |
| [README_VENV.md](README_VENV.md) | 🐍 Работа с виртуальным окружением |
| [PROXYAPI_SETUP.md](PROXYAPI_SETUP.md) | 🔑 Настройка ProxyAPI (для РФ) |

### Специализированные руководства

| Документ | Описание |
|----------|----------|
| [RAG_GUIDE.md](RAG_GUIDE.md) | 📚 База знаний и семантический поиск |
| [README_IMAGE_GENERATION.md](README_IMAGE_GENERATION.md) | 🎨 Генерация изображений |
| [VISUAL_GUIDE.md](VISUAL_GUIDE.md) | 🎯 Визуальная схема архитектуры |

### Структура проекта

```
ego-assistflow/
├── main.py                 # Точка входа
├── bot.py                  # Инициализация бота
├── config.py               # Конфигурация
├── requirements.txt        # Зависимости
│
├── handlers/               # Обработчики команд
│   ├── start.py           # /start, /help
│   ├── text.py            # Текстовые сообщения
│   ├── voice.py           # Голосовые сообщения
│   ├── image.py           # Изображения
│   └── document_upload.py # Загрузка документов
│
├── services/               # Сервисы
│   ├── openai_client.py   # Клиент OpenAI
│   ├── stt.py             # Speech-to-Text
│   ├── tts.py             # Text-to-Speech
│   ├── vision.py          # Анализ изображений
│   ├── image_generation.py# Генерация изображений
│   └── router.py          # Маршрутизация запросов
│
├── rag/                    # База знаний
│   ├── index.py           # Векторный индекс
│   ├── loader.py          # Загрузчик документов
│   └── query.py           # Обработка запросов
│
├── utils/                  # Утилиты
│   ├── helpers.py         # Вспомогательные функции
│   └── logging.py         # Логирование
│
├── data/                   # Данные
│   ├── documents/         # Ваши документы для RAG
│   ├── chroma_db/         # База векторных embeddings
│   └── generated_images/  # Сгенерированные изображения
│
└── tests/                  # Тесты
    ├── test_text.py
    ├── test_stt.py
    ├── test_rag.py
    └── test_image_generation.py
```

### Команды бота

| Команда | Описание |
|---------|----------|
| `/start` | Приветствие и описание возможностей |
| `/help` | Подробное руководство |
| `/mode <режим>` | Переключение режима (text/voice/vision/rag) |
| `/voice <голос>` | Выбор голоса для TTS |
| `/reset` | Очистка истории диалога |
| `/stats` | Статистика базы знаний |
| `/voices` | Список доступных голосов |

### Режимы работы

| Режим | Описание |
|-------|----------|
| `text` | Обычный текстовый режим (по умолчанию) |
| `voice` | Голосовой режим - ответы голосом |
| `vision` | Анализ изображений |
| `rag` | Работа с базой знаний |

### Доступные голоса (TTS)

| Голос | Описание |
|-------|----------|
| `alloy` | Нейтральный (по умолчанию) |
| `echo` | Мужской |
| `nova` | Женский |
| `fable` | Мужской (британский акцент) |
| `onyx` | Мужской (глубокий) |
| `shimmer` | Женский (теплый) |

## 🧪 Тестирование

```bash
# Запустить все тесты
python -m pytest tests/ -v

# Тестирование ProxyAPI
python test_proxyapi.py

# Индексация документов
python index_documents.py
```

## 🔧 Конфигурация

### Переменные окружения (.env)

```env
# Telegram Bot Token
TELEGRAM_BOT_TOKEN=your_bot_token_here

# OpenAI / ProxyAPI
OPENAI_API_KEY=your_api_key_here
USE_PROXYAPI=true

# Настройки бота
BOT_MODE=text
DEFAULT_VOICE=alloy
LOG_LEVEL=INFO
```

### Основные настройки (config.py)

| Параметр | Значение | Описание |
|----------|----------|----------|
| `GPT_MODEL` | `gpt-4o` | Основная модель |
| `WHISPER_MODEL` | `whisper-1` | Модель распознавания речи |
| `TTS_MODEL` | `tts-1` | Модель синтеза речи |
| `VISION_MODEL` | `gpt-4o` | Модель анализа изображений |
| `DALLE_MODEL` | `dall-e-3` | Модель генерации изображений |
| `RAG_CHUNK_SIZE` | `1000` | Размер фрагментов для RAG |
| `MAX_HISTORY_LENGTH` | `10` | Длина истории диалога |

## 📊 Статистика

- ✅ 49 тестов пройдено
- 📚 Поддержка 8+ языков программирования
- 🎤 6 голосов для TTS
- 📄 PDF, TXT, MD документы для RAG
- 🖼️ DALL-E 3 для генерации изображений

## 🛠️ Технологии

- **Python 3.10+**
- **pyTelegramBotAPI 4.x** - Telegram Bot API
- **OpenAI SDK** - GPT-4, Whisper, TTS, DALL-E
- **LangChain** - RAG и векторные базы
- **ChromaDB** - векторная база данных
- **pydub** - обработка аудио

## 📝 Лицензия

MIT License

## 🤝 Вклад

Приветствуются Pull Requests! Пожалуйста, прочитайте CONTRIBUTING.md перед началом.

## 📞 Поддержка

- [ProxyAPI Setup](PROXYAPI_SETUP.md) - настройка для работы в РФ
- [RAG Guide](RAG_GUIDE.md) - работа с базой знаний
- [QuickStart](QUICKSTART.md) - быстрые команды

---

**Создано с ❤️ для умной автоматизации**
