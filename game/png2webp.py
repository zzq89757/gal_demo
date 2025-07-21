from PIL import Image
from pathlib import Path

def compress_images_to_webp(input_folder: str, output_folder: str, quality: int = 85):
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    image_files = list(input_path.glob("*.png"))

    for img_file in image_files:
        with Image.open(img_file) as img:
            webp_path = output_path / (img_file.stem + ".webp")
            img.save(webp_path, format="WEBP", quality=quality, method=6)
            # img.save(webp_path, format="WEBP", quality=quality, lossless=True)
            print(f"Compressed: {img_file.name} -> {webp_path.name}")

    print(f"\nFinished. {len(image_files)} images converted to WebP.")


if __name__ == "__main__":
    # 替换为你的文件夹路径
    # compress_images_to_webp(r"images\差分\2_天使差分", r"images\差分\2_天使差分", quality=85)
    # compress_images_to_webp(r"images\差分\3_死神差分", r"images\差分\3_死神差分", quality=90)
    # compress_images_to_webp(r"images\差分\4_吸血姬差分", r"images\差分\4_吸血姬差分", quality=90)
    compress_images_to_webp(r"images\差分\5_骑士差分", r"images\差分\5_骑士差分", quality=90)
    compress_images_to_webp(r"images\差分\6_妹妹差分", r"images\差分\6_妹妹差分", quality=90)
    compress_images_to_webp(r"images\差分\7_boss", r"images\差分\7_boss", quality=90)
    compress_images_to_webp(r"images\差分", r"images\差分", quality=90)
