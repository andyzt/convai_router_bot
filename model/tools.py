from io import BytesIO
from pathlib import Path
from textwrap import wrap

from PIL import Image as Im, ImageDraw, ImageFont

path_to_font = Path(__file__).resolve().parents[0] / 'arial.ttf'


def get_image_from_text(text: str) -> bytes:
    """Generates jpeg image as bytes array for profile description and profile topic.

    Args:
        text: Message that will be converted to image.

    Returns:
        Generated image as bytes array.

    """
    font_size = 50
    bg_color = (255, 255, 255)
    fnt_color = (0, 0, 0)
    fnt = ImageFont.truetype(str(path_to_font), font_size)

    lines = []
    for piece in text.split('\n'):
        lines.extend(wrap(piece, width=25) or [''])

    width = 20
    if lines:
        width += max([fnt.getsize(line)[0] for line in lines])
    height = max(width // 2, len(lines) * font_size + 20)
    img = Im.new('RGB', (width, height), color=bg_color)
    d = ImageDraw.Draw(img)
    for i, line in enumerate(lines):
        x_begin = (width - fnt.getsize(line)[0]) // 2
        d.text((x_begin, 10 + i * font_size), line, font=fnt, fill=fnt_color)
    output = BytesIO()
    img.save(output, format='JPEG')
    return output.getvalue()
