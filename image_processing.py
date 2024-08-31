from PIL import Image, ImageEnhance, ImageOps
import numpy as np


def apply_adjustment(image, adjustments):
    edited = image.copy()
    for adjustment, factor in adjustments.items():
        if adjustment in ["Brightness", "Exposure"]:
            edited = ImageEnhance.Brightness(edited).enhance(factor)
        elif adjustment == "Contrast":
            edited = ImageEnhance.Contrast(edited).enhance(factor)
        elif adjustment == "Saturation":
            edited = ImageEnhance.Color(edited).enhance(factor)
        elif adjustment == "Sharpness":
            edited = ImageEnhance.Sharpness(edited).enhance(factor)
        elif adjustment == "Hue":
            edited = adjust_hue(edited, factor)
        elif adjustment == "Highlights":
            edited = adjust_highlights(edited, factor)
        elif adjustment == "Shadows":
            edited = adjust_shadows(edited, factor)
        elif adjustment == "Whites":
            edited = adjust_whites(edited, factor)
        elif adjustment == "Blacks":
            edited = adjust_blacks(edited, factor)
        elif adjustment == "Temperature":
            edited = adjust_temperature(edited, factor)
        elif adjustment == "Tint":
            edited = adjust_tint(edited, factor)
        elif adjustment == "Vibrance":
            edited = adjust_vibrance(edited, factor)
    return edited


def adjust_hue(image, factor):
    hsv = image.convert('HSV')
    h, s, v = hsv.split()
    h = h.point(lambda x: (x + int(factor * 255)) % 256)
    return Image.merge('HSV', (h, s, v)).convert('RGB')


def adjust_highlights(image, factor):
    img_array = np.array(image).astype(np.float32)
    mask = img_array > 192
    img_array[mask] = np.clip(img_array[mask] * factor, 0, 255)
    return Image.fromarray(np.uint8(img_array))


def adjust_shadows(image, factor):
    img_array = np.array(image).astype(np.float32)
    mask = img_array < 64
    img_array[mask] = np.clip(img_array[mask] * factor, 0, 255)
    return Image.fromarray(np.uint8(img_array))


def adjust_whites(image, factor):
    img_array = np.array(image).astype(np.float32)
    mask = img_array > 224
    img_array[mask] = np.clip(img_array[mask] * factor, 0, 255)
    return Image.fromarray(np.uint8(img_array))


def adjust_blacks(image, factor):
    img_array = np.array(image).astype(np.float32)
    mask = img_array < 32
    img_array[mask] = np.clip(img_array[mask] * factor, 0, 255)
    return Image.fromarray(np.uint8(img_array))


def adjust_temperature(image, factor):
    r, g, b = image.split()
    r = r.point(lambda x: x * (1 + factor))
    b = b.point(lambda x: x * (1 - factor))
    return Image.merge('RGB', (r, g, b))


def adjust_tint(image, factor):
    r, g, b = image.split()
    g = g.point(lambda x: x * (1 + factor))
    return Image.merge('RGB', (r, g, b))


def adjust_vibrance(image, factor):
    hsv = image.convert('HSV')
    h, s, v = hsv.split()
    s = s.point(lambda x: x * (1 + factor * (1 - x / 255)))
    return Image.merge('HSV', (h, s, v)).convert('RGB')


def flip_image(image, direction):
    if direction == "Horizontal":
        return ImageOps.mirror(image)
    elif direction == "Vertical":
        return ImageOps.flip(image)
    return image
