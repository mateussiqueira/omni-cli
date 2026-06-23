#!/usr/bin/env python3
"""Generate Omni CLI logo and banner assets."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ASSETS_DIR = Path(__file__).parent.parent / "assets"
ASSETS_DIR.mkdir(exist_ok=True)

# Color palette
DARK_BG = (13, 17, 23)  # GitHub dark bg
BLUE = (59, 130, 246)
CYAN = (6, 182, 212)
MAGENTA = (236, 72, 153)
WHITE = (255, 255, 255)
LIGHT_GRAY = (156, 163, 175)


def get_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    """Get a fallback font."""
    font_names = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFCompact.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for font_name in font_names:
        try:
            return ImageFont.truetype(font_name, size)
        except Exception:
            continue
    return ImageFont.load_default()


def draw_gradient_background(draw: ImageDraw.Draw, size: int, color1: tuple, color2: tuple) -> None:
    """Draw a vertical gradient background."""
    for y in range(size):
        ratio = y / size
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))


def create_logo(size: int = 1024) -> Image.Image:
    """Create the main square logo."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background with rounded rectangle
    padding = size // 16
    corner_radius = size // 8
    draw.rounded_rectangle(
        [(padding, padding), (size - padding, size - padding)],
        radius=corner_radius,
        fill=DARK_BG,
    )

    center = size // 2

    # Draw hub symbol - central circle with orbiting dots
    main_radius = size // 6
    orbit_radius = size // 3.2
    dot_radius = size // 22

    # Orbit ring
    draw.ellipse(
        [
            (center - orbit_radius, center - orbit_radius),
            (center + orbit_radius, center + orbit_radius),
        ],
        outline=(255, 255, 255, 40),
        width=size // 80,
    )

    # Orbiting dots (3 dots at 120 degrees)
    import math
    colors = [BLUE, CYAN, MAGENTA]
    for i, color in enumerate(colors):
        angle = math.radians(i * 120 - 90)
        x = center + orbit_radius * math.cos(angle)
        y = center + orbit_radius * math.sin(angle)
        draw.ellipse(
            [
                (x - dot_radius, y - dot_radius),
                (x + dot_radius, y + dot_radius),
            ],
            fill=color,
        )
        # Connect to center
        draw.line([(center, center), (x, y)], fill=color, width=size // 120)

    # Central circle
    draw.ellipse(
        [
            (center - main_radius, center - main_radius),
            (center + main_radius, center + main_radius),
        ],
        fill=(30, 41, 59),
        outline=CYAN,
        width=size // 60,
    )

    # Letter O in center
    font = get_font(size // 3, bold=True)
    bbox = draw.textbbox((0, 0), "O", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    draw.text(
        (center - text_width // 2, center - text_height // 2 - size // 40),
        "O",
        font=font,
        fill=WHITE,
    )

    # Text below symbol
    font_small = get_font(size // 12, bold=True)
    bbox = draw.textbbox((0, 0), "OMNI", font=font_small)
    text_width = bbox[2] - bbox[0]
    draw.text(
        (center - text_width // 2, center + orbit_radius + size // 16),
        "OMNI",
        font=font_small,
        fill=WHITE,
    )

    font_tiny = get_font(size // 24)
    bbox = draw.textbbox((0, 0), "CLI", font=font_tiny)
    text_width = bbox[2] - bbox[0]
    draw.text(
        (center - text_width // 2, center + orbit_radius + size // 8),
        "CLI",
        font=font_tiny,
        fill=LIGHT_GRAY,
    )

    return img


def create_banner(width: int = 1500, height: int = 500) -> Image.Image:
    """Create a wide banner for README."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background
    draw.rectangle([(0, 0), (width, height)], fill=DARK_BG)

    # Decorative gradient orbs
    draw.ellipse(
        [(width * 0.7, -height * 0.3), (width * 1.2, height * 0.7)],
        fill=(59, 130, 246, 30),
    )
    draw.ellipse(
        [(width * 0.6, height * 0.4), (width * 0.9, height * 1.1)],
        fill=(236, 72, 153, 20),
    )

    # Logo on the left (smaller)
    logo_size = height * 3 // 5
    logo = create_logo(size=512)
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
    img.paste(logo, (height // 4, (height - logo_size) // 2), logo)

    # Text on the right
    x_text = height // 4 + logo_size + height // 6
    y_center = height // 2

    font_title = get_font(height // 4, bold=True)
    bbox = draw.textbbox((0, 0), "OMNI", font=font_title)
    text_height = bbox[3] - bbox[1]
    draw.text(
        (x_text, y_center - text_height),
        "OMNI",
        font=font_title,
        fill=WHITE,
    )

    font_subtitle = get_font(height // 12, bold=True)
    bbox = draw.textbbox((0, 0), "The CLI of CLIs", font=font_subtitle)
    text_height = bbox[3] - bbox[1]
    draw.text(
        (x_text, y_center + height // 20),
        "The CLI of CLIs",
        font=font_subtitle,
        fill=CYAN,
    )

    font_tagline = get_font(height // 20)
    bbox = draw.textbbox((0, 0), "Unified hub to orchestrate development tools", font=font_tagline)
    text_height = bbox[3] - bbox[1]
    draw.text(
        (x_text, y_center + height // 6),
        "Unified hub to orchestrate development tools",
        font=font_tagline,
        fill=LIGHT_GRAY,
    )

    return img


def create_favicon(size: int = 64) -> Image.Image:
    """Create a small favicon (symbol only)."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    padding = size // 8
    draw.rounded_rectangle(
        [(padding, padding), (size - padding, size - padding)],
        radius=size // 6,
        fill=DARK_BG,
    )

    center = size // 2
    main_radius = size // 3
    import math

    # Small orbiting dots
    orbit_radius = size // 2.5
    dot_radius = max(size // 12, 2)
    colors = [BLUE, CYAN, MAGENTA]
    for i, color in enumerate(colors):
        angle = math.radians(i * 120 - 90)
        x = center + orbit_radius * math.cos(angle)
        y = center + orbit_radius * math.sin(angle)
        draw.ellipse(
            [
                (x - dot_radius, y - dot_radius),
                (x + dot_radius, y + dot_radius),
            ],
            fill=color,
        )

    # Central circle
    draw.ellipse(
        [
            (center - main_radius, center - main_radius),
            (center + main_radius, center + main_radius),
        ],
        fill=(30, 41, 59),
        outline=CYAN,
        width=max(size // 30, 1),
    )

    return img


def main() -> None:
    """Generate all logo assets."""
    print("Generating Omni CLI logo assets...")

    logo = create_logo(1024)
    logo_path = ASSETS_DIR / "logo.png"
    logo.save(logo_path, "PNG")
    print(f"✅ Saved: {logo_path}")

    banner = create_banner(1500, 500)
    banner_path = ASSETS_DIR / "banner.png"
    banner.save(banner_path, "PNG")
    print(f"✅ Saved: {banner_path}")

    favicon = create_favicon(64)
    favicon_path = ASSETS_DIR / "favicon.png"
    favicon.save(favicon_path, "PNG")
    print(f"✅ Saved: {favicon_path}")

    # Also create a social preview (1280x640)
    social = create_banner(1280, 640)
    social_path = ASSETS_DIR / "social-preview.png"
    social.save(social_path, "PNG")
    print(f"✅ Saved: {social_path}")

    print("\nAll assets generated successfully!")


if __name__ == "__main__":
    main()
