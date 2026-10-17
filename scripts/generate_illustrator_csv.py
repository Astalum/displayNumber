#!/usr/bin/env python3

import argparse
import csv
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Illustrator用のQRコード差し込みCSVを作成します。"
    )
    parser.add_argument(
        "path",
        type=Path,
        help="1.svg〜100.svgが入っているQRディレクトリのパス",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    qr_directory = args.path.expanduser().resolve()

    if not qr_directory.is_dir():
        print(
            f"エラー: QRディレクトリが見つかりません: {qr_directory}",
            file=sys.stderr,
        )
        return 1

    image_paths = {
        number: qr_directory / f"{number}.svg" for number in range(1, 101)
    }
    missing_files = [image_path for image_path in image_paths.values() if not image_path.is_file()]

    if missing_files:
        print("エラー: 次のSVGファイルが見つかりません。", file=sys.stderr)
        for image_path in missing_files:
            print(f"- {image_path}", file=sys.stderr)
        return 1

    headers = []
    for slot in range(1, 11):
        headers.extend((f"number{slot}", f"@qr{slot}"))

    output_path = qr_directory / "numberAndQR.csv"
    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, lineterminator="\n")
        writer.writerow(headers)

        for row_start in range(1, 101, 10):
            row = []
            for number in range(row_start, row_start + 10):
                row.extend((number, str(image_paths[number])))
            writer.writerow(row)

    print(f"作成しました: {output_path}")
    print(f"画像の絶対パス: {qr_directory}")

    if any(character.isspace() for character in str(qr_directory)):
        print(
            "注意: Adobeの推奨に従い、フォルダー名から空白を除くと安全です。",
            file=sys.stderr,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
