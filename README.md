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
1. homeにstart.shを作成
nohup node-red-pi –max-old-space-size=256 > node-red.log &
cd /home/pi/I2C0x52-IR
nohup python flask_server.py > flask.log &

## 
Node-RED Alexa Home Skill Bridge
1. ブラウザでhttps://alexa-node-red.bm.hardill.me.uk/に接続
1. ma_si_620_bed/...でログイン
1. 新しいボタンを追加(例：name=description=bed_aircon_reibou, Actions=on, type=switch)

## リモコンの学習
1. 真ん中のスイッチをlearn側にする
1. 1ボタンを押す
1. 記憶したいリモコンのボタンを押す（緑が光る）
1. 真ん中のスイッチをcontrol側にする
1. 1ボタンを押してボタンが記憶されているか確認

## トラブルシューティング
- ラズパイのフィルの中身を見たい・編集したい
    - windowsなどでsdをマウントしても、bootパーティションしか見れない→ほかのラズパイにsdをさすと、中身を確認できる
- ラズパイ zero whのwifiは5Ghzでは動かない