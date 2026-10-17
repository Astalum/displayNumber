# displayNumber

URLの末尾に指定した番号を、画面中央に大きく表示するだけのWebページです。

## 使い方

公開URLの末尾に番号を追加します。

```text
https://astalum.github.io/displayNumber/123
```

番号は半角数字に対応し、`001` のような先頭ゼロもそのまま表示されます。

`main` ブランチへのpush時に、GitHub ActionsからGitHub Pagesへ自動公開されます。

## QRコードを作る

初回のみ依存パッケージをインストールします。

```bash
npm install
```

次のコマンドを実行し、表示したい番号を入力します。

```bash
npm run qr
```

入力した番号の公開URLを埋め込んだSVG形式のQRコードが、`QR/番号.svg` に作成されます。

## Illustratorへ流し込む

`QR/illustrator.csv` は、10個の番号とQRコードを1セットとして、1〜100を10データセットにまとめたIllustrator用CSVです。

- `number1`〜`number10`: 番号用のテキスト変数
- `@qr1`〜`@qr10`: QRコード用のリンクファイル変数

CSVとSVGファイルは同じ`QR`ディレクトリに置いたまま使用してください。Illustratorの［ウィンドウ］→［変数］からCSVを読み込み、各変数を対応するテキストまたはリンク画像へ紐付けます。
