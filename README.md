# raspi-remocon

## frontendの開発
1. docker compose up
1. vue-appコンテナにアタッチ
1. cd /frontend
1. export NODE_OPTIONS=--openssl-legacy-provider 
    - opensslの問題のため
1. npm install
1. npm run serve
    - dev serverが開く(hostのブラウザで開く場合はport=8083なので注意)
1. 編集
1. 出来上がったらbuild
    - npm run build
1. ラズパイに送る
    - sftp {user}@{ip}
    - put frontend
1. 送ったfrontendフォルダをラズパイの~/I2C0x52-IR/remoconフォルダに変更
1. ラズパイを再起動sudo shutdown -r now
1. 変更が反映されていることを確認

## bedpiのリストア
1. bedpiのsdをほかのラズパイにさして起動
1. host pocからほかのラズパイにsftpでつなぐ
1. homeの下を他のラズパイの/media/...で見れるようになるので、home/I...以下をgetする(remoconのnodemodule以下は重いのでどこかにうつしておく)
1. 新しいbedpiをラズパイimagerでやく
1. sshで接続
1. sudo raspi-config -> Interface Options -> I2CをEnable
1. pythonの準備
    cd ~
    python -m venv env
    source env/bin/activate
    pip install flask flask_cors
1. 下のリモコンの学習を参考にスイッチを追加
1. nodeの準備
    bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
1. nodeの登録
    1. node-red-start
    1. ブラウザに接続して(nodeの準備で入れたユーザ名とパスを入れる)ノードを加えていく
    1. [こちら](https://qiita.com/g-iki/items/a5d4d4674a30de7ed124)を参考にする
1. homeにstart.shを作成
nohup node-red-pi –max-old-space-size=256 > node-red.log &
cd /home/pi/I2C0x52-IR
nohup /home/pi/env/bin/python flask_server.py > flask.log &
1. crontabの設定
    crotab -eで一番したに@reboot sh /home/pi/start.sh
1. sh start.shで始まる

## Node-RED Alexa Home Skill Bridgeの設定
1. ブラウザでhttps://alexa-node-red.bm.hardill.me.uk/に接続
1. xxxx_bed/...でログイン
1. 新しいボタンを追加(例：name=description=bed_aircon_reibou, Actions=on, type=switch)

## alexaの設定
1. 音声でアレクサ新しいデバイスを検索して、というと先ほど登録したbed_aircon_reibouが追加される
1. スマホのalexaアプリで右下のその他 -> 定型アクション -> 右上の+追加ボタン -> 実行条件を追加で音声を登録 -> アクションを追加 -> スマートホーム -> スイッチ -> 先ほど登録したbed_aircon_reibouを登録

## リモコンの学習
1. 真ん中のスイッチをlearn側にする
1. 1ボタンを押す
1. 記憶したいリモコンのボタンを押す（緑が光る）
1. 真ん中のスイッチをcontrol側にする
1. 1ボタンを押してボタンが記憶されているか確認
1. save_sig.py 0 bed_aircon_reibou28みたいな感じで保存する(1に記録したやつは0にあるので注意)

## その他
- /home/pi/I2C0x52-IRに以下を置く
    - save_sig.py: リモコンの内容の保存に使う
    - trans_sig.py: 赤外を出すのに使う
    - flask_server.py: flask起動に使う

## トラブルシューティング
- ラズパイのフィルの中身を見たい・編集したい
    - windowsなどでsdをマウントしても、bootパーティションしか見れない→ほかのラズパイにsdをさすと、中身を確認できる
- ラズパイ zero whのwifiは5Ghzでは動かない
