# GooglePhotoの画像URLを使ってWordPress用のタグを生成する

Generate code for WordPress using Google Photo image URL

WordPressプラグインの「Photo Express for Google」が使えなくなってしまったので、  
URLを入力するとURLを画像表示するタグを生成してくれるアプリ（？）を作りました。

また、生成した際にタグをクリップボードへ追加します。

pyperclipを使用しているので、インストールしておいてください。

```pip install pyperclip```

## 使い方

1. Googleフォトの公開設定済みの画像を表示し、右クリック→画像アドレスをコピーを選択する
1. ImageCodeGenerationを実行します
1. URLを入力（ペースト）してEnter
1. クリップボードへ追加されているので、WordPressのコードが書かれている方へ貼り付けます
1. 無限ループしているので、まだ追加する画像があれば同じようにURLを入力してください
1. 「n」を入力してEnterを押すとプログラムが終了します


例）
```<span itemtype="http://schema.org/Photograph" itemscope="itemscope"><img class="magnifiable" src="画像URL" itemprop="image"></span>```


参考：https://www.tsuruyahonnpo.com/2019/01/20/photo-express-for-google-%E3%81%8C%E4%BD%BF%E3%81%88%E3%81%AA%E3%81%8F%E3%81%AA%E3%81%A3%E3%81%A1%E3%82%83%E3%81%A3%E3%81%9F/
