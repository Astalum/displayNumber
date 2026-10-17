import { mkdir } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { createInterface } from "node:readline/promises";
import QRCode from "qrcode";

const baseUrl = "https://astalum.github.io/displayNumber";

async function askForNumber() {
  const terminal = createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  try {
    return (await terminal.question("番号を入力してください（例: 42）: ")).trim();
  } finally {
    terminal.close();
  }
}

const number = process.argv[2]?.trim() || (await askForNumber());

if (!/^[0-9]+$/.test(number)) {
  console.error("エラー: 番号は半角数字で入力してください。");
  process.exitCode = 1;
} else {
  const outputDirectory = path.resolve("QR");
  const outputPath = path.join(outputDirectory, `${number}.svg`);
  const url = `${baseUrl}/${number}`;

  await mkdir(outputDirectory, { recursive: true });
  await QRCode.toFile(outputPath, url, {
    type: "svg",
    errorCorrectionLevel: "H",
    margin: 4,
  });

  console.log(`作成しました: QR/${number}.svg`);
  console.log(`URL: ${url}`);
}
