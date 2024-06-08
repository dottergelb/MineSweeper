# Игра "Сапер" 🧨

Этот проект реализует классическую игру "Сапер" (Minesweeper) на языке Python с использованием библиотеки Tkinter для графического интерфейса. Игра состоит из поля, на котором расположены мины, и кнопок, которые представляют собой клетки поля. Цель игры - разминировать поле, находя мины и не попадая на них.

## Основные компоненты программы

### 1. Графический интерфейс 🎨
Реализован с использованием библиотеки Tkinter. Включает:
- Главное меню
- Кнопки для выбора размера поля
- Кнопки для начала игры

### 2. Поле игры ⛏️
Состоит из двумерного массива, где каждая клетка может быть:
- Пустой
- Содержать мину
- Содержать цифру, указывающую на количество мин в окрестности

### 3. Кнопки на поле 🎯
Представляют собой клетки поля и позволяют игроку кликать на них. При клике на пустую клетку, она открывается, и если клетка соседствует с миной, то вокруг неё открываются клетки, которые не содержат мин.

### 4. Правила игры 📜
Отображаются в окне с информацией о том, как правильно играть в "Сапер".

### 5. Опции игры ⚙️
Включают возможность выбора размера поля и количества мин.

## Функциональность и механика игры

### 1. Выбор размера поля и количества мин 🗺️
Игрок может выбрать размер поля и количество мин перед началом игры.

### 2. Начало игры 🎬
После выбора размера и количества мин, игрок может начать игру, и поле с минами отображается на экране.

### 3. Клик по клеткам 🔍
Игрок может кликать по клеткам поля, чтобы разминировать их. Если клетка содержит мину, игра заканчивается.

### 4. Автоматическое открытие клеток 🔓
Если игрок кликает по клетке, которая содержит цифру, то вокруг неё автоматически открываются клетки, которые не содержат мин.

### 5. Проигрыш и победа 🏆
- **Проигрыш**: Если игрок нажимает на мину, игра заканчивается.
- **Победа**: Если игрок разминировал всё поле, то он побеждает.

### 6. Правила и источник кода 📖
## Правила игры 📜
- Ваша задача - разминировать поле, на котором расположены мины.
- Кликните на клетку, чтобы узнать, что там находится.
  - Если клетка содержит мину, игра заканчивается.
  - Если клетка пустая, то вокруг откроются клетки, которые никак не связаны с минами.
  - Если клетка содержит цифру, то это количество мин, которые находятся вокруг неё.
- Левой кнопкой мыши вы можете открывать поля, а правой помечать для себя, где находятся мины.


## Инструкции для использования программы

1. **Запустите программу**: Выберите размер поля и количество мин, которые вы хотите использовать.
2. **Нажмите кнопку "Начать игру"**: Начните игру.
3. **Кликните по клеткам поля**: Разминируйте их.
4. **Итог игры**: Если вы нажимаете на мину, игра закончится. Если вы разминировали всё поле, вы выиграли.
5. **Посмотрите правила и код**: Чтобы узнать правила игры или посмотреть на исходный код проекта, нажмите соответствующие кнопки в главном меню.

---

Приятной игры в "Сапер"! Если у вас есть вопросы или предложения, не стесняйтесь обращаться. Удачи! 🎉

