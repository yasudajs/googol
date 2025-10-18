# Googol - 歯車回転アニメーション

Pythonとmatplotlibを使用して、歯車の回転をシミュレートするアニメーションを生成するプロジェクトです。

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![matplotlib](https://img.shields.io/badge/matplotlib-3.10.7-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 概要

このプロジェクトは、複数の歯車が連動して回転する様子をアニメーションで表現します。各歯車は2:1の減速比で接続されており、上の歯車ほど速く回転します。

## 特徴

- 🔄 **リアルな回転表現**: 円周上を移動する赤いマーカーで実際の回転を可視化
- 📊 **回転数表示**: 各歯車の回転数をリアルタイムで表示（小数点1桁まで）
- ⏱️ **経過時間表示**: アニメーションの経過時間を表示
- 🎥 **MP4出力**: 60秒間のMP4動画として保存
- ⚙️ **カスタマイズ可能**: 歯車数、回転比、フレームレートなどを簡単に変更可能

## 必要な環境

- Python 3.12+
- ffmpeg（動画生成に必要）

## インストール

1. リポジトリをクローン:
```bash
git clone https://github.com/yasudajs/googol.git
cd googol
```

2. 仮想環境を作成・有効化:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# または
.venv\Scripts\activate     # Windows
```

3. 必要なライブラリをインストール:
```bash
pip install matplotlib numpy
```

4. ffmpegをインストール（Ubuntu/Debian）:
```bash
sudo apt update
sudo apt install -y ffmpeg
```

## 使用方法

1. スクリプトを実行:
```bash
python googol.py
```

2. `gear_rotation_2x_15fps_60sec.mp4`が生成されます

## パラメータのカスタマイズ

`googol.py`内の以下のパラメータを変更できます：

```python
fps = 15                    # フレームレート
duration_sec = 60          # アニメーション時間（秒）
num_gears = 10             # 歯車の数
rotation_ratio = 2         # 減速比
gear_radius = 0.5          # 歯車の半径
```

## 生成される動画の仕様

- **解像度**: 図のサイズに依存（デフォルト: 6x10インチ）
- **フレームレート**: 15 FPS
- **時間**: 60秒
- **フォーマット**: MP4
- **コーデック**: ffmpeg

## ファイル構成

```
googol/
├── googol.py                           # メインスクリプト
├── .gitignore                          # Git除外設定
├── README.md                           # このファイル
└── gear_rotation_2x_15fps_60sec.mp4   # 生成される動画（Gitでは追跡されません）
```

## 技術詳細

- **matplotlib**: グラフィック描画とアニメーション
- **numpy**: 数値計算（三角関数など）
- **ffmpeg**: 動画エンコーディング

### アニメーションの仕組み

1. 各歯車を円として描画
2. 赤いマーカーを円周上に配置
3. フレームごとに回転角度を更新
4. マーカーの位置を`cos`と`sin`で計算
5. 回転数を`角度/(2π)`で算出

## ライセンス

MIT License

## 作者

yasudajs

## 貢献

プルリクエストやイシューを歓迎します！

## 今後の改善予定

- [ ] GIF出力対応
- [ ] 歯車の歯の描画
- [ ] 色のカスタマイズ
- [ ] インタラクティブなパラメータ調整UI