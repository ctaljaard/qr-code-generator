import qrcode
from PIL import ImageColor
import os


def validate_color(color: str):
    """Validate and convert a color input (hex or named) to RGB."""
    try:
        return ImageColor.getcolor(color.lower(), "RGB")
    except ValueError:
        return None


def ensure_png_extension(filename: str) -> str:
    """Ensure the filename has a .png extension."""
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        filename += '.png'
    return filename


def generate_qr(data: str, filepath: str, filename: str, fill_color: str = '#000000', back_color: str = '#FFFFFF',
                border_size: int = 1):
    """Generate and save a QR code with custom colors."""
    fill_rgb, back_rgb = validate_color(fill_color), validate_color(back_color)
    if not fill_rgb or not back_rgb:
        print("Error: Invalid color. Use a valid hex code (e.g., #FF5733) or color name (e.g., red).")
        return

    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=border_size
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white').convert("RGBA")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            if pixels[i, j][:3] == (0, 0, 0):  # Black pixels
                pixels[i, j] = fill_rgb
            elif pixels[i, j][:3] == (255, 255, 255):  # White pixels
                pixels[i, j] = back_rgb

    filename = ensure_png_extension(filename)
    full_path = os.path.join(filepath, filename)
    img.save(full_path)
    print(f"QR Code saved as {full_path}")


def get_filepath():
    """Prompt user for a directory to save the QR code."""
    filepath = input("Enter the directory to save the QR code (e.g., /path/to/folder): ").strip()
    return filepath if filepath else None


def get_filename():
    """Prompt user for a filename and ensure it has a valid extension."""
    filename = input("Enter the filename to save the QR code (e.g., output.png): ").strip()
    return ensure_png_extension(filename) if filename else None


def main():
    """Handle user input and generate a QR code."""
    data = input("Enter text or URL for the QR code: ").strip()
    if not data:
        print("Error: No data provided.")
        return

    fill_color = input("Enter fill color (default: '#000000'): ") or '#000000'
    back_color = input("Enter background color (default: '#FFFFFF'): ") or '#FFFFFF'

    try:
        border_size = int(input("Enter border size (default: 1): ") or 1)
    except ValueError:
        print("Invalid input. Using default border size of 1.")
        border_size = 1

    filepath = get_filepath()
    filename = get_filename()

    if filepath and filename:
        generate_qr(data, filepath, filename, fill_color, back_color, border_size)
    else:
        print("Invalid path or filename. QR code not saved.")


if __name__ == "__main__":
    main()
