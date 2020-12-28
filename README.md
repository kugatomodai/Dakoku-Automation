# Dakoku-Automation
ワーク◯アプリケーション 就労・プロジェクト管理 web打刻の自動化
<br>
seleniumを用いて打刻を自動化します。Google chromeでの使用をイメージしています。
Chromedriverが必要になるので、ご使用のGoogle chromeバージョンに合うwebdriverをダウンロードしてください。
<br>
https://sites.google.com/a/chromium.org/chromedriver/downloads
<br>
macでは、AutomatorとCalendarアプリで実行タイミングをスケジュールできます。
<br>

## var.py
ユーザ名やURLなど、ユーザごとに異なる情報についてをまとめてこちらに記述します。
<br>
こちらで記述した変数は、taikin.pyやshukkinn.pyで参照します。
<br>
## taikin.py
webページにユーザ情報を渡し、退勤ボタンを押します。
<br>
入力・退勤ボタンを押しおえたら、ブラウザを閉じます。

## shukkinn.py
webページにユーザ情報を渡し、出勤ボタンを押します。
<br>
入力・退勤ボタンを押しおえたら、ブラウザを閉じます。

