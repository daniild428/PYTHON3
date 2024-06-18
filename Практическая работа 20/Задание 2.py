from PIL import Image, ImageDraw

# Цвета
bg_color = (135, 206, 250)  # Голубой фон
tv_color = (0, 0, 0)  # Черный телевизор
stand_color = (139, 69, 19)  # Коричневый столик
speaker_color = (169, 169, 169)  # Серые колонки

# Размеры
width = 600
height = 400
tv_width = 400
tv_height = 250
stand_width = 100
stand_height = 20
speaker_width = 30
speaker_height = 50

# Создаем изображение
image = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(image)

# Рисуем телевизор
tv_x = (width - tv_width) // 2
tv_y = (height - tv_height) // 2 - 30
draw.rectangle(
    [(tv_x, tv_y), (tv_x + tv_width, tv_y + tv_height)], outline=tv_color, width=5
)

# Рисуем подставку
stand_x = tv_x + (tv_width - stand_width) // 2
stand_y = tv_y + tv_height + 10
draw.rectangle(
    [(stand_x, stand_y), (stand_x + stand_width, stand_y + stand_height)],
    fill=stand_color,
)

# Рисуем колонки
speaker_offset = 20
# Левая колонка
draw.rectangle(
    [
        (tv_x - speaker_width - speaker_offset, stand_y - speaker_height),
        (tv_x - speaker_offset, stand_y),
    ],
    fill=speaker_color,
)
# Правая колонка
draw.rectangle(
    [
        (
            tv_x + tv_width + speaker_offset,
            stand_y - speaker_height,
        ),
        (tv_x + tv_width + speaker_offset + speaker_width, stand_y),
    ],
    fill=speaker_color,
)

# Сохраняем изображение
image.save("smart_tv.png")