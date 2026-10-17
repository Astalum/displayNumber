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

`QR/numberAndQR.csv` は、10個の番号とQRコードを1セットとして、1〜100を10データセットにまとめたIllustrator用CSVです。

- `number1`〜`number10`: 番号用のテキスト変数
- `@qr1`〜`@qr10`: QRコード用のリンクファイル変数

Illustratorを使用するPCのターミナルで、プロジェクトのルートから次のコマンドを実行します。

```bash
npm run illustrator-csv
```

これにより、各SVGの絶対パスを記録した`QR/numberAndQR.csv`が作成されます。別の場所にあるQRディレクトリを指定する場合は、次のように実行します。

```bash
npm run illustrator-csv -- "/Users/your-name/path/to/QR"
```

Illustratorでは次の順に設定します。

1. ［ファイル］→［配置］でSVGを配置し、［リンク］を有効にする（埋め込まない）
2. ［ウィンドウ］→［変数］→［読み込み］から`numberAndQR.csv`を読み込む
3. 各テキストを`number1`〜`number10`へ紐付ける
4. 各リンク画像を`qr1`〜`qr10`へ［リンクファイルを動的に設定］で紐付ける
5. ［データセット］を切り替えて番号と画像が変わることを確認する
