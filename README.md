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

## リモコンの学習
1. 真ん中のスイッチをlearn側にする
1. 1ボタンを押す
1. 記憶したいリモコンのボタンを押す（緑が光る）
1. 真ん中のスイッチをcontrol側にする
1. 1ボタンを押してボタンが記憶されているか確認