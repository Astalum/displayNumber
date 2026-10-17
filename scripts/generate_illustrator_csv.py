#!/usr/bin/env python3

import argparse
import csv
import re
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Illustrator用のQRコード差し込みCSVを作成します。"
    )
    parser.add_argument(
        "path",
        help="Illustratorを使用する別PC上のQRディレクトリのパス",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("QR/numberAndQR.csv"),
        help="CSVの出力先（既定値: QR/numberAndQR.csv）",
    )
    return parser.parse_args()


def build_image_path(qr_directory: str, filename: str) -> str:
    is_windows_path = bool(re.match(r"^[A-Za-z]:[\\/]", qr_directory)) or qr_directory.startswith(
        "\\\\"
    )
    path_type = PureWindowsPath if is_windows_path else PurePosixPath
    return str(path_type(qr_directory) / filename)


def main() -> int:
    args = parse_args()
    qr_directory = args.path.strip()

    if not qr_directory:
        print("エラー: QRディレクトリのパスを指定してください。", file=sys.stderr)
        return 1

    image_paths = {
        number: build_image_path(qr_directory, f"{number}.svg")
        for number in range(1, 101)
    }

    headers = []
    for slot in range(1, 11):
        headers.extend((f"number{slot}", f"@qr{slot}"))

    output_path = args.output.expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, lineterminator="\n")
        writer.writerow(headers)

        for row_start in range(1, 101, 10):
            row = []
            for number in range(row_start, row_start + 10):
                row.extend((number, image_paths[number]))
            writer.writerow(row)

    print(f"作成しました: {output_path}")
    print(f"CSVに記録した別PC上の画像パス: {qr_directory}")
    print("画像ファイルの存在確認は行っていません。")

    if any(character.isspace() for character in str(qr_directory)):
        print(
            "注意: Adobeの推奨に従い、フォルダー名から空白を除くと安全です。",
            file=sys.stderr,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
