import { access, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const qrDirectory = path.resolve(process.argv[2] ?? "QR");
const outputPath = path.resolve(
  process.argv[3] ?? path.join(qrDirectory, "numberAndQR.csv"),
);

function escapeCsv(value) {
  const text = String(value);
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

const headers = [];
for (let slot = 1; slot <= 10; slot += 1) {
  headers.push(`number${slot}`, `@qr${slot}`);
}

const rows = [headers];
for (let rowStart = 1; rowStart <= 100; rowStart += 10) {
  const row = [];

  for (let number = rowStart; number < rowStart + 10; number += 1) {
    const imagePath = path.join(qrDirectory, `${number}.svg`);
    await access(imagePath);
    row.push(number, imagePath);
  }

  rows.push(row);
}

const csv = `${rows.map((row) => row.map(escapeCsv).join(",")).join("\n")}\n`;
await writeFile(outputPath, csv, "utf8");

console.log(`作成しました: ${outputPath}`);
console.log(`画像の絶対パス: ${qrDirectory}`);
if (/\s/.test(qrDirectory)) {
  console.warn("注意: Adobeの推奨に従い、フォルダー名から空白を除くと安全です。");
}
