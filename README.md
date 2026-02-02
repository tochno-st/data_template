# Стандартый шаблон проекта Если быть точным

Шаблон [Cookiecutter](https://github.com/cookiecutter/cookiecutter) для проектов Если быть точным с автоматическим созданием виртуального окружения и установкой Python-пакетов.

## Возможности

- Стандартизированная структура проекта
- Автоматическое создание виртуального окружения (`.venv`)
- Умное определение пакетного менеджера: использует [uv](https://github.com/astral-sh/uv) при наличии, иначе pip
- Готовность к работе с Jupyter notebooks — `ipykernel` включен по умолчанию
- Возмодность установить нужные пакеты в виртуальное окружение на этапе создания папки

## Требования

- Python 3.7+
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)

### Установка Cookiecutter

#### macOS

```bash
# Через Homebrew (рекомендуется)
brew install cookiecutter

# Или через pip
pip install cookiecutter
```

#### Linux (Ubuntu)

```bash
# Через apt
sudo apt install cookiecutter

# Или через pip
pip install cookiecutter
```

#### Windows

```powershell
# Через pip
pip install cookiecutter
```

> **Примечание:** На Windows рекомендуется использовать PowerShell или Windows Terminal.

## Использование

### Стандартный способ

```bash
cookiecutter /путь/к/data_template
```

### Настройка быстрого алиаса

Добавьте алиас в конфигурацию вашей оболочки для быстрого доступа.

**Для Zsh (`~/.zshrc`):**
```bash
alias tbtemp='cookiecutter /путь/к/data_template'
```

**Для Bash (`~/.bashrc`):**
```bash
alias tbtemp='cookiecutter /путь/к/data_template'
```

Замените `/путь/к/data_template` на актуальный путь к директории шаблона.

Перезагрузите конфигурацию оболочки:
```bash
source ~/.zshrc  # для Zsh
source ~/.bashrc # для Bash
```

Теперь можно создавать новые проекты одной командой:
```bash
tbtemp
```

## Структура проекта

Сгенерированные проекты имеют следующую структуру:

| Директория | Назначение |
|------------|------------|
| `data/raw` | Исходные файлы данных. **Никогда не изменяйте** — считайте неизменяемыми |
| `data/interim` | Промежуточные данные, прошедшие трансформацию |
| `data/processed` | Финальные наборы данных для анализа или моделирования |
| `data/external` | Данные из сторонних источников |
| `notebooks` | Jupyter-ноутбуки для исследования и анализа |
| `reports` | Сгенерированные отчеты, графики и документация |
| `src` | Переиспользуемый Python-код, модули и скрипты |

## Переменные шаблона

При создании нового проекта вам будет предложено ввести следующие значения:

| Переменная | Описание | По умолчанию |
|------------|----------|--------------|
| `directory_name` | Название папки проекта | `gather_data` |
| `author_name` | Ваше имя или название организации | - |
| `description` | Краткое описание проекта | - |
| `python_packages` | Пакеты для установки через пробел | `ipykernel pandas matplotlib` |

### Пример

```
$ tbtemp
directory_name [gather_data]: my_analysis
author_name [Your name]: Иван Иванов
description [A short description]: Анализ данных продаж Q4 2024
python_packages [ipykernel pandas matplotlib]: ipykernel pandas numpy scikit-learn seaborn
```

## После генерации

После создания проекта шаблон автоматически:

1. Создает виртуальное окружение `.venv`
2. Устанавливает указанные Python-пакеты
3. Выводит инструкции по активации

### Активация окружения

```bash
# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Приоритет пакетных менеджеров

Шаблон использует следующий приоритет для установки пакетов:

1. **uv** (если установлен) — сверхбыстрый пакетный менеджер на Rust
2. **pip** (запасной вариант) — стандартный пакетный менеджер Python

Для ускорения создания проектов установите [uv](https://github.com/astral-sh/uv):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Использование с Jupyter Hub

Если вы работаете в Jupyter Hub и не имеете доступа к терминалу на локальной машине, выполните следующие шаги:

### 1. Откройте терминал в Jupyter Hub

В интерфейсе Jupyter Hub: **File → New → Terminal**

### 2. Установите cookiecutter (если не установлен)

```bash
pip install --user cookiecutter
```

### 3. Склонируйте шаблон

```bash
git clone <url-репозитория-шаблона> ~/data_template
```

### 4. Настройте быстрый алиас (опционально)

Чтобы каждый раз не вводить полный путь, добавьте алиас в `~/.bashrc`:

```bash
echo "alias tbtemp='cookiecutter ~/data_template'" >> ~/.bashrc
source ~/.bashrc
```

Теперь для создания нового проекта достаточно команды `tbtemp`.

### 5. Создайте проект

```bash
cookiecutter ~/data_template
```

### 6. Подключите ядро к Jupyter Hub

После создания проекта перейдите в его директорию и зарегистрируйте виртуальное окружение как ядро Jupyter:

```bash
cd имя_проекта
source .venv/bin/activate
python -m ipykernel install --user --name=имя_проекта --display-name="Python (имя_проекта)"
```

Теперь в Jupyter Hub при создании нового notebook можно выбрать ядро **"Python (имя_проекта)"** с установленными пакетами.

### Удаление ядра

Если ядро больше не нужно:

```bash
jupyter kernelspec uninstall имя_проекта
```

## Кастомизация

### Изменение пакетов по умолчанию

Отредактируйте `cookiecutter.json` для изменения пакетов по умолчанию:

```json
{
    "python_packages": "ipykernel pandas numpy matplotlib seaborn"
}
```

### Добавление новых директорий

Отредактируйте шаблон в `{{cookiecutter.directory_name}}/` для добавления новых папок или файлов во все генерируемые проекты.

## Доработки шаблона

- [ ] Добавить автоматизацию работы с файлами данных
- [ ] Добавить упрощенную версию шаблона

