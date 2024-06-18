from PIL import Image, ImageDraw

# Создаем новое изображение
image = Image.new("RGB", (400, 200), "white")
draw = ImageDraw.Draw(image)

# --- Рисуем букву Д ---
draw.line([(20, 20), (20, 120)], fill="blue", width=10)  # Вертикальная линия
draw.arc([(20, 20), (150, 150)], start=0, end=180, fill="blue", width=10)  # Дуга

# --- Рисуем букву А ---
draw.line([(120, 120), (150, 20)], fill="red", width=10)  # Левая диагональ
draw.line([(150, 20), (180, 120)], fill="red", width=10)  # Правая диагональ
draw.line([(135, 70), (165, 70)], fill="red", width=10)  # Перекладина

# --- Рисуем букву Н ---
draw.line([(200, 20), (200, 120)], fill="green", width=10)  # Левая вертикальная
draw.line([(280, 20), (280, 120)], fill="green", width=10)  # Правая вертикальная
draw.line([(200, 70), (280, 70)], fill="green", width=10)  # Горизонтальная

# --- Рисуем букву И ---
draw.line([(300, 20), (300, 120)], fill="purple", width=10)  # Вертикальная

# --- Рисуем букву И ---
draw.line([(320, 20), (320, 120)], fill="orange", width=10)  # Вертикальная

# --- Рисуем букву Л ---
draw.line([(340, 20), (340, 120)], fill="brown", width=10)  # Вертикальная
draw.line([(340, 120), (380, 120)], fill="brown", width=10)  # Нижняя линия

# Сохраняем изображение
image.save("name.png")
