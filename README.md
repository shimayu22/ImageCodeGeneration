# GooglePhotoの画像URLを使ってWordPress用のタグを生成する

WordPressプラグインの「Photo Express for Google」が使えなくなってしまったので、  URLを入力するとURLを画像表示するタグを生成してくれるアプリ（？）を作りました。

また、生成した際にタグをクリップボードへ追加します。

pyperclipを使用しているので、インストールしておいてください。

```pip install pyperclip```

## 使い方

1.Googleフォトの公開設定済みの画像を表示し、右クリック→画像アドレスをコピーを選択する
1.ImageCodeGenerationを実行します
1.URLを入力（ペースト）してEnter
1.クリップボードへ追加されているので、WordPressのコードが書かれている方へ貼り付けます
1.無限ループしているので、まだ追加する画像があれば同じようにURLを入力してください
1.「n」を入力してEnterを押すとプログラムが終了します

Generate code for WordPress using Google Photo image URL

