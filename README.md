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
